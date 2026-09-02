import html
import os
import re
import time
from pathlib import Path

import requests

GRAPHQL_URL = "https://leetcode.com/graphql/"
ROOT = Path("problems")

LANG_EXT = {
    "python": "py", "python3": "py", "java": "java", "cpp": "cpp", "c": "c",
    "csharp": "cs", "javascript": "js", "typescript": "ts", "kotlin": "kt",
    "swift": "swift", "golang": "go", "go": "go", "rust": "rs", "ruby": "rb",
    "php": "php", "scala": "scala", "dart": "dart", "sql": "sql",
    "mysql": "sql", "mssql": "sql", "oraclesql": "sql", "postgresql": "sql",
}


def fail(message: str):
    raise RuntimeError(message)


def gql(session: requests.Session, query: str, variables: dict):
    response = session.post(GRAPHQL_URL, json={"query": query, "variables": variables}, timeout=30)
    response.raise_for_status()
    body = response.json()
    if body.get("errors"):
        raise RuntimeError(body["errors"])
    return body.get("data") or {}


def make_session():
    session_cookie = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = os.environ.get("LEETCODE_CSRF_TOKEN", "").strip()
    if not session_cookie or not csrf:
        fail("Missing LEETCODE_SESSION or LEETCODE_CSRF_TOKEN GitHub secret.")

    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Origin": "https://leetcode.com",
        "Referer": "https://leetcode.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/139 Safari/537.36",
        "x-csrftoken": csrf,
    })
    session.cookies.set("LEETCODE_SESSION", session_cookie, domain="leetcode.com")
    session.cookies.set("csrftoken", csrf, domain="leetcode.com")
    return session


def verify_login(session):
    data = gql(session, "query { userStatus { isSignedIn username } }", {})
    status = data.get("userStatus") or {}
    if not status.get("isSignedIn"):
        fail("LeetCode session is not authenticated. Refresh LEETCODE_SESSION and try again.")
    print(f"Authenticated as {status.get('username', 'unknown')}")


def fetch_solved_questions(session):
    query = """
    query userProgressQuestionList($filters: UserProgressQuestionListInput) {
      userProgressQuestionList(filters: $filters) {
        totalNum
        questions { frontendId title titleSlug difficulty lastSubmittedAt }
      }
    }
    """
    try:
        data = gql(session, query, {"filters": {"questionStatus": "SOLVED", "skip": 0, "limit": 1000}})
        result = data.get("userProgressQuestionList") or {}
        questions = result.get("questions") or []
        if questions:
            print(f"Found {len(questions)} solved problems from progress API.")
            return questions
    except Exception as exc:
        print(f"Progress API unavailable; using recent accepted submissions: {exc}")

    username = (gql(session, "query { userStatus { username } }", {}).get("userStatus") or {}).get("username")
    if not username:
        fail("Could not determine LeetCode username.")

    recent_query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
      recentAcSubmissionList(username: $username, limit: $limit) {
        id title titleSlug timestamp lang
      }
    }
    """
    recent = gql(session, recent_query, {"username": username, "limit": 20})
    submissions = recent.get("recentAcSubmissionList") or []
    return [
        {"frontendId": "", "title": item.get("title", "Unknown Problem"),
         "titleSlug": item.get("titleSlug"), "difficulty": "", "lastSubmittedAt": item.get("timestamp")}
        for item in submissions if item.get("titleSlug")
    ]


def fetch_question_meta(session, slug):
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) { questionFrontendId title titleSlug difficulty }
    }
    """
    data = gql(session, query, {"titleSlug": slug})
    return data.get("question") or {}


def fetch_latest_accepted(session, slug):
    query = """
    query questionSubmissionList($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {
      questionSubmissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {
        submissions { id statusDisplay lang timestamp }
      }
    }
    """
    data = gql(session, query, {"offset": 0, "limit": 20, "lastKey": None, "questionSlug": slug})
    result = data.get("questionSubmissionList") or {}
    submissions = result.get("submissions") or []
    accepted = [s for s in submissions if s.get("statusDisplay") == "Accepted"]
    accepted.sort(key=lambda x: int(x.get("timestamp") or 0), reverse=True)
    return accepted[0] if accepted else None


def fetch_submission_code(session, submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code lang { name } runtime memory statusDisplay
      }
    }
    """
    data = gql(session, query, {"submissionId": int(submission_id)})
    return data.get("submissionDetails") or {}


def safe_name(value):
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", value.strip()).strip("-").lower()


def sync_one(session, question):
    slug = question["titleSlug"]
    title = question.get("title") or slug.replace("-", " ").title()
    frontend_id = str(question.get("frontendId") or "").strip()
    difficulty = question.get("difficulty") or ""

    if not frontend_id or not difficulty:
        meta = fetch_question_meta(session, slug)
        frontend_id = str(meta.get("questionFrontendId") or frontend_id)
        difficulty = meta.get("difficulty") or difficulty
        title = meta.get("title") or title

    accepted = fetch_latest_accepted(session, slug)
    if not accepted:
        return False

    details = fetch_submission_code(session, accepted["id"])
    code = html.unescape(details.get("code") or "").replace("\r\n", "\n").replace("\r", "\n")
    if not code:
        print(f"Skipping {slug}: source code unavailable")
        return False

    lang = (accepted.get("lang") or "").lower()
    ext = LANG_EXT.get(lang, re.sub(r"[^a-z0-9]+", "", lang) or "txt")
    prefix = frontend_id.zfill(4) if frontend_id.isdigit() else frontend_id
    problem_dir = ROOT / f"{prefix}-{safe_name(slug)}"
    solution_path = problem_dir / f"solution.{ext}"

    if solution_path.exists():
        return False

    problem_dir.mkdir(parents=True, exist_ok=True)
    solution_path.write_text(code.rstrip() + "\n", encoding="utf-8")

    readme = f"# {title}\n\n"
    if frontend_id:
        readme += f"- **LeetCode:** [{frontend_id}](https://leetcode.com/problems/{slug}/)\n"
    else:
        readme += f"- **LeetCode:** https://leetcode.com/problems/{slug}/\n"
    readme += f"- **Difficulty:** {difficulty or 'Unknown'}\n"
    readme += f"- **Language:** {lang}\n"
    readme += f"- **Submission ID:** `{accepted['id']}`\n\n"
    readme += "> Solution source synced automatically from an accepted LeetCode submission.\n"
    (problem_dir / "README.md").write_text(readme, encoding="utf-8")

    print(f"Synced: {frontend_id} {title} [{lang}]")
    time.sleep(0.5)
    return True


def main():
    ROOT.mkdir(exist_ok=True)
    session = make_session()
    verify_login(session)
    questions = fetch_solved_questions(session)
    if not questions:
        print("No solved problems found. Nothing to sync.")
        return

    added = 0
    for index, question in enumerate(questions, start=1):
        try:
            if sync_one(session, question):
                added += 1
        except Exception as exc:
            print(f"Warning: {question.get('titleSlug')}: {exc}")
        if index % 10 == 0:
            print(f"Progress: {index}/{len(questions)}")

    print(f"Sync complete. Added {added} new solution(s).")


if __name__ == "__main__":
    main()

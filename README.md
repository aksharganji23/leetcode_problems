# LeetCode Problems

Automatically synced LeetCode solutions.

## How it works

A GitHub Actions workflow authenticates to LeetCode with repository secrets, finds solved problems, retrieves the latest accepted submission, and stores the source code in this repository. It uses a small Python GraphQL client instead of the older `joshcai/leetcode-sync` action, which is currently affected by a `submissionList.submissions is not iterable` failure for many accounts.

### Automatic sync

The workflow runs every 30 minutes and can also be started manually from **Actions → Sync LeetCode → Run workflow**.

### Repository structure

```text
leetcode_problems/
├── problems/
│   └── 0001-two-sum/
│       ├── solution.py
│       └── README.md
├── scripts/
│   └── sync_leetcode.py
└── README.md
```

Each problem README contains the LeetCode number, difficulty, language, and submission ID. Problem statements are not copied into the repository.

## Setup required

Add these two GitHub Actions secrets under **Settings → Secrets and variables → Actions**:

- `LEETCODE_CSRF_TOKEN`
- `LEETCODE_SESSION`

The workflow uses the repository's built-in `GITHUB_TOKEN` to commit synced solutions.

> Never commit your LeetCode cookies or tokens into this repository.

# LeetCode Problems

Automatically synced LeetCode solutions.

## How it works

When an accepted LeetCode submission is available, the GitHub Actions workflow syncs it into this repository using LeetCode Sync.

### Automatic sync

The workflow runs every 30 minutes and can also be started manually from **Actions → Sync LeetCode → Run workflow**.

### Repository structure

```text
leetcode_problems/
├── <problem-slug>/
│   └── solution.<language-extension>
└── README.md
```

## Setup required

Add these two GitHub Actions secrets under **Settings → Secrets and variables → Actions**:

- `LEETCODE_CSRF_TOKEN`
- `LEETCODE_SESSION`

The workflow uses the repository's built-in `GITHUB_TOKEN` to commit synced solutions.

> Never commit your LeetCode cookies or tokens into this repository.

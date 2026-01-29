# Scripts

Utility scripts for Personal OS operations. Run with `uv run <script-name>`.

## Available Scripts

| Script | Command | Description |
|--------|---------|-------------|
| `clean_git.py` | `uv run clean-git` | Clean Dropbox conflicted copies from `.git/` |
| `setup_symlinks.py` | `uv run setup-symlinks` | Create symlinks for external skills |

---

## clean-git

**Problem:** When using Git inside Dropbox and working from multiple computers, Dropbox creates "conflicted copy" files when the same `.git/` files are modified on both machines before syncing completes. These files (e.g., `main (Miguel's MacBook Air's conflicted copy 2026-01-24)`) corrupt Git's internal state and cause fetch/pull/push failures.

**Solution:** Run `clean-git` before Git operations to delete these conflicted copies.

```bash
uv run clean-git
```

**Output:**
```
Scanning /path/to/.git for Dropbox conflicts...
Cleaned 6 conflicted file(s)
```

**When to use:** Run this whenever Git commands fail with obscure errors, especially after switching between computers.

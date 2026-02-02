# Scripts

Utility scripts for Personal OS operations. Run with `uv run <script-name>`.

## Available Scripts

| Script | Command | Description |
|--------|---------|-------------|
| `clean_all.py` | `uv run clean` | **Master command** - Clean git + Python environment |
| `clean_git.py` | `uv run clean-git` | Clean Dropbox conflicted copies from `.git/` |
| `clean_env.py` | `uv run clean-env` | Clean and rebuild Python virtual environment |
| `setup_symlinks.py` | `uv run setup-symlinks` | Create symlinks for external skills |

---

## Why These Scripts Exist

When working with Git repositories inside Dropbox (or any cloud storage), multiple computers syncing the same files can create "conflicted copy" files. These happen when:

- You edit files on Computer A before Dropbox finishes syncing changes from Computer B
- Git modifies `.git/` internals (indices, refs, logs) on both machines
- Cloud storage sees these as conflicts and creates backup copies

These conflicted copies break Git operations and can corrupt your Python virtual environment. The cleanup scripts fix these issues.

---

## clean (Master Command)

**What it does:** Runs `clean-git` followed by `clean-env` in one shot.

**Use this when:** Switching computers or when things feel "off" and you want a fresh start.

```bash
uv run clean
```

**Output:**
```
==================================================
MASTER CLEAN - Resetting Git + Python environment
==================================================

[1/2] Cleaning Git conflicts...
  Scanning /path/to/.git...
  Cleaned 3 conflicted file(s)

[2/2] Cleaning Python environment...
  Removing /path/to/.venv...
  Syncing dependencies...

==================================================
All clean! Ready to work.
```

---

## clean-git

**Problem:** Dropbox creates "conflicted copy" files in `.git/` when the same internal Git files are modified on multiple machines. These files (e.g., `main (Miguel's MacBook Air's conflicted copy 2026-01-24)`) corrupt Git's state and cause fetch/pull/push failures.

**Solution:** Delete these conflicted copies to restore Git functionality.

```bash
uv run clean-git
```

**Output:**
```
Scanning /path/to/.git for Dropbox conflicts...
Cleaned 6 conflicted file(s)
```

**When to use:** Run this whenever Git commands fail with obscure errors, especially after switching between computers.

---

## clean-env

**Problem:** Cloud storage conflicts can also affect your Python virtual environment (`.venv/`). When Dropbox syncs partial or corrupted venv files across machines, you get import errors, package conflicts, or mysterious Python crashes. Even without conflicts, sometimes you just need a clean slate.

**Solution:** Delete `.venv/` and run `uv sync` to rebuild from scratch.

```bash
uv run clean-env
```

**Output:**
```
Cleaning Python environment at /path/to/.venv...
  Removing /path/to/.venv...
  Running uv sync...
Environment cleaned and rebuilt successfully
```

**When to use:** 
- When Python imports fail with "module not found" errors
- When you get cryptic package version conflicts
- When switching computers and the environment feels "stale"
- Before important demos or when you want certainty that dependencies are correct

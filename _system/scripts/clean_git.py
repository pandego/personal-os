#!/usr/bin/env -S uv run
"""Clean Dropbox conflicted copies from .git directory."""

import subprocess
from pathlib import Path


def find_git_root() -> Path | None:
    """Find the root of the git repository."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            capture_output=True,
            text=True,
            check=True,
        )
        return Path(result.stdout.strip()).resolve()
    except subprocess.CalledProcessError:
        return None


def clean_conflicted_copies(git_dir: Path) -> int:
    """Delete all Dropbox conflicted copy files in .git directory."""
    count = 0
    for path in git_dir.rglob("*conflicted copy*"):
        if path.is_file():
            print(f"  Deleting: {path.name}")
            path.unlink()
            count += 1
    return count


def main() -> None:
    """Clean Dropbox conflicted copies from git directory."""
    git_dir = find_git_root()

    if not git_dir:
        print("Not in a git repository")
        return

    print(f"Scanning {git_dir} for Dropbox conflicts...")
    count = clean_conflicted_copies(git_dir)

    if count:
        print(f"Cleaned {count} conflicted file(s)")
    else:
        print("No conflicted copies found")


if __name__ == "__main__":
    main()

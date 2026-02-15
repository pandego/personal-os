#!/usr/bin/env -S uv run
"""Clean Dropbox conflicted copies from .git directory."""

import subprocess
from pathlib import Path

from loguru import logger


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
            logger.info(f"  Deleting: {path.name}")
            path.unlink()
            count += 1
    return count


def main() -> None:
    """Clean Dropbox conflicted copies from git directory."""
    git_dir = find_git_root()

    if not git_dir:
        logger.info("Not in a git repository")
        return

    logger.info(f"Scanning {git_dir} for Dropbox conflicts...")
    count = clean_conflicted_copies(git_dir)

    if count:
        logger.info(f"Cleaned {count} conflicted file(s)")
    else:
        logger.info("No conflicted copies found")


if __name__ == "__main__":
    main()

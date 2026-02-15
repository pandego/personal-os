#!/usr/bin/env -S uv run
"""Master cleanup script - runs all cleaners in sequence."""

import sys

from loguru import logger


def run_clean_git() -> bool:
    """Run the git cleanup."""
    logger.info("\n[1/2] Cleaning Git conflicts...")
    try:
        from _system.scripts.clean_git import find_git_root, \
            clean_conflicted_copies

        git_dir = find_git_root()
        if not git_dir:
            logger.info("  Not in a git repository, skipping...")
            return True

        logger.info(f"  Scanning {git_dir}...")
        count = clean_conflicted_copies(git_dir)

        if count:
            logger.info(f"  Cleaned {count} conflicted file(s)")
        else:
            logger.info("  No conflicts found")
        return True
    except Exception as e:
        logger.error(f"  Error: {e}")
        return False


def run_clean_env() -> bool:
    """Run the environment cleanup."""
    logger.info("\n[2/2] Cleaning Python environment...")
    try:
        from _system.scripts.clean_env import find_venv, delete_venv, \
            sync_dependencies

        venv_path = find_venv()

        if not venv_path:
            logger.info("  No .venv found, syncing...")
            return sync_dependencies()

        if delete_venv(venv_path):
            logger.info("  Syncing dependencies...")
            return sync_dependencies()
        return False
    except Exception as e:
        logger.error(f"  Error: {e}")
        return False


def main() -> None:
    """Run all cleaners."""
    logger.info("=" * 50)
    logger.info("MASTER CLEAN - Resetting Git + Python environment")
    logger.info("=" * 50)

    git_ok = run_clean_git()
    env_ok = run_clean_env()

    logger.info("\n" + "=" * 50)
    if git_ok and env_ok:
        logger.success("All clean! Ready to work.")
        sys.exit(0)
    else:
        logger.error("Some cleaners failed. Check output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()

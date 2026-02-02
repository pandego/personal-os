#!/usr/bin/env -S uv run
"""Master cleanup script - runs all cleaners in sequence."""

from pathlib import Path
import sys


def run_clean_git() -> bool:
    """Run the git cleanup."""
    print("\n[1/2] Cleaning Git conflicts...")
    try:
        from _system.scripts.clean_git import find_git_root, clean_conflicted_copies

        git_dir = find_git_root()
        if not git_dir:
            print("  Not in a git repository, skipping...")
            return True

        print(f"  Scanning {git_dir}...")
        count = clean_conflicted_copies(git_dir)

        if count:
            print(f"  Cleaned {count} conflicted file(s)")
        else:
            print("  No conflicts found")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def run_clean_env() -> bool:
    """Run the environment cleanup."""
    print("\n[2/2] Cleaning Python environment...")
    try:
        from _system.scripts.clean_env import find_venv, delete_venv, sync_dependencies

        venv_path = find_venv()

        if not venv_path:
            print("  No .venv found, syncing...")
            return sync_dependencies()

        if delete_venv(venv_path):
            print("  Syncing dependencies...")
            return sync_dependencies()
        return False
    except Exception as e:
        print(f"  Error: {e}")
        return False


def main() -> None:
    """Run all cleaners."""
    print("=" * 50)
    print("MASTER CLEAN - Resetting Git + Python environment")
    print("=" * 50)

    git_ok = run_clean_git()
    env_ok = run_clean_env()

    print("\n" + "=" * 50)
    if git_ok and env_ok:
        print("All clean! Ready to work.")
        sys.exit(0)
    else:
        print("Some cleaners failed. Check output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env -S uv run
"""Clean Python virtual environment and reinstall dependencies."""

import subprocess
import shutil
from pathlib import Path


def find_venv() -> Path | None:
    """Find the virtual environment directory."""
    venv_path = Path(".venv")
    if venv_path.exists() and venv_path.is_dir():
        return venv_path.resolve()
    return None


def delete_venv(venv_path: Path) -> bool:
    """Delete the virtual environment directory."""
    try:
        print(f"  Removing {venv_path}...")
        shutil.rmtree(venv_path)
        return True
    except Exception as e:
        print(f"  Error removing venv: {e}")
        return False


def sync_dependencies() -> bool:
    """Run uv sync to reinstall dependencies."""
    try:
        print("  Running uv sync...")
        result = subprocess.run(
            ["uv", "sync"],
            capture_output=True,
            text=True,
            check=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"  Error running uv sync: {e.stderr}")
        return False


def main() -> None:
    """Clean and rebuild Python environment."""
    venv_path = find_venv()

    if not venv_path:
        print("No .venv directory found, running uv sync...")
        if sync_dependencies():
            print("Environment synced successfully")
        else:
            print("Failed to sync environment")
        return

    print(f"Cleaning Python environment at {venv_path}...")

    if delete_venv(venv_path):
        if sync_dependencies():
            print("Environment cleaned and rebuilt successfully")
        else:
            print("Failed to rebuild environment")
    else:
        print("Failed to clean environment")


if __name__ == "__main__":
    main()

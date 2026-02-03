"""
setup_symlinks.py
Creates symbolic links for skills from external submodules and internal repos.
Safe to run multiple times (idempotent). Cross-platform (macOS, Linux, Windows).

Usage: uv run setup-symlinks
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

# ANSI colors (disabled on Windows unless in modern terminal)
if sys.platform == "win32" and "WT_SESSION" not in os.environ:
    GREEN, YELLOW, RED, NC = "", "", "", ""
else:
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    RED = "\033[0;31m"
    NC = "\033[0m"


def get_repo_root() -> Path:
    """Get the repository root (grandparent of _system/scripts/)."""
    return Path(__file__).resolve().parent.parent.parent


def create_symlink(skills_dir: Path, skill_name: str, relative_target: str) -> bool:
    """
    Create a symlink for a skill.

    Args:
        skills_dir: Path to .claude/skills/
        skill_name: Name of the skill (will be the symlink name)
        relative_target: Relative path from skills_dir to the source

    Returns:
        True if successful or already exists, False if source not found
    """
    link_path = skills_dir / skill_name
    target_path = (skills_dir / relative_target).resolve()

    # Check if source exists
    if not target_path.is_dir():
        print(f"{YELLOW}[SKIP]{NC} {skill_name} - source not found: {relative_target}")
        return False

    # Already a symlink pointing to the right place
    if link_path.is_symlink():
        print(f"{GREEN}[OK]{NC}   {skill_name} - symlink already exists")
        return True

    # Remove existing directory
    if link_path.is_dir():
        print(f"{YELLOW}[DEL]{NC}  {skill_name} - removing existing directory")
        shutil.rmtree(link_path)

    # Create symlink
    # On Windows, need target_is_directory=True for directory symlinks
    link_path.symlink_to(relative_target, target_is_directory=True)
    print(f"{GREEN}[NEW]{NC}  {skill_name} -> {relative_target}")
    return True


def init_submodules(repo_root: Path) -> None:
    """Initialize git submodules if .gitmodules exists."""
    print("Checking submodules...")
    gitmodules = repo_root / ".gitmodules"
    if gitmodules.exists():
        try:
            subprocess.run(
                ["git", "submodule", "update", "--init", "--recursive"],
                cwd=repo_root,
                capture_output=True,
                check=False,
            )
        except FileNotFoundError:
            print(f"{YELLOW}[WARN]{NC} git not found - skipping submodule init")
    print()


def main() -> None:
    """Main entry point."""
    repo_root = get_repo_root()
    skills_dir = repo_root / ".claude" / "skills"

    print("=" * 50)
    print("  Personal OS - Skills Symlink Setup")
    print("=" * 50)
    print()
    print(f"Repository root: {repo_root}")
    print(f"Skills directory: {skills_dir}")
    print()

    # Initialize submodules
    init_submodules(repo_root)

    # Anthropic Skills
    print("--- Anthropic Skills (from _external/anthropic-skills) ---")
    for skill in ["docx", "pdf", "pptx", "xlsx", "brand-guidelines", "skill-creator"]:
        create_symlink(
            skills_dir, skill, f"../../_external/anthropic-skills/skills/{skill}"
        )
    print()

    # Fork Terminal
    print("--- Fork Terminal (from _external/disler-fork-terminal-skill) ---")
    create_symlink(
        skills_dir,
        "fork-terminal",
        "../../_external/disler-fork-terminal-skill/.claude/skills/fork-terminal",
    )
    print()

    # Parallel Thread
    print("--- Parallel Thread (from _external/pandego-parallel-thread-skill) ---")
    create_symlink(
        skills_dir,
        "pthd",
        "../../_external/pandego-parallel-thread-skill/.claude/skills/pthd",
    )
    print()

    # Private Skills (optional)
    print("--- Private Skills (from _internal/private-skills) ---")
    internal_skills = repo_root / "_internal" / "private-skills" / ".claude" / "skills"
    if internal_skills.is_dir():
        for skill in [
            "blog-content",
            "linkedin-content",
            "brand-guidelines-datavengers",
            "datavengers-proposal",
            "comment-suggesting",
        ]:
            create_symlink(
                skills_dir,
                skill,
                f"../../_internal/private-skills/.claude/skills/{skill}",
            )
    else:
        print(
            f"{YELLOW}[WARN]{NC} _internal/private-skills not found - skipping private skills"
        )
        print("       (This is normal if you don't have access to the private repo)")
    print()

    # Summary
    print("=" * 50)
    print("  Setup complete!")
    print("=" * 50)
    print()
    print("Skills kept as regular folders (NOT symlinked):")
    print("  - process-backlog")
    print("  - review")
    print("  - setup-repo")
    print()
    if sys.platform == "win32":
        print("Run 'dir .claude\\skills' to verify symlinks.")
    else:
        print("Run 'ls -la .claude/skills/' to verify symlinks.")


if __name__ == "__main__":
    main()

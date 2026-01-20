# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Personal OS is an AI-powered personal knowledge and content management system organized into three domains: Content (blog, LinkedIn, X, YouTube), Business (portfolio, clients), and Personal (reviews, knowledge). It integrates with Todoist for task capture and Obsidian for visual kanban management.

## Key Commands

| Command | Purpose |
|---------|---------|
| `/setup-repo` | First-time setup (voice config, Python env, Todoist MCP) |
| `/process-backlog` | Sync KANBAN.md ↔ Todoist, clean up messy tasks |
| `/draft-blog [topic]` | Create blog post in `1-content/01-blog/01-drafts/` |
| `/draft-linkedin [topic]` | Create LinkedIn post in `1-content/02-linkedin/01-drafts/` |
| `/draft-tweet [topic]` | Create tweet in `1-content/03-twitter/01-drafts/` |
| `/draft-youtube-script [topic]` | Create YouTube script in `1-content/04-youtube/01-drafts/` |
| `/update-voice [platform]` | Analyze `04-my-top/` + `05-swipe-files/`, update voice guide |
| `/review-week [transcript]` | Generate weekly review from notes |
| `/review-year [transcript]` | Generate yearly review |

## Python Environment

Uses `uv` for dependency management:
```bash
uv sync          # Install dependencies
uv run <script>  # Run with project environment
```

## Architecture

```
1-content/           # Content OS: each platform follows same workflow
  └── 01-blog/
      ├── 01-drafts/     → 02-in-review/ → 03-published/
      ├── 04-my-top/     # Curated best posts (for voice analysis)
      ├── 05-swipe-files/ # External examples
      └── VOICE_blog.md  # Platform-specific voice patterns

2-business/          # Business OS: portfolio, outbound, clients
3-personal/          # Personal OS: reviews, knowledge (private)
.claude/             # Source of truth for all IDE configs
  ├── commands/      # Slash command definitions
  └── skills/        # Reusable automation (process-backlog, setup-repo)
```

## Voice System

Before creating content, always read:
1. `VOICE.md` — Universal identity and patterns, created the first time you run `/setup-repo`.
2. Platform-specific guide (e.g., `1-content/01-blog/VOICE_blog.md`), created when you run `update-voice blog`.

Core patterns: authority via specifics, no corporate jargon, statement hooks (not questions), practitioner-focused.

## Todoist Integration

- Requires "PersonalOS" project in Todoist with board view
- Sections: Backlog | Ready | In Progress | Done | Abandoned
- `/process-backlog` handles bidirectional sync with `KANBAN.md`
- MCP permissions are restricted to: find, add, delete (no direct complete)

## File Naming

- Content files: `YYYY-MM-DD-slug.md`
- Voice guides: `VOICE_<platform>.md`
- Templates: `TEMPLATE_*.md`

## Gitignore Behavior

The repo tracks structure (`.gitkeep` files) but excludes actual content: all drafts, published posts, personal reviews, client work, and `RESUME.md` are gitignored. Only templates and voice guides are versioned.

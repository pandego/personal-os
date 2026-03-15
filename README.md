# Personal OS

A blueprint for managing your life with AI-powered workflows. **This is meant to be customized**—fork it, rename folders, add domains, remove what you don't need. That's why it's called *Personal* OS.

## Domains

| Domain | Folder | Purpose |
|--------|--------|---------|
| **Personal OS** | `1-personal/` | Reviews, knowledge, data exports |
| **Business OS** | `2-business/` | Consulting business, clients, Upwork |
| **Content OS** | `3-content/` | Blog and LinkedIn content |

## Quick Start

Run the setup skill:

```bash
/get-started
```

This guides you through:
- **Voice configuration** — your writing style
- **Python environment** — uses `uv`
- **Todoist MCP** — optional, for task/idea sync

## Todoist Integration

By default, Personal OS syncs with Todoist for idea capture and task management.

**Manual setup** (if not using the wizard):

```bash
claude mcp add --transport http todoist https://ai.todoist.net/mcp
```

Then launch Claude, run `/mcp`, and authenticate with Todoist.

**Required**: Create a project called **"PersonalOS"** in Todoist with **board view** enabled. Use `/process-backlog` to sync with local `KANBAN.md`.

## Obsidian

Open the repo in Obsidian, as a Vault, and the [Kanban plugin](https://github.com/mgmeyers/obsidian-kanban) to start using it for kanban-style idea management. The `KANBAN.md` file syncs with your Todoist PersonalOS project every time you run `/process-backlog`.

### Locally ignoring tracked files (e.g., `KANBAN.md`)

If you want to keep a tracked file in the repo but ignore your local edits (e.g., personal tweaks to `KANBAN.md`), mark it skip-worktree locally:

```bash
git update-index --skip-worktree KANBAN.md
```

Status will now hide changes to that file. To resume tracking later:

```bash
git update-index --no-skip-worktree KANBAN.md
```

For a folder (e.g., `Perafolder`), use the same flag against the directory:

```bash
git update-index --skip-worktree Perafolder/
```

Re-enable tracking for the folder with:

```bash
git update-index --no-skip-worktree Perafolder/
```

## Tool-Agnostic Setup

This repo uses `.codex/` as the canonical runtime folder, with `.claude/` symlinked to it for compatibility.

If you want to integrate another runtime later, point it at the same canonical commands and skills instead of duplicating configuration.

For agent instructions, `AGENTS.md` and `CLAUDE.md` remain the project-level source of truth.

## License

MIT License - see LICENSE file for details

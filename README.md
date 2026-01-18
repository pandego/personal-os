# Personal OS

A blueprint for managing your life with AI-powered workflows. **This is meant to be customized**—fork it, rename folders, add domains, remove what you don't need. That's why it's called *Personal* OS.

## Domains

| Domain | Folder | Purpose |
|--------|--------|---------|
| **Content OS** | `1-content/` | Blog, LinkedIn, X, YouTube content |
| **Business OS** | `2-business/` | Consulting business, clients, Upwork |
| **Personal OS** | `3-personal/` | Reviews, knowledge, data exports |

## Quick Start

Run the setup skill:

```bash
/setup-repo
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

**Required**: Create a project called **"PersonalOS"** in Todoist with **board view** enabled. Use `/sync-todoist` to sync with local `KANBAN.md`.

## Obsidian

Open the repo in Obsidian, as a Vault, and the [Kanban plugin](https://github.com/mgmeyers/obsidian-kanban) to start using it for kanban-style idea management. The `KANBAN.md` file syncs with your Todoist PersonalOS project every time you run `/sync-todoist`.

## Tool-Agnostic Setup

This repo uses **symlinks** to remain agnostic to the agentic coding provider. The `.claude/` directory serves as the source of truth for commands, skills, and agent instructions.

To use with a different IDE (e.g., Windsurf):

```bash
# Symlink skills
mkdir -p .windsurf/skills
ln -s .claude/skills .windsurf/skills

# Symlink commands → workflows (must symlink contents, not directory)
mkdir -p .windsurf/workflows && cd .windsurf/workflows
ln -s ../../.claude/commands/* . && cd ../..
```

For agent instructions, `AGENTS.md` points to `CLAUDE.md`:

```markdown
# AGENTS.md
@CLAUDE.md
```

This allows switching between Claude Code, Windsurf, Cursor, or any other agentic coding tool without duplicating configuration.

## License

MIT License - see LICENSE file for details

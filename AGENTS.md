# AGENTS.md

This is the canonical instruction file for all agentic runtimes used in this repository.

## Runtime-Agnostic Contract

1. Read this file first.
2. Treat this file as source of truth for behavior, structure, and workflow.
3. Use runtime-specific folders only for runtime-specific wiring (commands, adapters, local settings), not for conflicting project rules.
4. If a runtime requires its own rule filename, that file should redirect to `AGENTS.md` whenever possible.

## Runtime Redirects

Each runtime has its own config filename convention. The root instruction file for each should redirect to `AGENTS.md`:

| Runtime | Root file | Redirect syntax | Runtime folder |
|---------|-----------|----------------|----------------|
| Claude Code | `CLAUDE.md` | `@AGENTS.md` | `.claude/` |
| Codex / GPT | `AGENTS.md` (direct) | — | `.codex/` |
| Gemini CLI | `AGENTS.md` | — | `.gemini/` |
| Cursor | `AGENTS.md` | — | `.cursor/` |
| Windsurf | `AGENTS.md` | — | `.agents/` |
| OpenCode | `AGENTS.md` | — | `.agents/` |
| Generic / multi-runtime | `AGENTS.md` (direct) | — | `.agents/` |

If a runtime does not support redirect syntax, keep a short local rule file that says: "Follow `AGENTS.md` in this repository as source of truth."

The `.agents/` folder is the runtime-agnostic default for skills, commands, and agents that should work across all runtimes.

## What This Is

Personal OS is an AI-powered personal knowledge and content management system organized into three domains:
- Content (`1-content/`): blog, LinkedIn, X, YouTube
- Business (`2-business/`): portfolio, clients, outbound
- Personal (`3-personal/`): reviews, knowledge

It integrates with Todoist for task capture and Obsidian for visual Kanban management.

## Getting Started

**Run `/prime` at the start of every session.** This bootstraps the agent with repo context and discovers all available skills.

## Core Skills

| Skill | Purpose |
|-------|---------|
| `setup-repo` | First-time setup (voice config, Python env, symlinks, Todoist MCP) |
| `process-backlog` | Sync `KANBAN.md` ↔ Todoist, clean up messy tasks |

Additional skills (content, business, utilities) are loaded dynamically per runtime. Run `/prime` or `/list-all-skills` to see them all.

## Python Environment

**CRITICAL: ALWAYS use `uv run` for Python execution. NEVER use `python` or `python3` directly.**

```bash
uv sync
uv run <script>
uv run python -c "..."
uv run pytest
```

## Architecture

```text
1-content/           # Content OS: platform-specific content workflows
2-business/          # Business OS: portfolio, clients, outbound
3-personal/          # Personal OS: reviews, knowledge (private)
.agents/             # Runtime-agnostic skills/commands/agents (shared across runtimes)
.claude/             # Claude Code-specific wiring
.codex/              # Codex/GPT-specific wiring
.cursor/             # Cursor-specific wiring (if used)
.windsurf/           # Windsurf-specific wiring (if used)
.opencode/           # OpenCode-specific wiring (if used)
```

## Runtime-Specific Folder Rules

- Keep shared logic and policy in repo docs (`AGENTS.md`, `README-*.md`, templates, guides), not locked into one runtime folder.
- Place runtime-agnostic skills and commands in `.agents/` so any runtime can consume them.
- Keep runtime-only artifacts (adapters, hooks, settings) in their runtime folder:
  - `.claude/` — commands, agents, skills, settings
  - `.codex/` — skills, agents
  - `.cursor/` — agents
  - `.windsurf/` — skills, workflows, rules
  - `.opencode/` — skills, commands, agents
- If duplicate instructions exist across runtimes, consolidate them into `.agents/` or a shared file and reference it from each runtime folder.

### Folder Organization

Rule: Flat = public, Subfolder = private

- Flat files (example: `commands/draft-blog.md`) can be committed.
- Domain-specific/private subfolders can stay gitignored.

This keeps reusable structure public while allowing private voice workflows.

## Creating Skills

Rule: ALWAYS start from template.

Use `_system/templates/TEMPLATE_SKILL.md` as base:
1. Copy template to target skills folder (prefer `.agents/skills/<skill-name>/SKILL.md` for shared skills, or `.claude/skills/` / `.codex/skills/` for runtime-specific ones).
2. Fill Purpose, Variables, Instructions, Workflow, Cookbook.
3. Keep core logic runtime-agnostic. Add runtime-specific wiring only where needed.

## Skills Architecture (Symlinks)

Many skills in `.claude/skills/` are symbolic links pointing to external submodules or private repos.

Source locations:
- `_external/anthropic-skills/skills/` — docx, pdf, pptx, xlsx, brand-guidelines, skill-creator
- `_external/disler-fork-terminal-skill/.claude/skills/` — fork-terminal
- `_external/pandego-parallel-thread-skill/.claude/skills/` — pthd
- `_internal/private-skills/.claude/skills/` — blog-content, linkedin-content, brand-guidelines-datavengers, datavengers-proposal

Local skills (not symlinked): `process-backlog`, `review`, `setup-repo`

Setup: run `uv run setup-symlinks` after cloning (or run `/setup-repo`). Script is idempotent.

Editing symlinked skills: changes are applied in the source repo; use `git status` there to track/commit.

## Voice System

Before creating content, read:
1. `VOICE.md` (universal voice and identity)
2. Platform guide (example: `1-content/01-blog/VOICE_blog.md`)

Core patterns: authority via specifics, no corporate jargon, statement hooks, practitioner focus.

## Todoist Integration

- Requires Todoist project `PersonalOS` in board view
- Sections: Backlog | Ready | In Progress | Done | Abandoned
- `/process-backlog` handles bidirectional sync with `KANBAN.md`
- MCP permissions are intentionally limited (find/add/delete, no direct complete)

## File Naming

- Content files: `YYYY-MM-DD-slug.md`
- Voice guides: `VOICE_<platform>.md`
- Templates: `TEMPLATE_*.md`

## Gitignore Behavior

The repo tracks structure (`.gitkeep`) but excludes most real content:
- drafts/published content
- personal reviews
- client work
- `RESUME.md`

Templates and voice guides are versioned.

## Sub-Folder Documentation

Each domain folder has its own `README-<folder>.md` with domain-specific instructions:
- `1-content/README-content.md` — Content workflows, voice system, platform structure
- `2-business/README-business.md` — Business domain
- `3-personal/README-personal.md` — Personal reviews and knowledge
- `_system/README-system.md` — Scripts, templates, MCP servers
- `_internal/README-internal.md` — Internal resources

## Reference

Claude-specific configuration patterns (skills, agents, hooks, `CLAUDE.md` structure):
- `_system/docs/claude-code_best-practices.md`

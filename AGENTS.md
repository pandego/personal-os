# AGENTS.md

This is the canonical instruction file for all agentic runtimes used in this repository.

## Runtime-Agnostic Contract

1. Read this file first.
2. Treat this file as source of truth for behavior, structure, and workflow.
3. Use runtime-specific folders only for runtime-specific wiring, not for conflicting project rules.
4. If a runtime requires its own rule filename, that file should redirect to `AGENTS.md` whenever possible.

## Runtime Redirects

Each runtime has its own config filename convention. The root instruction file for each should redirect to `AGENTS.md`:

| Runtime | Root file | Redirect syntax | Runtime folder |
|---------|-----------|----------------|----------------|
| Claude Code | `CLAUDE.md` | `@AGENTS.md` | `.claude/` |
| Codex / GPT | `AGENTS.md` (direct) | - | `.codex/` |
| Gemini CLI | `AGENTS.md` | - | `.gemini/` |
| Cursor | `AGENTS.md` | - | `.cursor/` |
| Windsurf | `AGENTS.md` | - | `.agents/` |
| OpenCode | `AGENTS.md` | - | `.agents/` |
| Generic / multi-runtime | `AGENTS.md` (direct) | - | `.agents/` |

If a runtime does not support redirect syntax, keep a short local rule file that says: "Follow `AGENTS.md` in this repository as source of truth."

## What This Is

Personal OS is a personal AI workspace organized into three default domains:
- Personal (`1-personal/`) - reviews, knowledge, and private reference material
- Business (`2-business/`) - portfolio, outreach, and client-facing work
- Content (`3-content/`) - blog and LinkedIn workflows

The structure is meant to be adapted, not obeyed blindly.

## Getting Started

Use `/get-started` to shape the system around the user before pushing advanced tooling or integrations.

The first-run experience should help the user:
- clarify intent
- define how the assistant should sound
- decide whether to prepare optional Python tooling
- generate a tailored `MY_OS_BLUEPRINT.md`

Do not force advanced integrations as part of the core first-run flow.

## Available Skills

These are the default local skills available in this Personal OS, in recommended discovery order:

| Skill | What it does |
|-------|---------------|
| `get-started` | first-run guided onboarding that helps the user clarify intent, set voice, optionally prepare Python tooling, and generate a tailored `MY_OS_BLUEPRINT.md` |
| `review-week` | weekly reflection workflow using the local `review` skill and its week review path |
| `review-year` | yearly reflection workflow using the local `review` skill and its year review path |
| `skill-creator` | create, improve, evaluate, and refine skills so the Personal OS can grow over time |
| `mcp-builder` | design and build MCP servers and integrations when the user wants to extend the system with external capabilities |

`get-started` should be treated as the main entrypoint.

## Python Environment

Use `uv` for Python-related commands.

```bash
uv sync
uv run <script>
uv run python -c "..."
uv run pytest
```

Python setup is important, but should be presented in plain language to non-technical users.

## Architecture

```text
1-personal/         # private reflection, knowledge, personal reference
2-business/         # business systems, portfolio, outreach, clients
3-content/          # blog and LinkedIn workflows
.agents/            # runtime-agnostic skills/commands/agents (shared across runtimes)
.claude/            # Claude Code compatibility link/wiring
.codex/             # canonical runtime folder
.cursor/            # Cursor-specific wiring (if used)
.windsurf/          # Windsurf-specific wiring (if used)
.opencode/          # OpenCode-specific wiring (if used)
```

## Runtime-Specific Folder Rules

- Keep shared logic and policy in repo docs (`AGENTS.md`, `README-*.md`, templates, guides), not locked into one runtime folder.
- Keep runtime-only artifacts in their runtime folder.
- If duplicate instructions exist across runtimes, consolidate them into shared docs where possible.

## Skills Architecture

The canonical runtime folder is `.codex/`, with `.claude/` symlinked to it for compatibility.

The repo intentionally keeps a minimal local skill set:
- `review`
- `get-started`

## Voice System

Before creating content, read:
1. `VOICE.md`
2. the relevant platform voice file if one exists

Voice guidance should stay plain-language and practical.

## Optional Enhancements

These are later-stage enhancements, not first-run requirements:
- advanced automations
- extra custom skills
- third-party integrations

## File Naming

- Content files: `YYYY-MM-DD-slug.md`
- Voice guides: `VOICE_<platform>.md`
- Templates: `TEMPLATE_*.md`

## Gitignore Behavior

The repo tracks structure and documentation, while ignoring most genuinely private or generated working content.

## Sub-Folder Documentation

Each domain folder has its own `README-<folder>.md` with domain-specific instructions:
- `3-content/README-content.md` - Content workflows and voice system
- `2-business/README-business.md` - Business domain guidance
- `1-personal/README-personal.md` - Personal reviews and knowledge
- `_system/README-system.md` - Scripts, templates, and supporting tooling

## Reference

Claude-specific configuration patterns (skills, agents, hooks, `CLAUDE.md` structure):
- `_system/docs/claude-code_best-practices.md`

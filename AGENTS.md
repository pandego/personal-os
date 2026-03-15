# AGENTS.md

This is the canonical instruction file for all agentic runtimes used in this repository.

## Runtime-Agnostic Contract

1. Read this file first.
2. Treat this file as the source of truth for agent behavior and repository workflow.
3. Use runtime-specific folders only for runtime-specific wiring, not for conflicting project rules.
4. If a runtime requires its own rule filename, that file should redirect to `AGENTS.md` whenever possible.
5. Keep the system adaptable. Suggest structural changes when helpful, but do not reorganize the user's workspace without clear reason.

## Runtime Redirects

Each runtime has its own config filename convention. The root instruction file for each should redirect to `AGENTS.md`:

| Runtime | Root file | Redirect syntax | Runtime folder |
|---------|-----------|----------------|----------------|
| Claude Code | `CLAUDE.md` | `@AGENTS.md` | `.claude/` |
| Codex / GPT | `AGENTS.md` (direct) | - | `.codex/` |
| Other runtimes | runtime-specific | redirect when supported | optional |

If a runtime does not support redirect syntax, keep a short local rule file that says: "Follow `AGENTS.md` in this repository as source of truth."

## What This Is

Personal OS is a personal AI workspace organized into three default domains:
- Personal (`1-personal/`) - reviews, knowledge, and private reference material
- Business (`2-business/`) - portfolio, outreach, and client-facing work
- Content (`3-content/`) - blog and LinkedIn workflows

The structure is meant to be adapted, not obeyed blindly.

## Getting Started

Use `/get-started` before pushing advanced tooling, automations, or integrations.

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
| `get-started` | first-run guided onboarding that helps the user clarify intent, personalize voice, optionally prepare Python tooling, and generate a tailored `MY_OS_BLUEPRINT.md` |
| `review` | reflection skill with two entry paths: `review-week` for weekly reviews and `review-year` for yearly reviews |
| `draft-content` | draft content through one shared entrypoint that asks for the platform, applies the repo voice system, and can refresh platform voice guidance from examples |
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
.claude/            # Claude Code compatibility link to `.codex/`
.codex/             # canonical runtime folder
_system/            # scripts, templates, and supporting tooling
```

## Runtime-Specific Folder Rules

- Keep shared logic and policy in repo docs (`AGENTS.md`, `README-*.md`, templates, guides), not locked into one runtime folder.
- Keep runtime-only artifacts in their runtime folder.
- If duplicate instructions exist across runtimes, consolidate them into shared docs where possible.
- Prefer a single canonical runtime folder over duplicated parallel setups.

## Skills Architecture

The canonical runtime folder is `.codex/`, with `.claude/` symlinked to it for compatibility.

The current local skills are:
- `get-started`
- `review`
- `draft-content`
- `skill-creator`
- `mcp-builder`

## Voice System

Before creating content, read:
1. `VOICE.md`
2. the relevant platform voice file if it exists
3. relevant examples from `3-content/_voice-examples/<platform>/` when useful

`VOICE.md` is the default voice contract for this repo.

- If `VOICE.md` still contains the onboarding note, treat it as a temporary default voice and recommend running `/get-started`.
- After `/get-started`, `VOICE.md` should be rewritten as the user's personalized voice guide.
- Platform voice files should be refined from the matching `_voice-examples` folder.

Voice guidance should stay plain-language and practical.

## Default Writing Rules

Unless a personalized voice guide says otherwise:
- avoid em dashes
- avoid fake-contrast patterns like "it's not X, it's Y"
- avoid stacked negation patterns like "it's not X, not Y, not Z, it's..."
- avoid scolding or preachy phrasing like "stop doing this"
- avoid generic ChatGPT-style rhetoric and inflated summaries
- prefer plain, concrete, human language
- keep writing useful before trying to sound clever

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

Each domain folder has its own `README_<name>.md` with short, user-readable instructions:
- `3-content/README_content.md` - content workflows and voice system
- `3-content/01-blog/README_blog.md` - blog workflow
- `3-content/02-linkedin/README_linkedin.md` - LinkedIn workflow
- `3-content/_voice-examples/README_voice-examples.md` - voice example usage
- `2-business/README_business.md` - business domain guidance
- `1-personal/README_personal.md` - personal reviews and knowledge
- `_system/README-system.md` - scripts, templates, and supporting tooling

## Reference

Claude-specific configuration patterns (skills, agents, hooks, `CLAUDE.md` structure):
- `_system/docs/claude-code_best-practices.md`

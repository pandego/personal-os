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

Shared skills live in `.agents/skills/`. Runtime folders should point to that shared skill folder instead of keeping separate copies.

## Always-loaded context

Read these three files at the start of every session, in this order:

@memories/USER.md
@memories/MEMORY.md
@SOUL.md

| File | Scope |
|---|---|
| `memories/USER.md` | About the user. Their identity, story, what they want this Personal OS for, tone they prefer. |
| `memories/MEMORY.md` | About the user's setup. Repo layout, tooling, conventions, workflows, environment notes. |
| `SOUL.md` | About you, the assistant. Standing character, defaults, refusals, posture. |

`VOICE.md` is loaded only by `/draft-content` when drafting or updating content. It is not part of the always-loaded context.

### Placeholder detection

If `memories/USER.md` or `memories/MEMORY.md` is missing, empty, or starts with `<!-- placeholder: get-started -->`, say once: "`memories/USER.md` (or `MEMORY.md`) is unpopulated. Run `/get-started` to personalize." Then proceed with the user's request. Do not block.

If `VOICE.md` is missing or starts with `<!-- placeholder: draft-content update-voice -->`, only mention this when the user is drafting content, then continue with whatever signal you have.

Do not fabricate content for these files. Only `/get-started` populates `USER.md` and `MEMORY.md`. Only `/draft-content` (update-voice cookbook) populates `VOICE.md`. `SOUL.md` ships with a default character (JARVIS-like). The user edits it directly if they want a different one.

## What This Is

Personal OS is a personal AI workspace organized into three default domains:
- Personal (`1-personal/`) - reviews, knowledge, and private reference material
- Business (`2-business/`) - portfolio, outreach, and client-facing work
- Content (`3-content/`) - blog and LinkedIn workflows

The structure is meant to be adapted, not obeyed blindly.

## Getting Started

Use `/get-started` before pushing advanced tooling, automations, or integrations.

`/get-started` produces exactly two files: `memories/USER.md` and `memories/MEMORY.md`. It also confirms folder structure with explicit yes/no per change. It does not create blueprint files, edit `VOICE.md` or `SOUL.md`, or touch Python.

Do not force advanced integrations as part of the core first-run flow.

## Available Skills

These are the default local skills available in this Personal OS, in recommended discovery order:

| Skill | What it does |
|-------|---------------|
| `get-started` | one-time onboarding. Creates `memories/USER.md` and `memories/MEMORY.md`, confirms folder structure with explicit per-change yes/no |
| `review` | reflection skill with two entry paths: `review-week` for weekly reviews and `review-year` for yearly reviews |
| `draft-content` | three cookbooks: `write-blog`, `write-linkedin`, `update-voice` (rewrites root `VOICE.md` from `3-content/_voice-samples/`) |
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
Do not make Python setup part of the default `/get-started` flow.

## Architecture

```text
1-personal/         # private reflection, knowledge, personal reference
2-business/         # business systems, portfolio, outreach, clients
3-content/          # blog and LinkedIn workflows; flat _voice-samples/
memories/           # USER.md (the human) + MEMORY.md (the setup)
SOUL.md             # the assistant (root)
VOICE.md            # the writing voice (root, owned by /draft-content)
.claude/            # Claude Code runtime wiring (skills -> .agents/skills)
.codex/             # Codex runtime wiring (skills -> .agents/skills)
.agents/            # shared local skills
_system/            # scripts, templates, and supporting tooling
```

## Runtime-Specific Folder Rules

- Keep shared logic and policy in repo docs (`AGENTS.md`, `README-*.md`, templates, guides), not locked into one runtime folder.
- Keep runtime-only artifacts in their runtime folder.
- If duplicate instructions exist across runtimes, consolidate them into shared docs where possible.
- Prefer one shared skills folder over duplicated parallel setups.

## Skills Architecture

The shared skills folder is `.agents/skills/`.
Runtime-specific skill folders should point there, for example `.codex/skills` and `.claude/skills`.

The current local skills are:
- `get-started`
- `review`
- `draft-content`
- `skill-creator`
- `mcp-builder`

## Voice System

The three always-loaded files (see "Always-loaded context") plus `VOICE.md` (loaded only by `/draft-content`) cover voice and personalization. There are no per-platform voice files.

Order of precedence when drafting content:
1. `memories/USER.md` directness and avoid preferences
2. `VOICE.md` patterns at repo root, if populated
3. explicit user instructions in the current request

Voice samples live flat in `3-content/_voice-samples/`. There are no per-platform subfolders. Anything written in the user's voice can go there: emails, blog posts, LinkedIn posts, notes.

`VOICE.md` is owned by `/draft-content` (update-voice cookbook). Do not edit it from any other skill.

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
- Templates: `TEMPLATE_*.md`

## Gitignore Behavior

The repo tracks structure and documentation, while ignoring most genuinely private or generated working content.

## Sub-Folder Documentation

Each domain folder has its own `README_<name>.md` with short, user-readable instructions:
- `3-content/README_content.md` - content workflows and voice system
- `3-content/01-blog/README_blog.md` - blog workflow
- `3-content/02-linkedin/README_linkedin.md` - LinkedIn workflow
- `3-content/_voice-samples/README_voice-samples.md` - voice sample usage
- `2-business/README_business.md` - business domain guidance
- `2-business/02-outbound/README_outbound.md` - outbound workflow
- `2-business/03-clients/_template/README_client-template.md` - client template guide
- `1-personal/README_personal.md` - personal reviews and knowledge
- `_system/README_system.md` - scripts, templates, and supporting tooling

## Reference

Claude-specific configuration patterns (skills, agents, hooks, `CLAUDE.md` structure):
- `_system/docs/claude-code_best-practices.md`

# MEMORY

Operational memory for you, the assistant. Stable facts about the user's setup, conventions, and workflows.

## Repo
- Root: {REPO_ROOT}
- Domains the user kept: {DOMAINS}
- Domains the user removed: {REMOVED_DOMAINS}

## Tooling
- Python: the user runs scripts via `uv run`. Use `uv` for any Python work.
- Runtime wiring: shared skills live in `.agents/skills/`; runtime-specific skill folders should point or redirect there.

## Conventions
- Content drafts use the filename pattern `YYYY-MM-DD-slug.md`.
- Voice samples live flat in `3-content/_voice-samples/` (no platform subfolders).
- Persistent context files:
  - `memories/USER.md` — about the user
  - `memories/MEMORY.md` — about the user's setup (this file)
  - `AGENTS.md` — about the assistant (character + project rules)
  - `VOICE.md` — patterns from the user's real writing

## Workflows
- Onboarding: `/get-started`
- Reviews: `/review` (week or year)
- Drafting: `/draft-content` (write blog, write LinkedIn, update voice)

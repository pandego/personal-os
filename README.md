# Personal OS

A starter folder for building a personal AI operating system around your real life, work, and priorities.

This repo is meant to be shaped over time. You can rename folders, remove areas you do not need, keep only what is useful, and let your assistant work inside one clear workspace that reflects how you actually organize things.

## Domains

| Domain | Folder | Purpose |
|--------|--------|---------|
| **Personal OS** | `1-personal/` | Reviews, knowledge, private reflection, and personal reference material |
| **Business OS** | `2-business/` | Portfolio, outreach, client-facing work, and business systems |
| **Content OS** | `3-content/` | Blog and LinkedIn writing workflows, plus platform voice samples |

## Quick Start

Run:

```bash
/get-started
```

This guided flow:
- asks four short questions
- writes `memories/USER.md` (who you are) and `memories/MEMORY.md` (your setup)
- confirms folder structure with explicit yes/no for any change

One more file is already at the repo root:
- `VOICE.md` - your writing voice. Populate later by dropping samples into `3-content/_voice-samples/` and running `/draft-content` (update voice)

The assistant's character lives in `AGENTS.md` at repo root (alongside the project rules). Edit it directly if you want a different one.

## What this folder is for

Think of this repo as the home folder for your assistant.

The better this folder reflects your real life and work, the more useful the assistant becomes.

You do **not** need to use every folder, every workflow, or every feature. Start simple. Shape the system around what you actually need.

## How to approach it

A good first version usually looks like this:
1. decide what you want help with first
2. keep only the domains that matter right now
3. add real material slowly
4. improve structure only when it helps you

Avoid turning this into a giant life-admin machine on day one.

## Optional later enhancements

Once the basics feel useful, you can later explore:
- `review` for weekly or yearly reflection
- `draft-content` for blog and LinkedIn drafting
- extra skills and automations

## Tool-Agnostic Setup

This repo keeps shared skills in `.agents/skills/`.
Runtime-specific folders such as `.codex/skills` and `.claude/skills` should point to that shared folder.

If you want to integrate another runtime later, point it at the same shared commands and skills instead of duplicating configuration.

For agent instructions, `AGENTS.md` and `CLAUDE.md` remain the project-level source of truth.

## Obsidian

You can open the repo in Obsidian as a vault if that helps you browse and edit the folder more comfortably.

## License

MIT License - see LICENSE file for details

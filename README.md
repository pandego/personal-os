# Personal OS

A starter folder for building a personal AI operating system around your real life, work, and priorities.

This repo is meant to be shaped over time. You can rename folders, remove areas you do not need, keep only what is useful, and let your assistant work inside one clear workspace that reflects how you actually organize things.

## Domains

| Domain | Folder | Purpose |
|--------|--------|---------|
| **Personal OS** | `1-personal/` | Reviews, knowledge, private reflection, and personal reference material |
| **Business OS** | `2-business/` | Portfolio, outreach, client-facing work, and business systems |
| **Content OS** | `3-content/` | Blog and LinkedIn writing workflows |

## Quick Start

Run:

```bash
/get-started
```

This guided flow helps you:
- clarify what you want this Personal OS to help with
- create a `VOICE.md` for how your assistant should sound
- optionally prepare the Python tooling used by some skills
- generate a `MY_OS_BLUEPRINT.md` tailored to your needs

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
- `/review` for weekly or yearly reflection
- extra skills and automations
- deeper AI workflows inside each domain

## Tool-Agnostic Setup

This repo uses `.codex/` as the canonical runtime folder, with `.claude/` symlinked to it for compatibility.

If you want to integrate another runtime later, point it at the same canonical commands and skills instead of duplicating configuration.

For agent instructions, `AGENTS.md` and `CLAUDE.md` remain the project-level source of truth.

## Obsidian

You can open the repo in Obsidian as a vault if that helps you browse and edit the folder more comfortably.

## License

MIT License - see LICENSE file for details

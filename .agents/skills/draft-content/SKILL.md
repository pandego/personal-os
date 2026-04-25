---
name: draft-content
description: Three cookbooks for content work in Personal OS. Use when the user wants to (a) write a blog post, (b) write a LinkedIn post, or (c) update root `VOICE.md` from samples in `3-content/_voice-samples/`. Routes to one cookbook based on the user's intent.
---

# Draft Content

This skill has exactly three cookbooks. Pick one. Do not mix them.

| Cookbook | When to use |
|---|---|
| `cookbooks/write-blog.md` | User wants to draft or revise a blog post |
| `cookbooks/write-linkedin.md` | User wants to draft or revise a LinkedIn post |
| `cookbooks/update-voice.md` | User wants to populate or refresh root `VOICE.md` from samples |

## Routing

If the user's intent is clear from their request, go straight to the matching cookbook and follow it.

If the intent is ambiguous, use AskUserQuestion ONCE with this question:

- Header: "What do you want to do?"
  Type: single-select.
  Options: `Write a blog post`, `Write a LinkedIn post`, `Update VOICE.md from samples`.

Do not ask more than one routing question.

## Always read first

Before any cookbook:

1. Read `memories/USER.md`. Use the directness and avoid preferences.
2. Read `VOICE.md` at repo root. Use its patterns when drafting.

If `VOICE.md` contains the marker `<!-- placeholder: draft-content update-voice -->` and the user picked a writing cookbook (blog or LinkedIn), mention this once in the chat: "VOICE.md is still a placeholder. I'll draft using only USER.md preferences. Run /draft-content (update voice) once you have samples." Then continue. Do not block.

## Output rules

- Drafts go in the platform's `01-drafts/` folder. Filenames: `YYYY-MM-DD-slug.md`.
- One strong draft beats several hedged variants. Only produce variants if the user asks.
- Do not invent quotes, sources, or numbers.
- Apply repo voice rules: no em dashes, no "it's not X, it's Y", no stacked negation, no scolding, no inflated summaries.

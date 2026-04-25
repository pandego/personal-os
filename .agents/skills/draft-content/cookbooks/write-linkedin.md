# Write LinkedIn cookbook

Goal: produce a LinkedIn draft in `3-content/02-linkedin/01-drafts/YYYY-MM-DD-slug.md`.

## Pre-checks

1. If `3-content/02-linkedin/01-drafts/` does not exist, tell the user the LinkedIn folder is not set up and stop.
2. Confirm `memories/USER.md` and `VOICE.md` were already read by the parent SKILL.

## Step 1: Get the minimum input

Ask only what is missing. Use ONE AskUserQuestion call with up to three questions:

1. Header: "What is the post about?" Type: free text.
2. Header: "What is the framing?" Type: single-select.
   Options: `educate`, `convince`, `inspire`, `entertain`.
3. Header: "What perspective?" Type: single-select.
   Options: `personal`, `expert`, `general`.

Skip any question the user already answered in their request.

## Step 2: Draft the post

Write to `3-content/02-linkedin/01-drafts/YYYY-MM-DD-slug.md` using today's date and a short kebab-case slug.

Use this structure:

```md
---
title: "Post Title"
description: "Post description"
platform: linkedin
category: educate | convince | inspire | entertain
perspective: personal | expert | general
visual: none | image | carousel | video
---

[HOOK: one clear line that earns attention]

[STORY OR CONTEXT: 2 to 4 short paragraphs]

[VALUE: specific takeaways, bullets, or examples]
- {Specific insight 1}
- {Specific insight 2}
- {Specific insight 3}

[CTA: question, invitation, or next step]

<!-- IMAGE | VIDEO | CAROUSEL: [description if a visual would improve the post] -->
```

## Quality rules

- Tight and readable. Trim filler aggressively.
- One strong post over four weak variants unless the user asks for options.
- Emojis only if they help tone. Sparingly.
- Concrete, not hypey.
- Apply patterns from `VOICE.md` if it is populated. Otherwise use plain, concrete language and the `USER.md` directness setting.

---
name: draft-content
description: Draft content for Personal OS through one shared entrypoint. Use when the user wants to write or draft content for blog or LinkedIn, adapt a draft to one of those platforms, or work from platform voice samples. Ask which platform if it is not already clear, then follow the matching cookbook and apply `VOICE.md` plus the relevant sample set.
---

# Draft Content

Use one shared flow for content creation and voice-aware writing.

## Modes

This skill supports two modes:
- **draft mode** - create or improve a blog post or LinkedIn post
- **voice mode** - infer platform voice from the samples in the matching `_voice-samples/` folder

If the user intent is not explicit, ask one short clarifying question.

## Core workflow

1. Ask which platform to work on if it is not already clear.
   - supported platforms: `blog`, `linkedin`
2. Read `VOICE.md` first.
3. Read the matching platform cookbook:
   - blog -> `references/blog.md`
   - linkedin -> `references/linkedin.md`
4. Read relevant samples from:
   - blog -> `3-content/_voice-samples/blog/`
   - linkedin -> `3-content/_voice-samples/linkedin/`
5. Decide whether the task is draft mode or voice mode.
6. If the task is draft mode, ask only for the minimum missing details needed to produce a strong draft.
7. If the task is draft mode, create or revise the content in the correct `01-drafts/` folder using `YYYY-MM-DD-slug.md`.
8. If the task is voice mode, infer the platform voice from repeated patterns in the samples and use that guidance in the output.
9. Keep the output practical, specific, and aligned with the voice guidance.

## Question policy

Ask short follow-up questions only when they materially improve the result.

Good examples:
- What platform is this for: blog or LinkedIn?
- What is the main idea or claim?
- Who is this for?
- Do you want this to teach, persuade, reflect, or announce something?

Do not interrogate the user with a giant questionnaire.

## Voice samples

Use `_voice-samples` as the flexible source of platform voice material.

- Treat both personal samples and swipe examples as valid inputs.
- Focus on repeated patterns, not one-off quirks.
- Ignore examples that obviously conflict with the repo's core voice rules unless the user explicitly wants that style.
- When working from platform samples, capture practical guidance another assistant could actually apply.

## Voice rules

Always apply the repo voice system in this order:
1. `VOICE.md`
2. relevant platform samples
3. explicit user instructions in the current request

If `VOICE.md` still contains the onboarding note, treat it as a temporary default voice and gently recommend `/get-started`, but still complete the task.

## Output rules

- Put drafts in the correct platform draft folder.
- Use realistic titles and filenames.
- Avoid generic filler and fake authority.
- Prefer one strong draft over many weak variants unless the user asks for options.
- When working from platform samples, keep the applied guidance short, concrete, and easy to follow.

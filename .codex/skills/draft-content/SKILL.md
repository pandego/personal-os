---
name: draft-content
description: Draft content for Personal OS through one shared entrypoint. Use when the user wants to write or draft content for blog or LinkedIn, adapt a draft to one of those platforms, or refresh platform voice guidance from examples. Ask which platform if it is not already clear, then follow the matching cookbook and apply `VOICE.md` plus any platform voice file.
---

# Draft Content

Use one shared flow for content creation and voice-aware writing.

## Modes

This skill supports two modes:
- **draft mode** - create or improve a blog post or LinkedIn post
- **voice mode** - refresh `VOICE_blog.md` or `VOICE_linkedin.md` from example files

If the user intent is not explicit, ask one short clarifying question.

## Core workflow

1. Ask which platform to work on if it is not already clear.
   - supported platforms: `blog`, `linkedin`
2. Read `VOICE.md` first.
3. Read the matching platform cookbook:
   - blog -> `references/blog.md`
   - linkedin -> `references/linkedin.md`
4. Read the matching platform voice file if it exists:
   - blog -> `3-content/01-blog/VOICE_blog.md`
   - linkedin -> `3-content/02-linkedin/VOICE_linkedin.md`
5. Read relevant examples from:
   - blog -> `3-content/_voice-examples/blog/`
   - linkedin -> `3-content/_voice-examples/linkedin/`
6. Decide whether the task is draft mode or voice mode.
7. If the task is draft mode, ask only for the minimum missing details needed to produce a strong draft.
8. If the task is draft mode, create or revise the content in the correct `01-drafts/` folder using `YYYY-MM-DD-slug.md`.
9. If the task is voice mode, update or create the platform voice file based on repeated patterns from the examples.
10. Keep the output practical, specific, and aligned with the voice guidance.

## Question policy

Ask short follow-up questions only when they materially improve the result.

Good examples:
- What platform is this for: blog or LinkedIn?
- What is the main idea or claim?
- Who is this for?
- Do you want this to teach, persuade, reflect, or announce something?

Do not interrogate the user with a giant questionnaire.

## Voice examples

Use `_voice-examples` as the flexible source of platform voice material.

- Treat both personal samples and swipe examples as valid inputs.
- Focus on repeated patterns, not one-off quirks.
- Ignore examples that obviously conflict with the repo's core voice rules unless the user explicitly wants that style.
- When updating a platform voice guide, capture practical rules another assistant can actually apply.

## Voice rules

Always apply the repo voice system in this order:
1. `VOICE.md`
2. platform voice file if present
3. explicit user instructions in the current request

If `VOICE.md` still contains the onboarding note, treat it as a temporary default voice and gently recommend `/get-started`, but still complete the task.

## Output rules

- Put drafts in the correct platform draft folder.
- Use realistic titles and filenames.
- Avoid generic filler and fake authority.
- Prefer one strong draft over many weak variants unless the user asks for options.
- When updating a voice file, keep it short, concrete, and easy to apply.

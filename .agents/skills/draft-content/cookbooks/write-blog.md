# Write Blog cookbook

Goal: produce a blog draft in `3-content/01-blog/01-drafts/YYYY-MM-DD-slug.md`.

## Pre-checks

1. If `3-content/01-blog/01-drafts/` does not exist, tell the user the blog folder is not set up and stop.
2. Confirm `memories/USER.md` and `VOICE.md` were already read by the parent SKILL.

## Step 1: Get the minimum input

Ask only what is missing. Use ONE AskUserQuestion call with up to three questions:

1. Header: "What is the main idea or claim?" Type: free text.
2. Header: "Who is this for?" Type: free text.
3. Header: "What kind of post?" Type: single-select.
   Options: `tutorial`, `explainer`, `deep-dive`, `case-study`.

Skip any question the user already answered in their request.

## Step 2: Draft the post

Write to `3-content/01-blog/01-drafts/YYYY-MM-DD-slug.md` using today's date and a short kebab-case slug derived from the main idea.

Use this structure:

```md
---
title: "Blog Title"
description: "Blog description"
platform: blog
category: tutorial | explainer | deep-dive | case-study
---

# {Title}

## {Subtitle}

<!-- COVER IMAGE: [Description of a banner or cover image that works standalone] -->

[Introduction: 2 to 3 paragraphs setting up the context and why this matters]

---

## {Section 1 Title}

[Content with h3 subsections as needed]

### {Subsection}

[Text, bullet points, explanations]

<!-- IMAGE: [Description of relevant image if needed] -->

## {Section 2 Title}

[Content continues]

### {Subsection}

[Text, bullet points, explanations]

## {Wrap-up Title}

[Closing thoughts, summary, or call to action]
```

## Quality rules

- Open with the problem, tension, or motivation. No empty intros.
- Be specific and opinionated when the evidence supports it.
- If code is included, keep it accurate and runnable.
- Cover failure modes or tradeoffs when relevant.
- Apply patterns from `VOICE.md` if it is populated. Otherwise use plain, concrete language and the `USER.md` directness setting.

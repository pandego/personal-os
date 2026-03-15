# Blog cookbook

## Output location

Write blog drafts to:
- `3-content/01-blog/01-drafts/YYYY-MM-DD-slug.md`

Voice examples for this platform live in:
- `3-content/_voice-examples/blog/`

Platform voice guide:
- `3-content/01-blog/VOICE_blog.md`

## Blog modes

Choose or confirm the best fit:
- `tutorial` - step-by-step how to do something
- `explainer` - explain a concept clearly
- `deep-dive` - go deep on a topic with more nuance
- `case-study` - show what was done, why, and what happened

If the mode is unclear, ask one short question.

## Draft template

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

[Introduction - 2 to 3 paragraphs setting up the context and why this matters]

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

<!-- IMAGE: [Description of relevant image if needed] -->

---

## {Wrap-up Title}

[Closing thoughts, summary, or call to action]
```

## Voice mode

When refreshing `VOICE_blog.md`:
- read examples from `3-content/_voice-examples/blog/`
- focus on repeated opening, structure, explanation, and closing patterns
- keep the guide practical instead of literary
- write rules that another assistant could actually follow while drafting

## Quality rules

- Start with the problem, tension, or motivation.
- Be specific and opinionated when the evidence supports it.
- If code is included, keep it accurate and runnable.
- Cover failure modes or tradeoffs when relevant.
- Avoid empty intros and generic conclusions.

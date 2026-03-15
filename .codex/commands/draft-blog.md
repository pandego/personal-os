---
description: Create a new blog post draft
allowed-tools: Read, Write, AskUserQuestion
---

# Create Blog Draft

Create a new blog post draft in `1-content/01-blog/01-drafts/`.

## Topic

$ARGUMENTS

## Steps

1. **Determine blog type** based on topic:
   - **tutorial**: "How to X", step-by-step guides
   - **explainer**: "What is X", concept explanations
   - **deep-dive**: Comprehensive explorations
   - **case-study**: "How I built X", results-focused

2. **Read voice file**: `1-content/01-blog/VOICE_blog.md` (if exists)

3. **Create file**: `1-content/01-blog/01-drafts/YYYY-MM-DD-<slug>.md`
   - Use today's date
   - Generate slug from topic: lowercase, dashes, no special chars

## Type Selection

If the type isn't obvious from the topic, ask the user:
- **Tutorial**: Step-by-step how-to
- **Explainer**: Concept/theory explanation
- **Deep-dive**: Comprehensive exploration
- **Case-study**: Real project with results

## Draft Template

```markdown
---
title: "Blog Title"
description: "Blog description"
platform: blog
category: tutorial | explainer | deep-dive | case-study
---

# {Title}

## {Subtitle}

<!-- COVER IMAGE: [Description of a visually appealing banner/cover image that works standalone] -->

[Introduction - 2-3 paragraphs setting up the context and why this matters]

---

## {Section 1 Title}

[Content with h3 subsections as needed]

### {Subsection}

[Text, bullet points, explanations]

<!-- IMAGE: [Description of relevant image if needed] -->

## {Section 2 Title}

[Content continues...]

### {Subsection}

[Text, bullet points, explanations]

<!-- IMAGE: [Description of relevant image if needed] -->

---

## {Wrap-up Title}

[Closing thoughts, summary, or call to action - can include bullet points]

---

> *Unless otherwise noted, all images are by the author.*
> [Subscribe!](https://medium.com/<author>)
```

## Instructions

- Apply VOICE_blog.md patterns if available
- Start with the problem, not the solution
- If applicable, include code examples with expected output
- Cover failure modes, not just happy paths
- Be specific and opinionated

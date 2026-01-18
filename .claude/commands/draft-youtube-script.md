---
description: Create a new YouTube script draft
allowed-tools: Read, Write, AskUserQuestion
---

# Create YouTube Script Draft

Create a new YouTube script draft in `1-content/04-youtube/01-drafts/`.

## Topic

$ARGUMENTS

## Steps

1. **Determine video type** based on topic:
   - **tutorial**: "How to X", step-by-step guides
   - **explainer**: "What is X", concept explanations
   - **deep-dive**: Comprehensive explorations
   - **case-study**: "How I built X", results-focused

2. **Read voice file**: `1-content/04-youtube/VOICE_youtube.md` (if exists)

3. **Create file**: `1-content/04-youtube/01-drafts/YYYY-MM-DD-<slug>.md`
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
title: "Video Title"
description: "Video description"
platform: youtube
category: tutorial | explainer | deep-dive | case-study
duration: 5-10 min | 10-20 min | 20+ min
---

# {Title}

## Intro (30-90 seconds)

### Hook
[Bold claim, surprising result, or compelling question]

### Context
[What we'll cover and who this is for]

## Main Content

### Section 1: {Topic}

[Content with visual cues]

**B-ROLL**: [Description of what to show]

### Section 2: {Topic}

[Content with visual cues]

**SCREEN SHARE**: [What to demonstrate]

### Section 3: {Topic}

[Content with visual cues]

## Outro

### Key Takeaways
1. {Takeaway 1}
2. {Takeaway 2}
3. {Takeaway 3}

### CTA
[Subscribe, comment prompt, next video teaser]
```

## Instructions

- Apply VOICE_youtube.md patterns if available
- Include visual cues (B-ROLL, SCREEN SHARE, etc.)
- Write for spoken delivery, not reading
- Keep sections focused and progressive
- Be specific and opinionated

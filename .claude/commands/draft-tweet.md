---
description: Create a new tweet draft
allowed-tools: Read, Write
---

# Create Tweet Draft

Create four tweet drafts in `1-content/03-twitter/01-drafts/`.

## Topic

$ARGUMENTS

## Steps

1. **Read voice file**: `1-content/03-twitter/VOICE_twitter.md` (if exists)

2. **Create file**: `1-content/03-twitter/01-drafts/YYYY-MM-DD-<slug>.md`
   - Use today's date
   - Generate slug from topic: lowercase, dashes, no special chars

## Draft Template

```markdown
---
title: "Tweet Title"
description: "Tweet description"
platform: twitter
category: educate | convince | inspire | entertain
perspective: personal | expert | general
visual: none | image | video
---

## Option 1: Educate

[Tweet content - max 280 characters]

[Optional: 3-5 relevant hashtags]

## Option 2: Inspire

[Tweet content - max 280 characters]

[Optional: 3-5 relevant hashtags]

## Option 3: Entertain

[Tweet content - max 280 characters]

[Optional: 3-5 relevant hashtags]

## Option 4: Convince

[Tweet content - max 280 characters]

[Optional: 3-5 relevant hashtags]
```

## Instructions

- Apply VOICE_twitter.md patterns if available
- Keep under 280 characters (excluding hashtags)
- Be specific and opinionated
- Use emojis sparingly but effectively
- Include 3-5 relevant hashtags at the end
- Add **"(Recommended)"** next to the option you evaluate as best for engagement
- If a video or image would enhance the tweet, add a comment with description: `<!-- VIDEO: [description] -->` or `<!-- IMAGE: [description] -->`

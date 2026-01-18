---
description: Create a new LinkedIn post draft
allowed-tools: Read, Write
---

# Create LinkedIn Draft

Create a new LinkedIn post draft in `1-content/02-linkedin/01-drafts/`.

## Topic

$ARGUMENTS

## Steps

1. **Read voice file**: `1-content/02-linkedin/VOICE_linkedin.md` (if exists)
2. **Create file**: `1-content/02-linkedin/01-drafts/YYYY-MM-DD-<slug>.md`
   - Use today's date
   - Generate slug from topic: lowercase, dashes, no special chars

## Content Framework

**Formula**: Category x Perspective x Topic

### Categories (pick one)
- **Educate**: Teach practical skills (main lead driver)
- **Convince**: Prove results with case studies/testimonials
- **Inspire**: Build trust through stories
- **Entertain**: Boost reach with creative/fun content

### Perspectives (pick one)
- **Personal**: Real wins, struggles, lessons
- **Expert**: Deep, niche insights proving expertise
- **General**: Broad tips reaching wider audience

## Post Anatomy

1. **Trigger**: One bold, clear line that makes them stop
2. **Story**: Quick personal moment or real example
3. **Value**: 2-4 punchy bullets with specifics
4. **CTA**: Question, invite to DM, or call to save/share

## Draft Template

```markdown
---
title: "Post Title"
description: "Post description"
platform: linkedin
category: educate | convince | inspire | entertain
perspective: personal | expert | general
visual: none | image | carousel | video
---

## Option 1: Educate

[HOOK: One bold line that makes them stop scrolling]

[STORY: Quick personal moment or real example - 2-3 sentences]

[VALUE: 2-4 punchy bullets with specifics]
- {Specific insight 1}
- {Specific insight 2}
- {Specific insight 3}

[CTA: Question, invite to DM, or call to save/share]

## Option 2: Inspire

[HOOK: One bold line that makes them stop scrolling]

[STORY: Quick personal moment or real example - 2-3 sentences]

[VALUE: 2-4 punchy bullets with specifics]
- {Specific insight 1}
- {Specific insight 2}
- {Specific insight 3}

[CTA: Question, invite to DM, or call to save/share]

## Option 3: Entertain

[HOOK: One bold line that makes them stop scrolling]

[STORY: Quick personal moment or real example - 2-3 sentences]

[VALUE: 2-4 punchy bullets with specifics]
- {Specific insight 1}
- {Specific insight 2}
- {Specific insight 3}

[CTA: Question, invite to DM, or call to save/share]

## Option 4: Convince

[HOOK: One bold line that makes them stop scrolling]

[STORY: Quick personal moment or real example - 2-3 sentences]

[VALUE: 2-4 punchy bullets with specifics]
- {Specific insight 1}
- {Specific insight 2}
- {Specific insight 3}

[CTA: Question, invite to DM, or call to save/share]
```

## Instructions

- Apply VOICE_linkedin.md patterns if available
- Target: <800 characters per option
- Emojis sparingly, for tone only
- Trim the fat: short, punchy, high-value
- Be specific and opinionated
- Add **"(Recommended)"** next to the option you evaluate as best for engagement
- If a video, image, or carousel would enhance the post, add a comment with description: `<!-- VIDEO: [description] -->` or `<!-- IMAGE: [description] -->` or `<!-- CAROUSEL: [description] -->`

---
description: Analyze top content (my-top + swipe-files) and update platform voice guide
allowed-tools: Read, Write, Edit, Glob
---

# Update Voice Guide

Analyze top content (my-top + swipe-files) for a specific platform and update its VOICE_{platform}.md file.

## Arguments

$ARGUMENTS - Required platform: `blog` | `linkedin` | `twitter` | `youtube`

## Platform Locations

| Platform  | Content Folders | Voice File |
|-----------|----------------|------------|
| blog      | `1-content/01-blog/04-my-top/` AND `1-content/01-blog/05-swipe-files/` | `1-content/01-blog/VOICE_blog.md` |
| linkedin  | `1-content/02-linkedin/04-my-top/` AND `1-content/02-linkedin/05-swipe-files/` | `1-content/02-linkedin/VOICE_linkedin.md` |
| twitter   | `1-content/03-twitter/04-my-top/` AND `1-content/03-twitter/05-swipe-files/` | `1-content/03-twitter/VOICE_twitter.md` |
| youtube   | `1-content/04-youtube/shorts/` AND `1-content/04-youtube/videos/` | `1-content/04-youtube/VOICE_youtube.md` |

## Process

1. **Validate platform argument**
   - Must be one of: blog, linkedin, twitter, youtube
   - If not provided or invalid, ask user which platform to analyze

2. **Read existing voice file** from platform location (if exists)

3. **Read all content** from platform's folder(s)
   - Use Glob to find all `.md` files in both `04-my-top/` AND `05-swipe-files/`
   - For YouTube: read from both `shorts/` AND `videos/`

4. **Analyze content for patterns**:
   - **Voice and tone**: Authoritative vs. casual balance
   - **Sentence structure**: Simple/compound/complex mix, typical lengths
   - **Opening patterns**: How content starts (hooks, statements, questions)
   - **Closing patterns**: How content ends (CTAs, summaries, challenges)
   - **Signature phrases**: Recurring expressions unique to this platform
   - **Technical explanation style**: How complex concepts are broken down
   - **Emoji usage**: Frequency, placement, types used
   - **Format patterns**: Headers, bullets, code blocks (platform-specific)

5. **Compare findings** against current voice file (if exists)
   - Identify new patterns discovered
   - Identify patterns that still hold
   - Identify patterns that should be removed/updated

6. **Update VOICE_{platform}.md** using the embedded template structure below:
   - Preserve existing patterns that still hold
   - Add new patterns discovered
   - Update Writing Patterns section with real examples
   - Update Reference Examples with links to analyzed content

7. **Report changes made**:
   - New patterns discovered
   - Patterns updated or removed

## Voice File Template

Use this structure when creating or updating the voice file:

```markdown
---
title: "{Platform} Voice Guide"
description: "How I write on {Platform}"
---

# {Platform} Voice Guide

*Last updated: {date}*

## I Sound Like

{2-3 sentences describing the overall tone and personality on this platform}

## Audience

- **Who I'm talking to**: {specific audience description}
- **What they care about**: {their goals/pain points}

## I Always

- {Pattern 1 - be specific, e.g., "Lead with a bold claim or surprising fact"}
- {Pattern 2 - e.g., "Use short paragraphs, max 2-3 lines"}
- {Pattern 3 - e.g., "End with a question or clear CTA"}
- {Pattern 4}
- {Pattern 5}

## I Never

- {Anti-pattern 1 - e.g., "Use 'Key takeaways' or 'In conclusion'"}
- {Anti-pattern 2 - e.g., "Start with 'I'm excited to share...'"}
- {Anti-pattern 3 - e.g., "Use more than 2 emojis per post"}
- {Banned phrases}

## Sentence Style

- {Length pattern - e.g., "Short sentences. Punchy. Rarely over 15 words."}
- {Structure pattern - e.g., "Questions to transition: 'So what does this mean?'"}
- {Punctuation pattern - e.g., "Em dashes for emphasis, not parentheses"}

## Opening Hooks

**{Hook type 1}**
> "{Real example from analyzed content}"

**{Hook type 2}**
> "{Real example from analyzed content}"

**{Hook type 3}**
> "{Real example from analyzed content}"

## Closing Patterns

**{Closing type 1}**
> "{Real example from analyzed content}"

**{Closing type 2}**
> "{Real example from analyzed content}"

## Signature Phrases

- "{Phrase I actually use}"
- "{Another phrase}"
- "{Another phrase}"

## Format Rules

- **Length**: {platform-specific limits}
- **Structure**: {how I organize content - sections, bullets, etc.}
- **Emojis**: {when/how I use them}
- **Hashtags**: {usage pattern if applicable}

## Reference Examples

{Title or link to top-performing content that exemplifies this voice}
```

## Output Format

```
## Voice Update Report: {platform}

### New Patterns Discovered
- {pattern 1}
- {pattern 2}

### Patterns Updated
- {change 1}
- {change 2}

### Reference Examples Added
- {title 1}
- {title 2}
```

## Notes

- If no swipe files exist, create a stub voice file and notify the user
- Preserve any manually-added content that doesn't conflict with analyzed patterns
- Focus on patterns that appear in 2+ samples (not one-offs)

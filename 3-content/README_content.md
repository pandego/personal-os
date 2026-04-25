# Content Domain

This is where blog and LinkedIn content gets drafted and refined.

## What lives here

- `01-blog/` - long-form writing and article workflow
- `02-linkedin/` - LinkedIn post workflow
- `_voice-samples/` - flat folder of sample writing in your voice (any prose; no platform split)
- `_external/` - media or supporting assets

## Keep it simple

You do not need to over-organize this area.

A good rule is:
- put drafts in the platform draft folder
- drop any prose in your voice into `_voice-samples/` (emails, posts, notes, anything)
- use markdown files whenever possible

## Platform structure

### Blog
- `01-blog/01-drafts/` - work in progress
- `01-blog/02-in-review/` - ready for final review
- `01-blog/03-published/` - published archive
- `01-blog/README_blog.md` - short guide for the blog area

### LinkedIn
- `02-linkedin/01-drafts/` - work in progress
- `02-linkedin/02-in-review/` - ready for final review
- `02-linkedin/03-published/` - published archive
- `02-linkedin/README_linkedin.md` - short guide for the LinkedIn area

### Voice samples
- `_voice-samples/` - flat folder. Drop any prose in your voice (emails, blog posts, LinkedIn posts, notes).
- `_voice-samples/README_voice-samples.md` - how to use this area

## How the assistant uses this

Before drafting content, the assistant reads:
1. `memories/USER.md` for directness and avoid preferences
2. `VOICE.md` at repo root for voice patterns (populated by `/draft-content` update-voice)

## Skills
- `draft-content` - three cookbooks: write a blog post, write a LinkedIn post, or update root `VOICE.md` from samples

## Workflow
- Start in `01-drafts/`
- Move to `02-in-review/` when the draft is worth polishing
- Move to `03-published/` after it is live
- Use filenames like `YYYY-MM-DD-slug.md`

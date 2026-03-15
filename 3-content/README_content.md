# Content Domain

This is where blog and LinkedIn content gets drafted and refined.

## What lives here

- `01-blog/` - long-form writing and article workflow
- `02-linkedin/` - LinkedIn post workflow
- `_voice-samples/` - sample writing that helps the assistant learn how you like to sound on each platform
- `_external/` - media or supporting assets

## Keep it simple

You do not need to over-organize this area.

A good rule is:
- put drafts in the platform draft folder
- put useful voice samples in `_voice-samples/blog/` or `_voice-samples/linkedin/`
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
- `_voice-samples/blog/` - blog examples in your voice or examples worth learning from
- `_voice-samples/linkedin/` - LinkedIn examples in your voice or examples worth learning from
- `_voice-samples/README_voice-samples.md` - how to use this area

## How the assistant uses this

Before drafting content, the assistant should read:
1. `VOICE.md`
2. relevant samples from `_voice-samples/<platform>/` when useful

## Skills
- `draft-content` - drafts content for blog or LinkedIn and can also refresh voice guidance from examples when needed

## Workflow
- Start in `01-drafts/`
- Move to `02-in-review/` when the draft is worth polishing
- Move to `03-published/` after it is live
- Use filenames like `YYYY-MM-DD-slug.md`

# Content Domain

All content creation for Blog and LinkedIn.

## Structure
- `01-blog/` - Long-form articles
  - `01-drafts/` → `02-in-review/` → `03-published/`
  - `04-my-top/` - Curated best posts (voice source)
  - `05-swipe-files/` - External examples (inspiration)
  - Voice: VOICE_blog.md
- `02-linkedin/` - Professional posts (same structure as blog)
- `_external/` - Media and external assets

## Idea Capture
Capture ideas in whatever way feels natural, then move the useful ones into the right folder when you are ready to shape them.

A simple approach is:
- keep rough idea notes nearby until they matter
- move promising ideas into the correct `01-drafts/` folder
- use the folder structure to separate rough work from refined work

Alternatively, drop idea files directly into a platform's `01-drafts/` folder, then reference them when calling `/draft-*` commands.

## Platform Folder Structure
Each platform follows this pattern:
```
{platform}/
├── 01-drafts/       # Work in progress
├── 02-in-review/    # Ready for final review
├── 03-published/    # Posted live (archive)
├── 04-my-top/       # Curated best (for voice building)
├── 05-swipe-files/  # External examples (inspiration)
└── VOICE_*.md       # Platform voice guide
```

## Before Creating Content
**ALWAYS read `VOICE.md` and `VOICE_<platform>.md` first.** Apply voice patterns to all content.

## Voice Building
Voice is built from two sources per platform:
1. **04-my-top/** - Your best published content (curated, not all)
2. **05-swipe-files/** - External examples to learn from

Use `/update-voice <platform>` to analyze both and update the `VOICE_*.md` file.

## Commands
| Command | Action |
|---------|--------|
| `/draft-blog` | Create blog draft |
| `/draft-linkedin` | Create LinkedIn draft |
| `/update-voice` | Analyze content and update voice guide |

## Content Workflow
- Work in `01-drafts/` until content is ready
- Move to `02-in-review/` for final polish and review
- Move to `03-published/` after posting live
- Use date format: `YYYY-MM-DD-slug.md`

## Quality Checklist
- [ ] Voice matches `VOICE.md` and platform-specific `3-content/<platform>/VOICE_<platform>` patterns
- [ ] Hook is specific and compelling
- [ ] Technical claims have support
- [ ] Code examples are runnable
- [ ] CTA is included

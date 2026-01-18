# Content Domain

All content creation for Blog, LinkedIn, Twitter/X, and YouTube.

## Structure
- `01-blog/` - Long-form articles
  - `01-drafts/` → `02-in-review/` → `03-published/`
  - `04-my-top/` - Curated best posts (voice source)
  - `05-swipe-files/` - External examples (inspiration)
  - Voice: VOICE_blog.md
- `02-linkedin/` - Professional posts (same structure as blog)
- `03-twitter/` - Single tweets and threads (same structure)
- `04-youtube/` - Scripts and metadata
- `_external/` - Media and external assets

## Idea Capture
Ideas are captured via `KANBAN.md` (synced with Todoist PersonalOS project via `/process-backlog`).
For details on Todoist/Kanban setup, see the root `README.md`.

**Important**: Tag ideas clearly (e.g., "blog idea", "linkedin idea") so they sync correctly to the Kanban.

Alternatively, drop idea files directly into any platform's `01-drafts/` folder, then reference them when calling `/draft-*` commands.

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
**ALWAYS read `VOICE.md` and `VOICE_<platform>.md` first.** Apply voice patterns to ALL content.

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
| `/draft-tweet` | Create single tweet draft |
| `/draft-youtube-script` | Create YouTube script |
| `/update-voice` | Analyze content and update voice guide |

## Content Workflow
- Work in `01-drafts/` until content is ready
- Move to `02-in-review/` for final polish and review
- Move to `03-published/` after posting live
- Use date format: `YYYY-MM-DD-slug.md`

## Quality Checklist
- [ ] Voice matches `VOICE.md` and platform-specific in `1-content/<platform>/VOICE_<platform>` patterns
- [ ] Hook is specific and compelling
- [ ] Technical claims have support
- [ ] Code examples are runnable
- [ ] CTA is included

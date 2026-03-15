# Personal Domain

Private tracking separate from public content and business.

## Structure
- `01-week-reviews/` - Weekly retrospectives
- `02-year-reviews/` - Annual reviews
- `03-knowledge/` - Personal knowledge and private reference material

## Reviews

Run `/review` to invoke the review skill. It will:
1. Ask whether you want a week or year review
2. Gather the notes and material it can find in this workspace
3. Ask guided reflection questions
4. Generate a structured review with a forward-looking planning section

**Output locations:**
- Week: `01-week-reviews/02-done/YYYY-MM-DD_WXX_week-review.md`
- Year: `02-year-reviews/02-done/YYYY_year-review.md`

**Skill location:** `.codex/skills/review/` (with `.claude/` symlinked to `.codex/`)

## Knowledge
- `03-knowledge/` is for personal reference material that should not live in business or content folders
- Keep this area useful, private, and lightweight
- Prefer organized reference notes over dumping everything here

## Commands
| Command | Action |
|---------|--------|
| `/review` | guided weekly or yearly reflection |

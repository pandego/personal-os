# Personal Domain

Private tracking separate from public content and business.

## Structure
- `01-week-reviews/` - Weekly retrospectives
- `02-year-reviews/` - Annual reviews
- `03-knowledge/` - Personal knowledge and data exports

## Reviews

Run `/review` to invoke the unified review skill. It will:
1. Ask whether you want a week or year review
2. Gather completed tasks from ALL Todoist projects (not just PersonalOS)
3. Check KANBAN.md Done section
4. Ask guided questions (5-7 for week, 8-10 for year)
5. Generate structured review with planning section

**Output locations:**
- Week: `01-week-reviews/02-done/YYYY-MM-DD_WXX_week-review.md`
- Year: `02-year-reviews/02-done/YYYY_year-review.md`

**Skill location:** `.claude/skills/review/`

## Knowledge
- `03-knowledge/data-exports/` - LinkedIn exports, etc.
- Not for public content - personal reference only

## Commands
| Command | Action |
|---------|--------|
| `/review` | Unified review skill (week/year) |

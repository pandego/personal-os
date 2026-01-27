---
name: review
description: Unified review skill for weekly and yearly reflections. Gathers completed tasks from ALL Todoist projects and KANBAN.md, processes transcripts/notes, and generates structured reviews with forward planning. Triggers on /review-week, /review-year, or general review requests.
---

# Review Skill

Router for review workflows. Dispatches to specialized cookbooks based on review type.

## Trigger Phrases

- `/review-week` or `/review-year`
- "do my weekly review"
- "generate week review"
- "let's do a review"
- "year in review"

---

## Routing Flow

### Step 1: Determine Review Type

If not explicit from trigger, ask:

> "What type of review are we doing?"
>
> - **Week** — Reflect on the past week, plan the next
> - **Year** — Annual retrospective and planning

**Auto-detect hints:**
- December/January + "review" → likely year
- Friday/Sunday/Monday + "review" → likely week
- Explicit `/review-week` or `/review-year` → use that

### Step 2: Gather Input Source

Use `AskUserQuestion`:

> "Do you have notes or a transcript to include?"
>
> - **Yes, file path** — "Point me to the file"
> - **Yes, paste it** — "I'll paste/dictate my notes"
> - **No, just data** — "Build from Todoist + KANBAN only"

### Step 3: Execute Workflow

```
→ Read cookbook/gather-data.md
→ Execute data gathering (Todoist ALL projects + KANBAN + last review)

IF review_type = "week":
    → Read cookbook/week.md
    → Execute week review workflow
    → Read cookbook/plan-ahead.md
    → Execute planning phase

IF review_type = "year":
    → Read cookbook/year.md
    → Execute year review workflow
```

---

## Reference Documents

Load these as needed:

| Document | When to Load |
|----------|--------------|
| `REVIEW_PATTERNS.md` | When formatting review content |
| `prompts/week-questions.md` | Week review interactive questions |
| `prompts/year-questions.md` | Year review interactive questions |
| `templates/week-review.md` | Week output format (source of truth) |
| `templates/year-review.md` | Year output format (source of truth) |

**Note:** Templates define the output structure. The skill is self-contained.

---

## Output Locations

| Review Type | Output Path |
|-------------|-------------|
| Week | `3-personal/01-week-reviews/02-done/YYYY-MM-DD_WXX_week-review.md` |
| Year | `3-personal/02-year-reviews/02-done/YYYY_year-review.md` |

**Date conventions:**
- Week review: Use Friday date + week number (e.g., `2026-01-24_W04_week-review.md`)
- Year review: Use the year being reviewed (e.g., `2025_year-review.md`)

**Week number calculation:**
```bash
uv run .claude/skills/review/tools/week_number.py --filename        # Current week
uv run .claude/skills/review/tools/week_number.py 2026-01-24 --filename  # Specific date
```

Or inline: `uv run python -c "from datetime import datetime; d=datetime.now(); print(f'W{d.isocalendar()[1]:02d}')"`

---

## Output Summary

After completion, show:

> **Review complete!**
>
> **Accomplishments:** X tasks completed across Y projects
> **Key highlights:**
> - [highlight 1]
> - [highlight 2]
>
> **Next week priorities:**
> - [priority 1]
> - [priority 2]
>
> ---
> Saved to: `[file path]`

---

## Error Handling

| Error | Response |
|-------|----------|
| Todoist MCP not connected | "Run `/mcp` and connect the Todoist server first" |
| No previous review found | Ask user for date range to cover |
| Empty transcript | Proceed with data-only review, note in output |
| KANBAN.md missing | Continue with Todoist data only |

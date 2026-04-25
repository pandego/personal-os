---
name: review
description: Unified review skill for weekly and yearly reflections. Gathers available notes, prior reviews, workspace material, and user input to generate structured reviews with forward planning.
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
> - **Week** - Reflect on the past week, plan the next
> - **Year** - Annual retrospective and planning

### Step 2: Gather Input Source

Use `AskUserQuestion`:

> "Do you have notes or material to include?"
>
> - **Yes, file path** - "Point me to the file"
> - **Yes, paste it** - "I'll paste or dictate my notes"
> - **No, just workspace data** - "Build from what is already in this folder"

### Step 3: Execute Workflow

```
→ Read cookbook/gather-data.md
→ Execute local-first data gathering (prior reviews, workspace material, transcript/notes)

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
| `templates/week-review.md` | Week output format |
| `templates/year-review.md` | Year output format |

---

## Output Locations

| Review Type | Output Path |
|-------------|-------------|
| Week | `1-personal/01-week-reviews/02-done/YYYY-MM-DD_WXX_week-review.md` |
| Year | `1-personal/02-year-reviews/02-done/YYYY_year-review.md` |

---

## Output Summary

After completion, show:

> **Review complete!**
>
> **Key highlights:**
> - [highlight 1]
> - [highlight 2]
>
> **Next priorities:**
> - [priority 1]
> - [priority 2]
>
> ---
> Saved to: `[file path]`

---

## Error Handling

| Error | Response |
|-------|----------|
| No previous review found | Ask user for date range to cover |
| Input file missing | Ask user to verify path |
| Empty notes | Proceed with workspace-only review and note the limitation |

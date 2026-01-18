---
description: Generate a yearly review
allowed-tools: Read, Write, Glob
---

# Generate Yearly Review

Generate a structured yearly review.

## Arguments

$ARGUMENTS - year to review (default: previous year) or transcript/notes

## Steps

1. **Determine review year**:
   - If year provided (e.g., "2025"), use that
   - Otherwise, use previous year
   - If transcript provided, extract year from context

2. **Read the template**: `3-personal/02-year-reviews/TEMPLATE_year-review.md`

3. **Read `VOICE.md`** for voice patterns

4. **Gather context** (if available):
   - Read weekly reviews from `3-personal/01-week-reviews/02-done/` for the year
   - Look for content published in `1-content/*/03-published/`
   - Check `2-business/02-clients/` for client work
   - Review `2-business/03-upwork/02-proposals/` for freelance activity

5. **Create file**: `3-personal/02-year-reviews/02-done/YYYY_year-review.md`

## Instructions

- If a transcript is provided, extract information from it
- If no transcript, use gathered context to populate sections
- Mark sections as "[To fill in]" where data is missing
- Be honest about both achievements and failures
- Include concrete numbers where possible

## Review Sections

1. **Theme of the Year**: One sentence summary
2. **Highlights & Lowlights**
3. **Goals & Outcomes**: Table with achievement status
4. **What Went Well / Didn't Go Well**
5. **Key Learnings**
6. **By the Numbers**: Content, business, personal metrics
7. **Major Decisions Made**
8. **Relationships & Network**
9. **Health & Wellbeing**
10. **Next Year Priorities**
11. **Word/Theme for Next Year**

## Output

Generate a complete review following the template structure.
Fill in what's known, mark unknowns for manual completion.

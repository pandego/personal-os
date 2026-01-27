# Cookbook: Week Review

Generate a structured weekly review through guided questions and data synthesis.

**Input:** Data package from `gather-data.md`
**Output:** Completed week review file

---

## Interactive Flow (5-7 Questions)

### Question 1: Validate Accomplishments

Present the gathered data:

> "Here's what I found you completed this week:"
>
> **From Todoist (X tasks across Y projects):**
> - [task 1]
> - [task 2]
> - ...
>
> **From KANBAN Done:**
> - [item 1]
> - [item 2]
>
> "Anything missing or incorrect?"
>
> - **Looks good** — proceed
> - **Add more** — "What else did you accomplish?"
> - **Remove some** — "Which ones weren't actually done?"

### Question 2: Highlights

> "What were the TOP 2-3 highlights of your week?"
>
> *Suggest based on data:*
> - [Completed high-priority task]
> - [Finished long-running project]
> - [Published content]
>
> - **Use suggestions** — accept proposed highlights
> - **Different highlights** — "Tell me what stood out"

### Question 3: Goals & Outcomes

If previous review had priorities, show tracking:

> "Last week you planned to:"
> 1. [Priority 1] → Status: DONE/PARTIAL/NOT DONE
> 2. [Priority 2] → Status: ...
>
> "Does this look right? Any context to add?"
>
> - **Accurate** — proceed
> - **Add context** — "What happened with [item]?"

If no previous review:

> "What were your main goals for this week? How did they go?"

### Question 4: What Went Well

> "What went particularly well this week?"
>
> *Prompts to consider:*
> - Processes that worked
> - Habits that helped
> - Collaborations that clicked
> - Decisions you're glad you made
>
> - **List 2-3 things** — free text input

### Question 5: What Didn't Go Well

> "What didn't go as planned?"
>
> *Prompts to consider:*
> - Tasks that slipped
> - Blockers encountered
> - Time sinks
> - Distractions
>
> - **List 2-3 things** — free text input

### Question 6: Blockers

> "Any blockers or challenges that impacted your week?"
>
> For each blocker mentioned:
> - What was the blocker?
> - What was its impact?
> - Is it resolved? If not, what's needed?
>
> - **Yes, blockers** — describe them
> - **No blockers** — skip section

### Question 7: Learnings

> "What did you learn this week?"
>
> *Can be:*
> - Technical skills
> - Process improvements
> - Personal insights
> - Industry knowledge
>
> - **Share learnings** — list 1-3
> - **Nothing notable** — skip section

---

## Generate Review

### Read Template

```
Read: .claude/skills/review/templates/week-review.md
```

Use this as the template for structure and format.

### Read Questions

```
Read: .claude/skills/review/prompts/week-questions.md
```

Follow the question flow defined there.

### Populate Sections

Using gathered data + question responses:

```markdown
# Weekly Review — WXX (Week of YYYY-MM-DD)

## Highlights
- [From Question 2 responses]

## Goals & Outcomes
- **Goal:** [From last review priorities]
  - **Outcome:** Achieved / Partial / Not achieved
  - **Notes:** [From Question 3 context]

## What Went Well
- [From Question 4 responses]

## What Didn't Go Well
- [From Question 5 responses]

## Blockers
- **Blocker:** [From Question 6]
  - **Impact:** ...
  - **Resolution:** ...

## Learnings
- [From Question 7 responses]

## Completed This Week
[Auto-generated from data]

### By Project
**PersonalOS (X tasks)**
- [x] Task 1
- [x] Task 2

**Work (Y tasks)**
- [x] Task 3

### From KANBAN
- [x] Item 1

## Next Week Priorities (3-5)
[Populated by plan-ahead.md cookbook]

## Next Actions
[Populated by plan-ahead.md cookbook]

## Notes
- [From transcript if provided]
- [Any additional context]
```

---

## Writing Guidelines

Reference `../REVIEW_PATTERNS.md` for quality standards:

- **Concrete over vague**: "Shipped auth feature" not "Made progress"
- **Honest assessment**: Don't inflate or deflate
- **Forward-looking**: Connect learnings to future actions
- **Concise bullets**: No paragraph blocks in bullet points

---

## Output

Write to: `3-personal/01-week-reviews/02-done/YYYY-MM-DD_WXX_week-review.md`

**Naming convention:**
- Date: Use Friday of the reviewed week
- Week number: ISO week number, zero-padded (W01-W53)

**Calculate week number:**
```bash
uv run .claude/skills/review/tools/week_number.py --filename
# Or for specific date:
uv run .claude/skills/review/tools/week_number.py 2026-01-24 --filename
```

Example: Week of Jan 20-26, 2026 → `2026-01-24_W04_week-review.md`

**Title format:**
```markdown
# Weekly Review — W04 (Week of 2026-01-24)
```

---

## Handoff to Planning

After generating review content, dispatch to `plan-ahead.md` cookbook for:
- Next Week Priorities
- Next Actions
- Monthly outlook (if applicable)

Return to SKILL.md router after planning complete.

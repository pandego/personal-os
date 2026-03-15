# Cookbook: Gather Data

Collect all completion data from Todoist (ALL projects), KANBAN.md, and the last review.

**Purpose:** Build a comprehensive picture of what was accomplished since the last review.

---

## Step 1: Find Last Review

### For Week Reviews

```
Glob: 3-personal/01-week-reviews/02-done/*.md
Sort by date descending
Read the most recent one
Extract: date, next week priorities, any unfinished items
```

**If no previous review exists:**
→ Use `AskUserQuestion`:
> "I couldn't find a previous week review. What date range should I cover?"
>
> - **Last 7 days**
> - **Since last Monday**
> - **Custom date** — "Enter start date"

### For Year Reviews

```
Glob: 3-personal/02-year-reviews/02-done/*.md
Find review for previous year if exists
Also gather: 3-personal/01-week-reviews/02-done/*{YEAR}*.md (all week reviews for the year)
```

---

## Step 2: Get Todoist Completed Tasks

**IMPORTANT: Query ALL projects, not just PersonalOS**

### 2a. Determine Date Range

```python
if last_review_date:
    start_date = last_review_date
else:
    start_date = user_provided_date or "7 days ago"

end_date = today
```

### 2b. Fetch Completed Tasks

```
Use mcp__claude_ai_todoist__find-completed-tasks with:
    - completedAfter: start_date (ISO format)
    - completedBefore: end_date (ISO format)
    - limit: 200 (generous to capture all)

NOTE: Do NOT filter by projectId — we want ALL projects
```

### 2c. Organize by Project

Group completed tasks by project for reporting:

```
Project: PersonalOS
  - [x] Task 1 (completed 2026-01-20)
  - [x] Task 2 (completed 2026-01-21)

Project: Work
  - [x] Task 3 (completed 2026-01-19)

Project: Inbox
  - [x] Quick task (completed 2026-01-22)
```

---

## Step 3: Get Active Tasks (for Planning)

### 3a. Fetch All Active Tasks

```
Use mcp__claude_ai_todoist__find-tasks with:
    - No projectId filter (gets all)
    - Include priority, due dates, labels
```

### 3b. Categorize for Planning

```
Overdue:
  - Task with past due date

Due This Week:
  - Tasks due within next 7 days

Due This Month:
  - Tasks due within next 30 days

No Due Date:
  - Backlog items
```

---

## Step 4: Read KANBAN.md

```
Read: KANBAN.md (root)

Extract:
- Done section (completed since last sync)
- In Progress section (current work)
- Ready section (next up)
- Backlog section (ideas/future)
```

**Cross-reference with Todoist:**
- Items in KANBAN Done that aren't in Todoist completed → add to accomplishments
- Items in both → deduplicate

---

## Step 5: Read User Transcript (if provided)

If user provided a file path or pasted notes:

```
Read the transcript
Extract:
- Mentioned accomplishments (match against Todoist/KANBAN)
- Blockers mentioned
- Learnings mentioned
- Emotional tone/highlights
- Plans mentioned
```

**Transcript processing rules:**
- Accept messy, spoken-style input
- Infer meaning, correct obvious transcription errors
- Don't invent — only extract what's actually there
- Mark unclear items with "(unclear)"

---

## Step 6: Compare Against Last Review

### For Week Reviews

Compare last review's "Next Week Priorities" against completed tasks:

```
Last week's priorities:
1. "Finish project X" → DONE (found in Todoist completed)
2. "Start blog post" → PARTIAL (in KANBAN In Progress)
3. "Call client" → NOT DONE (not found anywhere)
```

This becomes input for "Goals & Outcomes" section.

### For Year Reviews

Compare last year's goals against all accomplishments:
- Pull from last year review's "Next Year Priorities"
- Check against completed tasks, published content, client work

---

## Output: Data Package

Return structured data for the review cookbook:

```yaml
review_period:
  start: YYYY-MM-DD
  end: YYYY-MM-DD

previous_review:
  date: YYYY-MM-DD
  priorities_set: [list]

completed_tasks:
  by_project:
    ProjectName: [tasks]
  total_count: N

active_tasks:
  overdue: [tasks]
  due_this_week: [tasks]
  due_this_month: [tasks]
  backlog: [tasks]

kanban_state:
  done: [items]
  in_progress: [items]
  ready: [items]

transcript_insights:
  accomplishments: [extracted]
  blockers: [extracted]
  learnings: [extracted]
  highlights: [extracted]

priority_tracking:
  completed: [matched items]
  partial: [in progress items]
  not_done: [unmatched items]
```

---

## Error Handling

| Error | Response |
|-------|----------|
| Todoist rate limited | Wait 60s, retry |
| No completed tasks found | Proceed with KANBAN + transcript only |
| KANBAN.md not found | Proceed with Todoist data only |
| Transcript file not found | Ask user to verify path |

# Cookbook: Gather Data

Collect review inputs from the local workspace, previous reviews, and any user-provided notes.

**Purpose:** Build a grounded picture of what happened without depending on external task systems.

---

## Step 1: Find Last Review

### For Week Reviews

```
Glob: 1-personal/01-week-reviews/02-done/*.md
Sort by date descending
Read the most recent one
Extract: date, next week priorities, unfinished items, notable patterns
```

If no previous week review exists, ask the user what date range to cover.

### For Year Reviews

```
Glob: 1-personal/02-year-reviews/02-done/*.md
Find review for previous year if it exists
Also gather: 1-personal/01-week-reviews/02-done/*{YEAR}*.md
```

---

## Step 2: Read Workspace Material

Look for useful signals in the local workspace.

Examples:
- recent review files
- notes or drafts the user points to
- relevant material in `1-personal/03-knowledge/`
- recent content drafts or published material in `3-content/`
- business artifacts in `2-business/` if they are relevant to the review period

Do not force every folder into the review. Prefer relevant evidence over folder tourism.

---

## Step 3: Read User Notes (if provided)

If the user provided a file path or pasted notes:

```
Read the notes
Extract:
- accomplishments
- blockers
- learnings
- emotional tone/highlights
- plans or priorities mentioned
```

Rules:
- accept messy spoken-style input
- infer obvious meaning without inventing facts
- mark uncertain items as unclear instead of fabricating certainty

---

## Step 4: Compare Against Last Review

### For Week Reviews
Compare last review's planned priorities against what appears to have happened.

Use categories like:
- done
- partial
- not done
- no longer relevant

### For Year Reviews
Compare prior yearly goals and recurring patterns against the year’s visible work and notes.

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

workspace_signals:
  notes: [items]
  content: [items]
  business: [items]
  personal: [items]

user_notes:
  accomplishments: [items]
  blockers: [items]
  learnings: [items]
  highlights: [items]

priority_tracking:
  completed: [items]
  partial: [items]
  not_done: [items]
  no_longer_relevant: [items]
```

---

## Error Handling

| Error | Response |
|-------|----------|
| No prior review found | Ask user for date range |
| No useful workspace material found | Proceed with user notes/questions only |
| Notes file missing | Ask user to verify path |

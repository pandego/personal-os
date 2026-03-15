# Cookbook: Plan Ahead

Generate forward-looking sections: next week priorities, next actions, and monthly outlook.

**Input:** Data from gather-data.md (active tasks, overdue items)
**Output:** Planning sections for the review document

---

## Step 1: Analyze Active Work

From the data package, organize:

```
OVERDUE (requires immediate attention):
- Task with past due date

DUE THIS WEEK:
- Tasks due in next 7 days

HIGH PRIORITY (P1/P2):
- Priority tasks regardless of due date

IN PROGRESS (from KANBAN):
- Currently active work

READY (from KANBAN):
- Next up items
```

---

## Step 2: Present Current State

Show user their active landscape:

> "Here's what's on your plate:"
>
> **Overdue (X items):**
> - [task 1] — was due [date]
> - [task 2] — was due [date]
>
> **Due This Week (Y items):**
> - [task 3] — due [date]
>
> **In Progress (Z items):**
> - [item from KANBAN]
>
> **Ready/Next Up (N items):**
> - [item from KANBAN Ready]

---

## Step 3: Interactive Priority Setting

### Question: Next Week Priorities

> "Based on this, what are your TOP 3-5 priorities for next week?"
>
> *Suggested priorities (from data):*
> 1. [Overdue item — catch up]
> 2. [Due this week item]
> 3. [High priority item]
>
> - **Accept suggestions** — use recommended priorities
> - **Modify list** — "Here's what I want to focus on instead"
> - **Mix** — "Keep 1 and 3, replace 2"

### Question: Next Actions

> "What are the specific NEXT ACTIONS for each priority?"
>
> For each priority, identify:
> - The very next physical action
> - Any blockers to address first
>
> Example:
> - Priority: "Finish project proposal"
> - Next action: "Draft executive summary section"

### Question: Monthly Outlook (Optional)

> "Looking at the month ahead, anything big coming up?"
>
> *Check for:*
> - Tasks due this month
> - Known deadlines
> - Planned events
>
> - **Yes, let's plan** — discuss monthly priorities
> - **Skip for now** — focus on the week

---

## Step 4: Generate Planning Sections

### Next Week Priorities (3-5)

```markdown
## Next Week Priorities (3-5)
- [ ] [Priority 1] — [brief context]
- [ ] [Priority 2]
- [ ] [Priority 3]
- [ ] [Priority 4] (if applicable)
- [ ] [Priority 5] (if applicable)
```

Format guidelines:
- Start with action verb
- Include outcome, not just activity
- Add context in em-dash suffix if helpful
- Keep to 3-5 items max (focus)

### Next Actions

```markdown
## Next Actions
- [ ] [Specific next action for Priority 1]
- [ ] [Specific next action for Priority 2]
- [ ] [Specific next action for Priority 3]
- [ ] [Any standalone quick wins identified]
```

Format guidelines:
- Physical, concrete actions
- Can be done without further planning
- Include context if action is unclear standalone

### Monthly Outlook (if discussed)

```markdown
## Monthly Outlook
**Key dates:**
- [Date]: [Event/deadline]

**Focus areas:**
- [Theme 1]
- [Theme 2]

**Watch out for:**
- [Potential blocker or risk]
```

---

## Step 5: Sync Recommendations

After planning, optionally suggest:

> "Want me to sync these priorities to Todoist?"
>
> - **Yes** — Create/update tasks in PersonalOS Ready section
> - **No** — Keep in review document only

If yes:
- Add new priority tasks to Todoist Ready section
- Set due dates for next week items
- Add labels if applicable

---

## Planning Principles

### Good Priorities
- Outcome-focused: "Ship feature X" not "Work on feature X"
- Realistic: 3-5 items is enough for a week
- Balanced: Mix of must-do and want-to-do

### Good Next Actions
- Specific: "Email John about timeline" not "Follow up"
- Actionable: Can be done without more planning
- Small: Under 2 hours typically

### Avoid
- Vague items: "Make progress on project"
- Too many priorities: More than 5 = no priorities
- Missing actions: Priorities without clear next steps

---

## Output

Return these sections to the review cookbook for insertion:

```yaml
next_week_priorities:
  - priority: "..."
    context: "..."
  - priority: "..."
    context: "..."

next_actions:
  - action: "..."
    related_priority: "..."
  - action: "..."

monthly_outlook: # optional
  key_dates: [...]
  focus_areas: [...]
  risks: [...]

sync_to_todoist: true/false
```

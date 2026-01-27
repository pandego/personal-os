# Week Review Questions

Interactive questions for the weekly review workflow. Use with `AskUserQuestion` tool.

---

## Input Questions

### Input Source
```yaml
question: "Do you have notes or a transcript to include?"
header: "Input"
options:
  - label: "Yes, file path"
    description: "I'll point you to the file"
  - label: "Yes, paste it"
    description: "I'll paste or dictate my notes"
  - label: "No, just data"
    description: "Build from Todoist + KANBAN only"
multiSelect: false
```

### Date Range (if no previous review found)
```yaml
question: "I couldn't find a previous week review. What date range should I cover?"
header: "Date range"
options:
  - label: "Last 7 days"
    description: "Standard week"
  - label: "Since last Monday"
    description: "Current calendar week"
  - label: "Custom"
    description: "I'll specify a start date"
multiSelect: false
```

---

## Review Questions

### Q1: Validate Accomplishments
```yaml
question: "I found [X] completed tasks. Anything missing or incorrect?"
header: "Verify"
options:
  - label: "Looks good"
    description: "The list is accurate"
  - label: "Add more"
    description: "I accomplished more things"
  - label: "Remove some"
    description: "Some weren't actually completed"
multiSelect: false
```

**Follow-up if "Add more":** Free text — "What else did you accomplish?"

### Q2: Highlights
```yaml
question: "What were the TOP 2-3 highlights of your week?"
header: "Highlights"
options:
  - label: "Use suggestions"
    description: "Accept the highlights I identified from data"
  - label: "Different highlights"
    description: "I'll tell you what stood out"
multiSelect: false
```

**Follow-up if "Different":** Free text — "What were your highlights?"

### Q3: Goals & Outcomes (if previous review exists)
```yaml
question: "Last week you planned these priorities. Does this assessment look right?"
header: "Goals"
options:
  - label: "Accurate"
    description: "The status tracking is correct"
  - label: "Add context"
    description: "Let me explain what happened"
multiSelect: false
```

**Follow-up if "Add context":** Free text per unfinished goal

### Q4: What Went Well
```yaml
question: "What went particularly well this week?"
header: "Went well"
# Free text response
# Prompts to consider:
# - Processes that worked
# - Habits that helped
# - Collaborations that clicked
# - Decisions you're glad you made
```

### Q5: What Didn't Go Well
```yaml
question: "What didn't go as planned?"
header: "Challenges"
# Free text response
# Prompts to consider:
# - Tasks that slipped
# - Blockers encountered
# - Time sinks
# - Distractions
```

### Q6: Blockers
```yaml
question: "Any blockers or challenges that impacted your week?"
header: "Blockers"
options:
  - label: "Yes, blockers"
    description: "I encountered obstacles"
  - label: "No blockers"
    description: "Week went smoothly"
multiSelect: false
```

**Follow-up if "Yes":** For each blocker:
- What was the blocker?
- What was its impact?
- Is it resolved? If not, what's needed?

### Q7: Learnings
```yaml
question: "What did you learn this week?"
header: "Learnings"
options:
  - label: "Share learnings"
    description: "I have insights to capture"
  - label: "Nothing notable"
    description: "Skip this section"
multiSelect: false
```

**Follow-up if "Share":** Free text — list 1-3 learnings

---

## Planning Questions

### Q8: Next Week Priorities
```yaml
question: "Based on active tasks, what are your TOP 3-5 priorities for next week?"
header: "Priorities"
options:
  - label: "Accept suggestions"
    description: "Use the recommended priorities from data"
  - label: "Modify list"
    description: "I have different priorities"
  - label: "Mix"
    description: "Keep some suggestions, change others"
multiSelect: false
```

### Q9: Next Actions
```yaml
question: "What are the specific NEXT ACTIONS for your top priorities?"
header: "Actions"
# Free text — concrete, physical actions for each priority
```

### Q10: Todoist Sync (optional)
```yaml
question: "Want me to sync these priorities to Todoist?"
header: "Sync"
options:
  - label: "Yes"
    description: "Create/update tasks in Todoist Ready section"
  - label: "No"
    description: "Keep in review document only"
multiSelect: false
```

---

## Question Flow

1. Input source (Q0)
2. Date range if needed (Q0b)
3. Validate accomplishments (Q1)
4. Highlights (Q2)
5. Goals tracking if previous review (Q3)
6. What went well (Q4)
7. What didn't go well (Q5)
8. Blockers (Q6)
9. Learnings (Q7)
10. Next week priorities (Q8)
11. Next actions (Q9)
12. Todoist sync (Q10)

**Total: 7-10 questions depending on context**

# Week Review Questions

Interactive questions for the weekly review workflow. Use with `AskUserQuestion`.

---

## Input Questions

### Input Source
```yaml
question: "Do you have notes or material to include?"
header: "Input"
options:
  - label: "Yes, file path"
    description: "I'll point you to the file"
  - label: "Yes, paste it"
    description: "I'll paste or dictate my notes"
  - label: "No, just workspace data"
    description: "Build from what is already in this folder"
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

### Q1: Validate Highlights
```yaml
question: "I found a few likely highlights from your week. Does this feel right?"
header: "Highlights"
options:
  - label: "Looks good"
    description: "The summary feels accurate"
  - label: "Add more"
    description: "There are more important things to include"
  - label: "Change it"
    description: "The emphasis is off"
multiSelect: false
```

### Q2: What Went Well
```yaml
question: "What went especially well this week?"
header: "Went well"
```

### Q3: What Didn't Go Well
```yaml
question: "What did not go as planned?"
header: "Challenges"
```

### Q4: Blockers
```yaml
question: "Any blockers or friction points worth capturing?"
header: "Blockers"
options:
  - label: "Yes"
    description: "There were obstacles"
  - label: "No"
    description: "Nothing major"
multiSelect: false
```

### Q5: Learnings
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

### Q6: Next Week Priorities
```yaml
question: "What are your top priorities for next week?"
header: "Priorities"
options:
  - label: "Use suggestions"
    description: "Start from the suggested priorities"
  - label: "I have my own"
    description: "I'll define them"
  - label: "Mix both"
    description: "Keep some suggestions and change others"
multiSelect: false
```

### Q7: Next Actions
```yaml
question: "What are the next concrete actions for those priorities?"
header: "Actions"
```

---

## Question Flow

1. Input source
2. Date range if needed
3. Validate highlights
4. What went well
5. What didn't go well
6. Blockers
7. Learnings
8. Next week priorities
9. Next actions

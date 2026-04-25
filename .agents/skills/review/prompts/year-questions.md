# Year Review Questions

Interactive questions for the yearly review workflow. Use with `AskUserQuestion` tool.

The year review is primarily driven by user reflection, not automated data. These questions guide the user through structured introspection.

---

## Input Questions

### Input Source
```yaml
question: "Do you have notes, journals, or a transcript to reference?"
header: "Input"
options:
  - label: "Yes, file path"
    description: "I'll point you to the file"
  - label: "Yes, paste it"
    description: "I'll paste or share notes"
  - label: "No, let's reflect together"
    description: "I'll answer questions from memory"
multiSelect: false
```

### Year to Review
```yaml
question: "Which year are we reviewing?"
header: "Year"
options:
  - label: "Previous year"
    description: "Review the year that just ended"
  - label: "Current year"
    description: "Mid-year or end-of-year review"
  - label: "Specific year"
    description: "I'll specify which year"
multiSelect: false
```

---

## REVIEW Section Questions

### Q1: Overall Theme
```yaml
question: "If you had to describe this year in one phrase or theme, what would it be?"
header: "Theme"
# Free text — examples:
# - "The year of foundations"
# - "Grinding through uncertainty"
# - "Breakthrough and growth"
```

### Q2: What Went Well
```yaml
question: "What went well this year? Think about career, relationships, health, personal growth."
header: "Wins"
# Free text — list 3-5 things
```

### Q3: What Went Badly
```yaml
question: "What didn't go as planned or was disappointing?"
header: "Challenges"
# Free text — list 3-5 things
# Be honest — this is for learning
```

### Q4: Why & Lessons
```yaml
question: "Looking at what went badly — why did those things happen? What lessons did you learn?"
header: "Lessons"
# Free text — connect challenges to insights
```

### Q5: Habits & Systems
```yaml
question: "What habit or system had the biggest positive impact? What patterns hurt you most?"
header: "Systems"
# Free text:
# - Positive system that worked: ...
# - Negative pattern to change: ...
```

### Q6: Valuable Time
```yaml
question: "What are the most valuable ways you spent your time this year?"
header: "Value"
# Free text — activities with highest ROI
```

### Q7: Happiness
```yaml
question: "What brought you the most happiness this year?"
header: "Joy"
# Free text — moments, activities, people
```

### Q8: People
```yaml
question: "Who are the people that had the greatest impact on you this year?"
header: "People"
# Free text — list key relationships
```

### Q9: Unfinished Goals
```yaml
question: "What did you expect to complete this year but didn't?"
header: "Unfinished"
# Free text — list incomplete goals
# Follow-up: Are these still important?
```

### Q10: Time Waste
```yaml
question: "What are the least valuable ways you spent your time?"
header: "Waste"
# Free text — identify time sinks
```

### Q11: Priority Shifts
```yaml
question: "How have your goals or priorities shifted over the year?"
header: "Shifts"
# Free text — what changed and why
```

---

## MEMORIES Section Questions

### Q12: Memorable Moments
```yaml
question: "Let's capture some memories. Which categories do you want to fill in?"
header: "Memories"
options:
  - label: "Quick favorites"
    description: "Just the highlights (5-6 questions)"
  - label: "Full memories"
    description: "Go through all categories"
  - label: "Skip memories"
    description: "Focus on review and planning"
multiSelect: false
```

**If "Quick favorites":**
- Best surprise?
- Coolest new experience?
- Favourite day?
- Favourite quote or insight?
- Most intense week?

**If "Full memories":** Go through template categories one by one.

---

## PLAN Section Questions

### Q13: Future Self
```yaml
question: "What would you do this year if you wanted to make 85-year-old you miserable?"
header: "Anti-goals"
# Free text — identify what to avoid
```

### Q14: 85-Year-Old Wishes
```yaml
question: "What would 85-year-old you wish you did more of?"
header: "Priorities"
# Free text — long-term perspective
```

### Q15: Daily Patterns
```yaml
question: "What makes your days go great? What makes them go terribly?"
header: "Patterns"
# Free text:
# - Great days have: ...
# - Terrible days have: ...
```

### Q16: Productivity Illusions
```yaml
question: "What do you think is productive but isn't? What is productive that you don't realize?"
header: "Illusions"
# Free text — challenge assumptions
```

### Q17: Time Allocation
```yaml
question: "What do you want to do more of? Less of?"
header: "Time"
# Free text:
# - More: ...
# - Less: ...
```

### Q18: Ideal Day
```yaml
question: "What does an ideal normal day look like? Write it out."
header: "Ideal day"
# Free text — describe hour by hour if helpful
```

### Q19: Conversations
```yaml
question: "What conversations do you need to have?"
header: "Conversations"
# Free text — difficult or important talks
```

### Q20: Habits
```yaml
question: "What habits are you committing to starting and stopping?"
header: "Habits"
# Free text:
# - START: ...
# - STOP: ...
```

---

## FINAL THOUGHTS Questions

### Q21: Success Definition
```yaml
question: "What would have to happen by the end of next year for you to consider it a success?"
header: "Success"
# Free text — define concrete outcomes
```

### Q22: Identity
```yaml
question: "Who do you need to become for next year to turn out the way you want?"
header: "Identity"
# Free text — character traits, behaviors
```

### Q23: Advice
```yaml
question: "What advice would you give yourself 12 months ago? (You probably still need to hear it)"
header: "Advice"
# Free text — wisdom for future self
```

---

## Question Flow

**Phase 1: Input (2 questions)**
1. Input source
2. Year to review

**Phase 2: Review (11 questions)**
3. Overall theme (Q1)
4. What went well (Q2)
5. What went badly (Q3)
6. Why & lessons (Q4)
7. Habits & systems (Q5)
8. Valuable time (Q6)
9. Happiness (Q7)
10. People (Q8)
11. Unfinished goals (Q9)
12. Time waste (Q10)
13. Priority shifts (Q11)

**Phase 3: Memories (1-16 questions)**
14. Memories scope (Q12)
15. Memory categories based on scope

**Phase 4: Plan (8 questions)**
16. Anti-goals (Q13)
17. 85-year-old wishes (Q14)
18. Daily patterns (Q15)
19. Productivity illusions (Q16)
20. Time allocation (Q17)
21. Ideal day (Q18)
22. Conversations (Q19)
23. Habits (Q20)

**Phase 5: Final Thoughts (3 questions)**
24. Success definition (Q21)
25. Identity (Q22)
26. Advice (Q23)

**Total: 15-25 questions depending on memories scope**

---

## Notes

- Year review is reflection-heavy, data-light
- Data supplements user input, doesn't replace it
- Allow user to skip sections if review is time-constrained
- Can be done across multiple sessions

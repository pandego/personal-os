# Cookbook: Year Review

Generate a comprehensive yearly retrospective through guided reflection.

**Input:** Data package from `gather-data.md` (year scope)
**Output:** Completed year review file

---

## Data Gathering (Year Scope)

Before interactive flow, ensure gather-data.md collected:

1. **All week reviews from the year** — `3-personal/01-week-reviews/02-done/*{YEAR}*.md`
2. **Completed tasks for entire year** — Todoist `find-completed-tasks` with year range
3. **Published content** — `1-content/*/03-published/`
4. **Client work** — `2-business/02-clients/`
5. **Previous year review** — for goal tracking

---

## Interactive Flow (8-10 Questions)

Year reviews are more comprehensive. Guide the user through reflection.

### Question 1: Overall Theme

> "If you had to describe this year in one phrase or theme, what would it be?"
>
> *Examples:*
> - "The year of foundations"
> - "Grinding through uncertainty"
> - "Breakthrough and growth"
>
> - **Enter theme** — free text

### Question 2: Validate Big Accomplishments

Present gathered data:

> "Based on your data, here are the major accomplishments I found:"
>
> **Content Published:** X blog posts, Y LinkedIn posts
> **Client Projects:** [list]
> **Tasks Completed:** N total across all projects
>
> "What were your TOP 5 accomplishments this year?"
>
> - **Use suggestions + add** — combine data with personal highlights
> - **Different list** — override with your own

### Question 3: Goals Review

If previous year review exists:

> "Last year you set these priorities for this year:"
> 1. [Goal 1] → Achieved / Partial / Not achieved
> 2. [Goal 2] → ...
>
> "Let's assess each one. What happened?"

If no previous review:

> "What goals did you have for this year? How did they turn out?"

### Question 4: What Went Well

> "What went really well this year?"
>
> *Categories to consider:*
> - Career/Business
> - Relationships
> - Health/Wellbeing
> - Personal growth
> - Habits/Systems
>
> - **List 3-5 wins** — by category or overall

### Question 5: What Didn't Go Well

> "What didn't go as planned or was disappointing?"
>
> *Be honest — this is for learning:*
> - Goals missed
> - Projects abandoned
> - Relationships neglected
> - Health setbacks
>
> - **List 3-5 challenges** — free text

### Question 6: Key Learnings

> "What are the most important things you learned this year?"
>
> *Can include:*
> - Professional skills
> - Personal insights
> - Life lessons
> - Things you'd do differently
>
> - **List 3-5 learnings**

### Question 7: Habits & Systems

> "What habit or system had the biggest positive impact? What hurt you most?"
>
> - **Positive system:** ...
> - **Negative pattern:** ...

### Question 8: Memorable Moments

> "Let's capture some memories. What stands out?"
>
> *Quick hits:*
> - Best surprise?
> - Favorite experience?
> - Most intense week?
> - Best new relationship?
>
> - **Share memories** — brief answers for each

### Question 9: Next Year Vision

> "What would have to happen next year for you to consider it a success?"
>
> - **Define success** — 2-3 concrete outcomes

### Question 10: Theme for Next Year

> "What word or theme do you want to guide next year?"
>
> - **Choose theme** — one word or phrase

---

## Generate Review

### Read Template

```
Read: .claude/skills/review/templates/year-review.md
```

Use this as the template for structure and format.

### Read Questions

```
Read: .claude/skills/review/prompts/year-questions.md
```

Follow the question flow defined there. Year review is reflection-heavy, data-light — user input drives the content.

### Populate Sections

Map question responses to template sections:

```markdown
# Year Review YYYY

## A Retrospective of the Good, the Bad, and the Blah

[Intro text from template]

## REVIEW

### How has this year gone?
- [From Question 1 theme]

### What went well?
- [From Question 4]

### What went badly?
- [From Question 5]

#### Why?
- [Analysis from Question 5 context]

#### What lessons did I learn?
- [From Question 6]

### What habit or system accounted for most of my success?
- [From Question 7 - positive]

### What are the most valuable ways I spend my time?
- [Inferred from accomplishments + learnings]

### What brought me the most happiness?
- [From Question 8 memories + Question 4 wins]

### Who are the people that had the greatest impact on me?
- [From Question 8 or ask if not mentioned]

### What did I expect to complete, but didn't?
- [From Question 3 - not achieved goals]

### What are the least valuable ways I am spending my time?
- [From Question 7 - negative pattern]

## MEMORIES

[From Question 8 responses - map to template categories]

## PLAN

### What would I do this year if I wanted to make 85 year old me miserable?
- [Invert from Question 7 negative patterns]

### What would 85 year old me wish I did more of?
- [From Question 4 + 9]

[Continue mapping...]

## FINAL THOUGHTS

### What would have had to have happened by the end of next year...
- [From Question 9]

### Who do I need to become...
- [From Question 10 theme]

### Knowing what I know now, what advice would I give...
- [From Question 6 learnings]

## MISCELLANEOUS NOTES & REFLECTIONS
- [Any additional transcript content]
```

---

## Data Appendix

Include a data summary at the end:

```markdown
---

## Year in Numbers

### Content
- Blog posts published: X
- LinkedIn posts: Y
- Tweets: Z

### Tasks
- Total completed: N
- By project: [breakdown]

### Business
- Clients served: X
- Projects delivered: Y

### Reviews
- Week reviews completed: X/52

*Data sourced from Todoist + KANBAN + content folders*
```

---

## Output

Write to: `3-personal/02-year-reviews/02-done/YYYY_year-review.md`

Example: `2025_year-review.md` for reviewing year 2025

---

## Timing Notes

Best times for year review:
- Late December (while year is fresh)
- Early January (with slight distance)
- Can split across multiple sessions — save draft to `01-drafts/`

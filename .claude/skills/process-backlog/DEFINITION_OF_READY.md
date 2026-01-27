# Definition of Ready (DoR)

A task is **Ready** when it can be started without further clarification. This standard ensures tasks are actionable, scoped, and verifiable.

## DoR Criteria

Every Ready task MUST have:

### 1. Clear Objective
Single sentence starting with a verb. What are we doing?

### 2. Acceptance Criteria
2-5 bullets defining "done". How do we know it's complete?

### 3. Scope Boundary
What's explicitly OUT of scope. Prevents creep.

### 4. Prerequisites
What must exist before starting. Blockers identified upfront.

### 5. Complexity
- **Small**: <1 hour, single file/concept
- **Medium**: 1-4 hours, multiple files, some unknowns
- **Large**: 4+ hours, architectural decisions, needs breakdown

---

## Task Format

```markdown
- [ ] [Verb] [objective in one sentence]
    **Criteria:**
    - [ ] [Measurable outcome 1]
    - [ ] [Measurable outcome 2]
    **Scope:** [What's NOT included]
    **Prerequisites:** [What must exist first]
    **Complexity:** [Small/Medium/Large]
    #[domain-tag]
```

---

## Quick Reference

| Question | If No → |
|----------|---------|
| Can someone start this immediately? | Needs clarification |
| Will two people interpret this the same way? | Needs specifics |
| Is "done" measurable? | Needs acceptance criteria |
| Are boundaries clear? | Needs scope definition |
| Are blockers identified? | Needs prerequisites |

---

## When to Simplify

Not every task needs full DoR. Use judgment:

- **Simple/obvious tasks**: Just need clear objective + done criteria
  - "Add `.env` to gitignore" → obvious scope, no prereqs needed
- **Complex/ambiguous tasks**: Need full DoR
  - "Build voice agent" → needs all criteria specified

The goal is actionability, not bureaucracy.

# Cookbook: Process to Ready

Transform messy backlog items into DoR-compliant Ready tasks.

**References:**
- `../DEFINITION_OF_READY.md` — criteria for Ready tasks
- `../ANTI_PATTERNS.md` — validation rules

---

## Workflow

### 1. Load KANBAN.md

Read `KANBAN.md` from project root.

**If missing:** Ask user:
> "`KANBAN.md` not found. Create it from template? (yes/no)"

If yes: copy from `assets/KANBAN_template.md`

### 2. Extract Backlog Items

Find all items under `## Backlog` section.

**If empty:**
> "No items in backlog to process!"

### 3. Process Each Item

For each backlog item:

#### 3a. Assess Clarity

**Clear enough?** Can be processed directly if:
- Intent is obvious
- Single action/goal
- Scope is implicit but reasonable

→ Go to Step 3b

**Unclear?** Needs clarification if:
- Ambiguous intent
- Multiple possible interpretations
- Missing critical context

→ **Dispatch to `clarify.md`**

#### 3b. Extract Core Intent

1. **Remove noise**: "um", "like", "you know", repetition, transcription artifacts
2. **Identify verb**: What action is being requested?
3. **Identify object**: What is being acted upon?
4. **Identify outcome**: What does "done" look like?

#### 3c. Check Complexity

- **Simple task** (add to gitignore, fix typo): Minimal DoR
- **Complex task** (build feature, refactor system): Full DoR

#### 3d. Format as DoR Task

**Simple task format:**
```markdown
- [ ] [Verb] [objective]
    **Done when:** [measurable outcome]
    #[domain-tag]
```

**Full DoR format:**
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

#### 3e. Validate Against Anti-Patterns

Check `../ANTI_PATTERNS.md`:
- [ ] Starts with verb
- [ ] Has acceptance criteria
- [ ] Scope is bounded
- [ ] Has domain tag
- [ ] Single goal (not nested)

If validation fails → fix before moving to Ready.

### 4. Split If Needed

One messy item may contain multiple tasks. Split into separate Ready items.

**Signals to split:**
- "and also..."
- Multiple distinct actions
- Unrelated goals combined

### 5. Move to Ready

- Remove processed item from `## Backlog`
- Add formatted task to `## Ready`

### 6. Track Changes

Maintain list of:
- Items processed
- Items split (and into what)
- Items sent to clarification

---

## Domain Tags

Use consistent tags:

| Tag | Domain |
|-----|--------|
| `#blog-idea` | Blog content |
| `#linkedin-idea` | LinkedIn content |
| `#tweet-idea` | Twitter/X content |
| `#youtube-idea` | YouTube content |
| `#repo-improvement` | PersonalOS codebase |
| `#business-task` | Client/portfolio work |
| `#personal-task` | Personal items |

---

## Output

After processing, return:
- Count of items processed
- List of Ready tasks created
- Any items needing clarification

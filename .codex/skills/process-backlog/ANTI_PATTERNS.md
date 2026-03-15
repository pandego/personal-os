# Anti-Patterns

Validation rules for task quality. A task failing any of these should not move to Ready.

---

## 1. Vague Objective

**Problem:** Task doesn't start with a clear action verb.

**Detect:**
- Starts with noun ("Voice agent")
- Starts with adjective ("Better error handling")
- No clear action ("The login thing")

**Fix:** Rewrite to start with verb (Create, Add, Fix, Update, Research, Implement, Refactor, etc.)

| Bad | Good |
|-----|------|
| "Voice agent" | "Create voice agent skill for TTS" |
| "Better errors" | "Improve error messages in auth flow" |
| "The login thing" | "Fix login redirect bug" |

---

## 2. Missing Acceptance Criteria

**Problem:** No way to know when task is "done".

**Detect:**
- No "Done when" or "Criteria" section
- Criteria are subjective ("make it better")
- Criteria are unmeasurable ("improve performance")

**Fix:** Add 2-5 specific, measurable outcomes.

| Bad | Good |
|-----|------|
| "Improve performance" | "Reduce API response time to <200ms" |
| "Make it better" | "Pass all linting rules, 100% test coverage" |
| "Clean up code" | "Extract 3 functions, remove dead code" |

---

## 3. Unbounded Scope

**Problem:** Task has no clear boundaries, invites scope creep.

**Detect:**
- Uses words like "all", "everything", "fully"
- No explicit exclusions
- Could expand indefinitely

**Fix:** Add explicit scope boundary stating what's NOT included.

| Bad | Good |
|-----|------|
| "Build auth system" | "Add JWT auth; OAuth and SSO out of scope" |
| "Improve all tests" | "Add tests for auth module only" |
| "Refactor everything" | "Refactor user service; leave API layer unchanged" |

---

## 4. No Domain Tag

**Problem:** Task can't be categorized or filtered.

**Detect:**
- Missing `#tag` at end of task
- Tag doesn't match known domains

**Fix:** Add appropriate domain tag.

Valid tags:
- `#blog-idea`, `#linkedin-idea`, `#tweet-idea`, `#youtube-idea`
- `#repo-improvement`
- `#business-task`
- `#personal-task`

---

## 5. Nested Goals

**Problem:** Single task contains multiple unrelated goals.

**Detect:**
- Contains "and also"
- Multiple verbs for different objects
- Would require context switching to complete

**Fix:** Split into separate tasks.

| Bad | Good |
|-----|------|
| "Add auth and fix the UI bug" | Task 1: "Add auth" / Task 2: "Fix UI bug" |
| "Research APIs and implement caching" | Task 1: "Research caching APIs" / Task 2: "Implement chosen caching solution" |

---

## 6. Dependency Buried

**Problem:** Prerequisites aren't explicit, task will block.

**Detect:**
- Assumes something exists that doesn't
- References undefined terms
- Requires prior task completion

**Fix:** Add Prerequisites section or complete dependency first.

| Bad | Good |
|-----|------|
| "Deploy to production" | "Prerequisites: Staging tests pass, PR approved" |
| "Use the new API" | "Prerequisites: API endpoint exists (see Task #X)" |

---

## Quick Validation Checklist

Before moving to Ready, verify:

- [ ] Starts with verb
- [ ] Has measurable acceptance criteria
- [ ] Scope is explicitly bounded
- [ ] Has domain tag
- [ ] Single goal only
- [ ] Dependencies are explicit or resolved

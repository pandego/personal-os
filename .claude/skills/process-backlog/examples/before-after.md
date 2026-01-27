# Before → After Examples

Real transformations from messy dictation to DoR-compliant tasks.

---

## Example 1: Rambling Dictation

### Before (Backlog)
```
- [ ] So perhaps I need an inbox that is above everything, so it would be 00 if that makes sense, or use the backlog as the inbox. And then, I don't know, because if you check the inbox there's already board content ideas and then a board for repo backlog. So I think we should have a backlog, that's where we dump anything and then have tasks being created and updated somewhere.
```

### After (Ready)
```
- [ ] Consolidate inbox structure: use KANBAN.md backlog as single inbox
    **Criteria:**
    - [ ] All task capture flows into KANBAN.md Backlog
    - [ ] Content ideas board deprecated or redirected
    - [ ] Repo backlog board deprecated or redirected
    - [ ] Documentation updated to reflect single inbox
    **Scope:** KANBAN.md structure only; Todoist sync unchanged
    **Prerequisites:** None
    **Complexity:** Small
    #repo-improvement
```

---

## Example 2: Vague Idea

### Before (Backlog)
```
- [ ] voice agent thing
```

### After Clarification → (Ready)
```
- [ ] Create voice-agent skill for TTS using ElevenLabs API
    **Criteria:**
    - [ ] Accepts text input up to 5000 characters
    - [ ] Returns MP3 audio file
    - [ ] Supports 3 voice options (configurable)
    - [ ] Error handling for API failures
    **Scope:** TTS only; STT out of scope; no streaming
    **Prerequisites:** ElevenLabs API key in .env
    **Complexity:** Medium
    #repo-improvement
```

---

## Example 3: Multi-Goal Split

### Before (Backlog)
```
- [ ] need to fix the auth bug and also add dark mode and maybe look at performance
```

### After (Ready) — Split into 3 tasks
```
- [ ] Fix authentication redirect bug on login
    **Done when:** Users redirect to dashboard after login (not 404)
    #repo-improvement

- [ ] Add dark mode toggle to settings
    **Criteria:**
    - [ ] Toggle in settings persists to localStorage
    - [ ] Respects system preference as default
    - [ ] All pages support dark theme
    **Scope:** Visual theme only; no accessibility audit
    **Complexity:** Medium
    #repo-improvement

- [ ] Research performance bottlenecks
    **Done when:** Profile report identifies top 3 slowest operations
    **Scope:** Investigation only; fixes are separate tasks
    #repo-improvement
```

---

## Example 4: Simple Task (Minimal DoR)

### Before (Backlog)
```
- [ ] add env to gitignore
```

### After (Ready)
```
- [ ] Add .env to gitignore
    **Done when:** .env file no longer tracked by git
    #repo-improvement
```

---

## Example 5: Content Idea

### Before (Backlog)
```
- [ ] write something about how people misunderstand AI agents, like they think its this magic thing but really its just loops and tools, should probably be a linkedin post
```

### After (Ready)
```
- [ ] Draft LinkedIn post: AI agents demystified (loops + tools, not magic)
    **Criteria:**
    - [ ] Hook: Statement that challenges "magic" perception
    - [ ] Body: Explain loop + tool pattern simply
    - [ ] Takeaway: What this means for practitioners
    - [ ] Under 1300 characters
    **Scope:** LinkedIn only; blog version is separate task
    **Prerequisites:** None
    **Complexity:** Small
    #linkedin-idea
```

---

## Example 6: Needs Clarification (Kept in Backlog)

### Before (Backlog)
```
- [ ] the thing with the API
```

### After Clarification Attempt
```
Asked: "What API thing? Options: fix a bug, add endpoint, integrate external API, other"
User: "I don't remember, skip it"
```

### Result
```
Kept in Backlog (unchanged) — revisit when user remembers context
```

---

## Pattern Summary

| Input Type | Action |
|------------|--------|
| Clear but messy | Clean up, format, move to Ready |
| Vague but answerable | Ask user via clarify.md, then format |
| Multiple goals | Split into separate tasks |
| Too unclear | Keep in Backlog, note clarification attempt |
| Simple/obvious | Minimal DoR (just Done when) |

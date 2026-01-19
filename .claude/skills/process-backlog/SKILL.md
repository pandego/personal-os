---
name: process-backlog
description: Bidirectional sync between KANBAN.md and Todoist PersonalOS project. Processes messy backlog items into clear, actionable tasks. Triggers on requests to sync todoist, process backlog, or when user mentions syncing tasks/ideas.
---

# Process Backlog

Processes messy backlog items (often dictated, rambling notes) into clear, actionable tasks. Optionally syncs with Todoist.

## Trigger Phrases

- `/process-backlog`
- "process my backlog"
- "clean up my backlog"
- "sync my todoist"
- "sync my tasks"

## Workflow

### Step 1: Ask About Scope

> "Want me to sync with Todoist too, or just process the local KANBAN.md?"
>
> - **Both** — sync from Todoist, process backlog, sync back
> - **Local only** — just process KANBAN.md backlog

### Step 2: If Syncing with Todoist

#### 2a. Find PersonalOS Project

Use `mcp__todoist__find-projects` to search for "PersonalOS".

**If not found:**
> "I couldn't find a 'PersonalOS' project in Todoist. Create one with board view and try again."

Stop here.

#### 2b. Get Todoist Sections

Use `mcp__todoist__find-sections` with the project ID.

Expected sections (create if missing with `mcp__todoist__add-sections`):
- Backlog
- Ready
- In Progress
- Done
- Abandoned (optional)

#### 2c. Pull Tasks from Todoist

Use `mcp__todoist__find-tasks` to get all tasks from PersonalOS.

For each task in Todoist not in local KANBAN.md:
- Add to the matching section in KANBAN.md
- Keep track of Todoist task IDs for later cleanup

### Step 3: Process Backlog Items

Ensure `KANBAN.md` exists locally before processing:

- If missing: prompt the user — "`KANBAN.md` not found. Create it from `.claude/skills/process-backlog/assets/KANBAN_template.md` now? (yes/no)".
  - If yes: create `KANBAN.md` from the template and continue.
  - If no: stop and tell the user to create `KANBAN.md` first.

Read `KANBAN.md` and find all items under `## Backlog`.

For each item:

1. **Understand** what the messy/dictated text is trying to say
2. **Extract** the core idea or action
3. **Reformat** into a clear, concise task:
   - Start with a verb (Create, Fix, Add, Update, Research, etc.)
   - Keep it to 1-2 sentences max
   - Remove filler words, repetition, transcription artifacts
4. **Categorize** if obvious (content idea, repo improvement, business task, etc.)

**Example transformation:**

Before (messy dictation):
```
- [ ] - So perhaps I need an inbox that is above everything, so it would be 00 if that makes sense, or use the backlog as the inbox. And then, I don't know, because if you check the inbox there's already board content ideas and then a board for repo backlog. So I think we should have a backlog, that's where we dump anything and then have tasks being created and updated somewhere.
```

After (processed):
```
- [ ] Consolidate inbox structure: use KANBAN.md backlog as single inbox, remove separate content/repo boards:
    1. Review current inbox locations (KANBAN.md, content ideas board, repo backlog)
    2. Decide on single source of truth
    3. Migrate existing items to KANBAN.md backlog
    4. Remove deprecated boards
#repo-improvement
```

**Format notes:**
- Add relevant tags at the beginning (e.g., `#blog-idea`, `#linkedin-idea`, `#repo-improvement`, `#business-task`)
- For multi-step tasks, add numbered steps

### Step 4: Move to Ready

After processing each backlog item:
- Remove from `## Backlog`
- Add processed version to `## Ready`

### Step 5: If Syncing with Todoist

#### 5a. Clean Up Todoist Backlog

For tasks that were pulled from Todoist Backlog and processed:
- Use `mcp__todoist__delete-object` with type "task" to remove them from Todoist Backlog
- These tasks will be re-added to Todoist Ready in the next step

#### 5b. Push All Ready Items to Todoist

For each item in local Ready:
- Check if it exists in Todoist Ready section
- If not, use `mcp__todoist__add-tasks` with the Ready section ID
- This ensures complete bidirectional sync

#### 5c. Sync Other Sections

For items in local "In Progress":
- Ensure they exist in Todoist "In Progress" section

For completed items (in Done):
- Use `mcp__todoist__complete-tasks` if not already completed in Todoist

#### 5d. Final Verification

After sync, verify that:
- Todoist Backlog section has same count as local Backlog (should be 0 after processing)
- Todoist Ready section has same count as local Ready
- If counts don't match, report the discrepancy to the user

#### 5e. Update Last Sync

Update the frontmatter in KANBAN.md:
```yaml
last-sync: YYYY-MM-DD HH:MM
```

### Step 6: Show Summary

> "**Backlog processed!**
>
> **Processed X items:**
> - [processed item 1]
> - [processed item 2]
>
> **Ready (Y items):**
> - [item 1]
> - [item 2]
>
> **In Progress (Z items):**
> - [item 1]
>
> ---
> Last sync: YYYY-MM-DD HH:MM" *(if synced)*

After showing the summary, ask: "Want to tackle something in Ready now? (yes/no). If yes, which item?" If the user picks one, follow their instructions for that item.

## Processing Guidelines

When reformatting messy items:

1. **Preserve intent** — don't lose the original idea
2. **Be concise** — 1-2 sentences max
3. **Start with a verb** — makes it actionable
4. **Remove noise** — "um", "like", "you know", repetition, transcription errors
5. **Split if needed** — one messy item might contain multiple tasks
6. **Ask if unclear** — if you can't understand the intent, ask the user

## Error Handling

- **Todoist MCP not connected**: "Run `/mcp` and connect the Todoist server first"
- **PersonalOS project missing**: "Create a 'PersonalOS' project in Todoist with board view"
- **Empty backlog**: "No items in backlog to process!"

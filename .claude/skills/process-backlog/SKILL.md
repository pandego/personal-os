---
name: process-backlog
description: Bidirectional sync between KANBAN.md and Todoist PersonalOS project. Processes messy backlog items into clear, actionable tasks. Triggers on requests to sync todoist, process backlog, or when user mentions syncing tasks/ideas.
---

# Process Backlog

Router for backlog processing workflows. Dispatches to specialized cookbooks.

## Trigger Phrases

- `/process-backlog`
- "process my backlog"
- "clean up my backlog"
- "sync my todoist"
- "sync my tasks"

---

## Routing Flow

### Step 1: Ask Scope

> "Want me to sync with Todoist too, or just process the local KANBAN.md?"
>
> - **Both** — sync from Todoist, process backlog, sync back
> - **Local only** — just process KANBAN.md backlog

### Step 2: Execute

```
IF scope = "Both":
    → Read cookbook/sync.md
    → Execute PULL phase
    → Read cookbook/process-to-ready.md
    → Execute processing
    → Read cookbook/sync.md
    → Execute PUSH phase

IF scope = "Local only":
    → Read cookbook/process-to-ready.md
    → Execute processing
```

### Step 3: Handle Unclear Items

```
IF item is unclear during processing:
    → Read cookbook/clarify.md
    → Execute clarification workflow
    → Return to processing with clarified intent
```

---

## Reference Documents

Load these as needed:

| Document | When to Load |
|----------|--------------|
| `DEFINITION_OF_READY.md` | When formatting tasks for Ready |
| `ANTI_PATTERNS.md` | When validating task quality |
| `SYNC_RULES.md` | When resolving state conflicts |
| `examples/before-after.md` | For transformation guidance |

---

## Output

After completion, show summary:

> **Backlog processed!**
>
> **Processed X items:**
> - [item 1]
> - [item 2]
>
> **Ready (Y items):**
> - [item 1]
> - [item 2]
>
> **In Progress (Z items):**
> - [item 1]
>
> **In Review (W items):**
> - [item 1]
>
> ---
> Last sync: YYYY-MM-DD HH:MM *(if synced)*

Then ask:
> "Want to tackle something in Ready now?"

---

## Error Handling

| Error | Response |
|-------|----------|
| KANBAN.md missing | Offer to create from `assets/KANBAN_template.md` |
| Todoist MCP not connected | "Run `/mcp` and connect the Todoist server first" |
| PersonalOS project missing | "Create a 'PersonalOS' project in Todoist with board view" |
| Empty backlog | "No items in backlog to process!" |

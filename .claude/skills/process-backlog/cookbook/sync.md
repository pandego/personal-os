# Cookbook: Todoist Sync

Bidirectional sync between KANBAN.md and Todoist PersonalOS project.

**Reference:** See `../SYNC_RULES.md` for state comparison matrix.

---

## Pull from Todoist

### 1. Find PersonalOS Project

```
Use mcp__claude_ai_todoist__find-projects with query "PersonalOS"
```

**If not found:** Stop and tell user:
> "I couldn't find a 'PersonalOS' project in Todoist. Create one with board view and try again."

### 2. Get Sections

```
Use mcp__claude_ai_todoist__find-sections with projectId
```

Expected sections (create if missing with `add-sections`):
- Backlog
- Ready
- In Progress
- In Review
- Done
- Abandoned (optional)

### 3. Get Active Tasks

```
Use mcp__claude_ai_todoist__find-tasks with projectId
```

Returns tasks with their section IDs. Map section ID → section name.

### 4. Get Completed Tasks

```
Use mcp__claude_ai_todoist__find-completed-tasks with projectId
```

**Important:** Completed tasks disappear from board view. This retrieves them for Done sync.

### 5. Merge with Local

For each Todoist task not in local KANBAN.md:
- Determine correct section using Most Advanced State Wins rule
- Add to KANBAN.md in that section
- Track Todoist task ID for later operations

---

## Push to Todoist

### 1. Sync Ready Section

For each item in local Ready:
- Check if exists in Todoist Ready (match by content)
- If not: `mcp__claude_ai_todoist__add-tasks` with Ready section ID

### 2. Sync In Progress Section

For each item in local In Progress:
- Check if exists in Todoist In Progress
- If not: `mcp__claude_ai_todoist__add-tasks` with In Progress section ID
- If exists in earlier section: delete and re-add to In Progress

### 2b. Sync In Review Section

For each item in local In Review:
- Check if exists in Todoist In Review
- If not: `mcp__claude_ai_todoist__add-tasks` with In Review section ID
- If exists in earlier section: delete and re-add to In Review

### 3. Sync Done Section

For items in local Done that are still active in Todoist:
```
Use mcp__claude_ai_todoist__complete-tasks with task IDs
```

### 4. Clean Up Processed Backlog

For Todoist Backlog tasks that were processed to Ready:
```
Use mcp__claude_ai_todoist__delete-object with type "task"
```

These tasks are re-added as Ready items (prevents duplicates).

---

## Verification

After sync, verify counts match:

| Section | Local Count | Todoist Count |
|---------|-------------|---------------|
| Backlog | X | X |
| Ready | Y | Y |
| In Progress | Z | Z |
| In Review | W | W |

If counts don't match, report discrepancy to user.

---

## Update Timestamp

Update KANBAN.md frontmatter:

```yaml
last-sync: YYYY-MM-DD HH:MM
```

---

## Error Handling

| Error | Response |
|-------|----------|
| MCP not connected | "Run `/mcp` and connect the Todoist server first" |
| Project not found | "Create a 'PersonalOS' project in Todoist with board view" |
| Section missing | Create it with `add-sections` |
| Rate limited | Wait and retry |

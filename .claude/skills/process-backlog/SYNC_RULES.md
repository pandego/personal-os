# Sync Rules

## Core Principle: Most Advanced State Wins

Tasks only move forward through the lifecycle:

```
Backlog → Ready → In Progress → In Review → Done → Abandoned
```

**Never regress a task.** If it's Done anywhere, it's Done everywhere.

---

## State Comparison Matrix

When the same task exists in both systems with different states:

| Local State | Todoist State | Action |
|-------------|---------------|--------|
| Done | Ready | Complete in Todoist |
| Done | In Progress | Complete in Todoist |
| Done | In Review | Complete in Todoist |
| Ready | Done | Move to Done locally |
| In Progress | Done | Move to Done locally |
| In Review | Done | Move to Done locally |
| Backlog | Ready | Move to Ready locally |
| Backlog | In Progress | Move to In Progress locally |
| Backlog | In Review | Move to In Review locally |
| Ready | Backlog | Move to Ready in Todoist |
| In Progress | Backlog | Move to In Progress in Todoist |
| In Review | Backlog | Move to In Review in Todoist |
| In Progress | Ready | Move to In Progress in Todoist |
| Ready | In Progress | Move to In Progress locally |
| In Review | Ready | Move to In Review in Todoist |
| In Review | In Progress | Move to In Review in Todoist |
| Ready | In Review | Move to In Review locally |
| In Progress | In Review | Move to In Review locally |

---

## Sync Direction Reference

### Pull (Todoist → Local)
- New tasks in Todoist → Add to matching section locally
- Completed tasks in Todoist → Move to Done locally
- Advanced state in Todoist → Update local to match

### Push (Local → Todoist)
- Processed Ready items → Add to Todoist Ready section
- Local In Progress → Ensure exists in Todoist In Progress
- Local In Review → Ensure exists in Todoist In Review
- Local Done → Complete task in Todoist

---

## Todoist Behavior Notes

- **Completed tasks disappear** from board view but remain stored
- Use `find-completed-tasks` to retrieve them for Done sync
- **Backlog items get deleted** after processing (they're re-added as Ready)

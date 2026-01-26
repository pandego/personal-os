# External Resources

Git submodules for reference repositories.

## Current Submodules

| Submodule | Description |
|-----------|-------------|
| `anthropic-skills/` | Official Anthropic Claude skills examples |
| `obra-superpowers/` | Claude Code superpowers collection by Jesse Vincent |
| `disler-fork-terminal/`    | A skill you can use to fork your agentic coding tools to a new terminal window by IndyDevDan |
| `pandego-parallel-thread-skill/` | A skill that spawns multiple parallel AI agent processes using mcprocs |

## Adding a New Submodule

```bash
git submodule add <repo-url> _external/<name>
```

## Updating Submodules

```bash
git submodule update --remote --merge
```

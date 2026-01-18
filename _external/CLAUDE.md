# External Resources

Git submodules for reference repositories.

## Current Submodules

| Submodule | Description |
|-----------|-------------|
| `anthropic-skills/` | Official Anthropic Claude skills examples |
| `obra-superpowers/` | Claude Code superpowers collection by Jesse Vincent |

## Adding a New Submodule

```bash
git submodule add <repo-url> _external/<name>
```

## Updating Submodules

```bash
git submodule update --remote --merge
```

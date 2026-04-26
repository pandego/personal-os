# System

Infrastructure, docs, and supporting tooling for Personal OS.

## Structure

```text
_system/
├── docs/              # system documentation and guides
├── templates/         # scaffolds for new components (currently empty)
├── scripts/           # Python utility scripts (currently empty)
├── mcp-servers/       # MCP server implementations
└── README_system.md
```

## Folders

### docs/
Explanatory documentation about how the system works.

### templates/
Scaffolds with placeholders for creating new components. Empty for now; add `TEMPLATE_*.md` files here as needed.

### scripts/
Python utility scripts callable via `uv run`. Empty for now. When adding a script, register it under `[project.scripts]` in `pyproject.toml` so it's available as a command:

```bash
uv run <command>
```

### mcp-servers/
MCP server implementations and related setup.

# System

Infrastructure, scripts, and tooling for Personal OS.

## Structure

```text
_system/
├── docs/              # system documentation and guides
├── templates/         # scaffolds for new components
├── scripts/           # Python utility scripts
├── mcp-servers/       # MCP server implementations
└── README_system.md
```

## Folders

### docs/
Explanatory documentation about how the system works.

### templates/
Scaffolds with placeholders for creating new components.

### scripts/
Python utility scripts for system operations. See `scripts/README_scripts.md` for details.

### mcp-servers/
MCP server implementations and related setup.

## Script usage
Scripts are registered in `pyproject.toml` and run as commands:

```bash
uv run <command>
```

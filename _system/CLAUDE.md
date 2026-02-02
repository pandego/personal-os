# System

Infrastructure, scripts, and tooling for Content OS.

## Structure

```
_system/
├── docs/            # System documentation and guides
├── templates/       # Scaffolds for creating new system components
│   └── voice-template.md  # Template for creating new platform voice files
├── scripts/         # Python utility scripts
├── mcp-servers/     # MCP server implementations
└── CLAUDE.md
```

## Folders

### docs/
Explanatory documentation about how the system works:
- Architecture decisions
- How-to guides
- System design docs

### templates/
Actionable scaffolds with placeholders for creating new components:
- `voice-template.md` - For creating new platform voice files
- Future: skill-template.md, command-template.md, etc.

## Scripts
Python utility scripts for system operations. See `scripts/README.md` for details.

### Script Usage
Scripts are registered in `pyproject.toml` and run as commands:
```bash
uv run <command>
```

**Why:** When using Git inside Dropbox (or any cloud storage), multiple computers syncing the same files create "conflicted copy" files. These corrupt Git's internal state and Python environments.

**Available commands:**
- `clean` - Master command: cleans Git conflicts + rebuilds Python environment
- `clean-git` - Clean Dropbox conflicted copies from `.git/`
- `clean-env` - Delete `.venv/` and run `uv sync` to rebuild from scratch

## MCP Servers
MCP servers are configured in root `.mcp.json` and start automatically with Claude Code, or globally in `~/.claude/settings.json`.

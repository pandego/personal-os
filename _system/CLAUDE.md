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
Python utility scripts for system operations.

### Script Usage
Always use uv to run scripts:
```bash
uv run _system/scripts/<script>.py <args>
```

## MCP Servers
MCP servers are configured in root `.mcp.json` and start automatically with Claude Code, or globally in `~/.claude/settings.json`.

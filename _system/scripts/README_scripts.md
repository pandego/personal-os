# Scripts

Python utility scripts for Personal OS, callable via `uv run <command>`.

Currently empty. Add new scripts here as `_system/scripts/<name>.py`, expose a `main()` entrypoint, and register the command in `pyproject.toml`:

```toml
[project.scripts]
my-command = "_system.scripts.my_module:main"
```

Then run with:

```bash
uv run my-command
```

## Conventions

- Use `loguru` for logging (already a dependency).
- Use `uv run` for all execution; never call `python`/`python3` directly.
- Add new dependencies with `uv add <pkg>`. Never hand-edit `pyproject.toml` dependencies.

---
name: setup-repo
description: Interactive setup workflow for Personal OS repository. Use when user explicitly asks to set up the repo, initialize Personal OS, or run first-time setup. Guides through voice configuration, Python environment setup (checking for uv), skill symlinks, and optional Todoist MCP configuration for task/idea sync.
---

# Personal OS Setup

Welcome message:

```
╔══════════════════════════════════════════════════════════════════╗
║                     PERSONAL OS SETUP                            ║
╠══════════════════════════════════════════════════════════════════╣
║  Four steps:                                                     ║
║    1. Voice - How you sound in writing                           ║
║    2. Python - Environment setup                                 ║
║    3. Skills - Symlink external skills                           ║
║    4. Todoist - Task sync (optional)                             ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Step 1: Voice Configuration

```
┌──────────────────────────────────────────────────────────────────┐
│  STEP 1 OF 4: YOUR VOICE                                         │
└──────────────────────────────────────────────────────────────────┘
```

Use AskUserQuestion to gather voice info in batches. Keep questions clear and simple.

### Question Set 1: Identity

Ask: "Let's set up your writing voice. First, the basics:"

Use AskUserQuestion with these questions:
1. **"What's your name?"** (free text - user types "Other")
2. **"What do you do?"** (free text - user types "Other")
3. **"Who do you write for?"** Options:
   - Engineers/developers
   - Founders/entrepreneurs
   - General tech audience
   - (Other for custom)

### Question Set 2: Communication Style

Ask: "Now, how do you like to communicate:"

Use AskUserQuestion with these questions:
1. **"How direct is your writing?"** Options:
   - Very direct - get to the point fast
   - Balanced - some context, then the point
   - Storytelling - build up to the insight

2. **"How formal is your tone?"** Options:
   - Professional but approachable
   - Casual, like talking to a colleague
   - Very casual, conversational

3. **"Emojis in your content?"** Options:
   - Yes, I use them
   - Sparingly
   - Never

4. **"Occasional swearing okay?"** Options:
   - Yes
   - No

5. **"What writing patterns do you want to avoid?"** (multiSelect: true) Options:
   - Corporate jargon ("synergy", "leverage", "ecosystem")
   - Clickbait hooks ("You won't believe...")
   - Over-hedging ("I think maybe perhaps...")
   - Excessive caveats and disclaimers
   - (Other for custom)

### Generate VOICE.md

After gathering answers, read `assets/VOICE_template.md` and generate a filled-in version.

Save to `/VOICE.md` (root of repo).

Confirm: "Voice saved to VOICE.md"

---

## Step 2: Python Environment

```
┌──────────────────────────────────────────────────────────────────┐
│  STEP 2 OF 4: PYTHON ENVIRONMENT                                 │
└──────────────────────────────────────────────────────────────────┘
```

### Check for uv

```bash
which uv
```

**If uv NOT found:**

Tell the user:
> Personal OS uses `uv` for Python dependency management.
>
> Install it with:
> ```bash
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ```

Use AskUserQuestion: "Install uv now?"
- Yes, install it
- Skip for now

If they skip, warn them that `uv sync` commands won't work until they install it.

**If uv IS found:**

Tell the user: "uv found."

### Set up environment

```bash
uv sync
```

Confirm: "Python environment ready."

---

## Step 3: Skills Symlinks

```
┌──────────────────────────────────────────────────────────────────┐
│  STEP 3 OF 4: SKILLS SYMLINKS                                    │
└──────────────────────────────────────────────────────────────────┘
```

This step links external skills from submodules to `.claude/skills/`.

Run the setup script:

```bash
uv run setup-symlinks
```

This script:
- Initializes git submodules if needed
- Creates symlinks for skills from `_external/` repos
- Optionally links private skills from `_internal/` (if present)

Confirm: "Skills symlinked."

---

## Step 4: Todoist MCP (Optional)

```
┌──────────────────────────────────────────────────────────────────┐
│  STEP 4 OF 4: TODOIST SYNC (OPTIONAL)                            │
└──────────────────────────────────────────────────────────────────┘
```

Use AskUserQuestion: "Set up Todoist sync? This lets you capture ideas in Todoist and sync them to your local KANBAN.md file."
- Yes, set it up
- No, skip this

**If NO:** Skip to Wrap Up. Tell them they can set it up later with:
```bash
claude mcp add --transport http todoist https://mcp.todoist.com/sse
```

**If YES:**

Check if already configured:
```bash
claude mcp list | grep -i todoist
```

**If NOT found**, run:
```bash
claude mcp add --transport http todoist https://mcp.todoist.com/sse
```

Tell the user:
> Todoist MCP added. Next time you start Claude Code:
> 1. Run `/mcp` and select todoist
> 2. Authenticate in your browser
> 3. Create a project called **PersonalOS** in Todoist with **board view**
>
> Then use `/process-backlog` to sync tasks.

**If already configured:**

Tell the user:
> Todoist already configured. Make sure you have a **PersonalOS** project with board view in Todoist.

---

## Wrap Up

```
┌──────────────────────────────────────────────────────────────────┐
│  SETUP COMPLETE                                                  │
└──────────────────────────────────────────────────────────────────┘

  [x] Voice configured (VOICE.md)
  [x] Python environment ready
  [x] Skills symlinked
  [x] Todoist sync (if enabled)

  NEXT STEPS:

  Before drafting content, set up platform-specific voices:

  1. Add your best posts to: 1-content/01-blog/04-my-top/
  2. Run: /update-voice blog
  3. Then: /draft-blog [your topic]
```

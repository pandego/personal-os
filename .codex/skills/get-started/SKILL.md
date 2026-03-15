---
name: get-started
description: Friendly guided onboarding for Personal OS. Use when the user wants to get started, shape the system around their life, and create a clear first blueprint for how this folder should serve them.
---

# Personal OS - Get Started

Welcome message:

```
╔══════════════════════════════════════════════════════════════════╗
║                  PERSONAL OS - GET STARTED                      ║
╠══════════════════════════════════════════════════════════════════╣
║  Three steps:                                                   ║
║    1. Your Intent - what this system is for                     ║
║    2. Make It Ready - voice + optional Python setup             ║
║    3. Your Blueprint - shape the system around your life        ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Step 1: Your Intent

```
┌──────────────────────────────────────────────────────────────────┐
│  STEP 1 OF 3: YOUR INTENT                                        │
└──────────────────────────────────────────────────────────────────┘
```

Goal: understand what this Personal OS should actually help with.

Use AskUserQuestion in short, clear batches. Keep the language human and low-jargon.

### Question Set 1: Context

Ask: "Let’s shape this around you first."

Use AskUserQuestion with these questions:
1. **"What’s your name?"** (free text)
2. **"What do you want this Personal OS to help you with most right now?"** Options:
   - Personal organization
   - Work and projects
   - Writing and content
   - Learning and knowledge
   - A mix of several things
   - (Other for custom)
3. **"What feels most messy or overloaded today?"** (free text)

### Question Set 2: Operating Style

Ask: "Now let’s make it fit how you actually work."

Use AskUserQuestion with these questions:
1. **"Do you want this system to feel more simple or more structured?"** Options:
   - Very simple
   - Balanced
   - Quite structured
2. **"What do you want help with first?"** (multiSelect: true) Options:
   - Capturing ideas
   - Organizing tasks
   - Writing better
   - Reviewing my week
   - Keeping notes and knowledge in order
   - Planning projects
   - Staying consistent
   - (Other for custom)
3. **"What should stay outside this system?"** (free text)

### Question Set 3: Communication Style

Ask: "Last part - how should your assistant sound and behave?"

Use AskUserQuestion with these questions:
1. **"How direct should the assistant be?"** Options:
   - Very direct
   - Balanced
   - Gentle and encouraging
2. **"How formal should it sound?"** Options:
   - Professional but warm
   - Casual and clear
   - Very conversational
3. **"What should it avoid?"** (multiSelect: true) Options:
   - Corporate jargon
   - Being too verbose
   - Being too technical
   - Sounding robotic
   - Being pushy
   - (Other for custom)

Keep answers for the blueprint and `VOICE.md` generation.

---

## Step 2: Make It Ready

```
┌──────────────────────────────────────────────────────────────────┐
│  STEP 2 OF 3: MAKE IT READY                                      │
└──────────────────────────────────────────────────────────────────┘
```

This step keeps the setup light and understandable.

### Part A: Create `VOICE.md`

Read `assets/VOICE_template.md` and generate a simple `VOICE.md` based on the communication answers from Step 1.

The resulting file should be practical and plain-language, not overly literary or abstract.

Save to `/VOICE.md`.

Confirm: "Voice saved to VOICE.md"

### Part B: Optional Python setup

Tell the user, in simple language:

> Some skills and helpers use Python behind the scenes.
> We use `uv` because it keeps project tools organized and avoids making a mess of your main Python setup.
> You can set it up now, or skip it and do it later.

Run:

```bash
which uv
```

**If uv NOT found:**
Show:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Use AskUserQuestion: "Do you want to install `uv` now?"
- Yes, install it
- Skip for now

If they skip, say that some advanced helpers may not work until Python tools are set up.

**If uv IS found:**
Tell the user: "Great - `uv` is already available."

Then ask:
"Do you want to prepare the Python environment now?"
- Yes, prepare it
- Skip for now

If yes, run:

```bash
uv sync
```

Confirm: "Python environment ready."

### Part C: Runtime layout check

Run:

```bash
ls -la .codex .claude
```

Confirm that:
- `.codex/` exists
- `.claude` points to `.codex`
- local skills available are `process-backlog`, `review`, and `get-started`

Confirm: "Runtime layout verified."

---

## Step 3: Your Blueprint

```
┌──────────────────────────────────────────────────────────────────┐
│  STEP 3 OF 3: YOUR BLUEPRINT                                     │
└──────────────────────────────────────────────────────────────────┘
```

Create a tailored blueprint file at the repo root:

- `MY_OS_BLUEPRINT.md`

The file should be short, clear, and personalized.

## Blueprint structure

Use this structure:

```md
# My Personal OS Blueprint

## What this system is for
- ...

## My current priorities
- ...

## What this system should help me do first
- ...

## Suggested focus for each domain
### 1-personal
- ...

### 2-business
- ...

### 3-content
- ...

## Suggested changes to make next
1. ...
2. ...
3. ...

## What to ignore for now
- ...

## How I want my assistant to behave
- ...
```

Guidance:
- tailor recommendations to the user’s answers
- keep suggestions realistic and not overly ambitious
- if one domain is not relevant, say so clearly instead of forcing fake structure
- prefer a focused first version over a bloated life system

After writing the file, give a short summary of:
- what this Personal OS is mainly for
- the top 3 recommended next actions

---

## Wrap Up

```
┌──────────────────────────────────────────────────────────────────┐
│  GET STARTED COMPLETE                                            │
└──────────────────────────────────────────────────────────────────┘

  [x] Intent clarified
  [x] Voice captured
  [x] Optional setup handled
  [x] Personal blueprint created

  NEXT STEPS:

  1. Read `MY_OS_BLUEPRINT.md`
  2. Adjust the folder structure only if the blueprint suggests it
  3. Start adding real material slowly - not everything at once
```

## Optional later enhancements

Only mention these at the end, not as core steps:
- Todoist sync via `/process-backlog`
- custom skills
- deeper automation
- MCP integrations

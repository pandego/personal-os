---
name: get-started
description: One-time onboarding. Populates `memories/USER.md` with information about the user (their name, story, intended use, tone preference) and `memories/MEMORY.md` with their setup, then confirms folder structure. Use when the user runs `/get-started`, when `memories/USER.md` or `memories/MEMORY.md` is missing or contains a placeholder marker, or when they ask to onboard or re-onboard.
---

# Get Started

Goal: capture information about the user so the assistant can work better for them.

By the end:
- `memories/USER.md` is populated with information about the user.
- `memories/MEMORY.md` is populated with the user's setup and folder choice.
- folder structure is confirmed.

`SOUL.md` already exists at repo root with a JARVIS-like character. This skill captures the user, not the assistant. Do not edit `SOUL.md`.

## Rules

- Ask all four onboarding questions in ONE call to your runtime's question tool:
  - Claude Code: `AskUserQuestion`
  - Codex: `functions.request_user_input`
  - Other runtimes: the equivalent input tool
- Never rename or remove a folder without an explicit yes from the user for that specific change.
- Use the templates in `assets/`. Replace every `{PLACEHOLDER}` with an answer.
- Keep your chat output short. One sentence per step.

## Step 1: Welcome

Print this and nothing else:

```
PERSONAL OS - GET STARTED
A few questions to tune your assistant. Then we confirm your folders.
```

## Step 2: Ask the four questions in one batch

Call your runtime's question tool ONCE with these four questions in this order:

1. "What is your name?"
2. "What's your story in two sentences? (role, projects, what you care about)"
3. "What would you use your Personal OS for?"
   Options:
   - `I need an assistant for daily life`
   - `I want to automate everything I can`
   - `No idea, I'll figure it out later`
4. "How should the assistant feel?"
   Options:
   - `Classic JARVIS: dry wit, calm, formal-ish`
   - `More casual: friendly, looser, less formal`
   - `More direct: terse, no flourishes, just the work`

Store the answers as: NAME, STORY, FOCUS, TONE.

## Step 3: Write `memories/USER.md`

Read `assets/USER_template.md`. Replace placeholders:

- `{NAME}` -> NAME
- `{STORY}` -> STORY
- `{FOCUS}` -> FOCUS
- `{TONE}` -> TONE
- `{NOTES}` -> empty

Write the result to `memories/USER.md`, overwriting the placeholder.

Print: `Saved memories/USER.md.`

## Step 4: Confirm folder structure

Default folders are `1-personal/`, `2-business/`, `3-content/`.

Call the question tool ONCE:

- "Keep the default three folders, or change them?" - single-select.
  Options: `Keep all three`, `Drop one or more`, `Rename one`.

Branch on the answer:

- **Keep all three**: set `DOMAINS = "1-personal, 2-business, 3-content"` and `REMOVED_DOMAINS = "none"`. Continue.
- **Drop one or more**: ask one yes/no per folder. For each `Yes`, run `git rm -r <folder>` from repo root. Update `DOMAINS` and `REMOVED_DOMAINS`.
- **Rename one**: ask which folder, ask the new name, run `git mv <old> <new>` from repo root. Update `DOMAINS`.

Never run `git rm` or `git mv` without an explicit yes from the user for that specific change.

## Step 5: Write `memories/MEMORY.md`

Read `assets/MEMORY_template.md`. Replace placeholders:

- `{REPO_ROOT}` -> output of `pwd`
- `{DOMAINS}` -> the value from Step 4
- `{REMOVED_DOMAINS}` -> the value from Step 4

Write to `memories/MEMORY.md`, overwriting the placeholder.

Print: `Saved memories/MEMORY.md.`

## Step 6: Wrap up

Print this and nothing else:

```    
     ✦  ·  ✦  ·  ✦  ·  ✦                                                                                                                       
       SYSTEMS ONLINE                   
     ✦  ·  ✦  · ✦  ·  ✦ 

           \ | /                                         
            .─.                                                                                                                                    
         ──│ ⊙ │──                                                                                                                                 
            '─'                                
           / | \                                                                                                                                   

Personal OS online. Tuned to your preferences.

A few ways to begin:
  ▸ Ask anything. I have your context now.
  ▸ /draft-content when you have something to write.
  ▸ /review for a weekly or yearly reflection.
  ▸ /skill-creator to teach me a new trick.

Ready when you are.
```

End the skill. Do not propose other actions unsolicited.

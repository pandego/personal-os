---
name: setup-repo
description: Interactive setup workflow for Personal OS repository. Use when user explicitly asks to set up the repo, initialize Personal OS, or run first-time setup. Guides through voice configuration (asking playful questions about communication style, personality), Python environment setup (checking for uv), and optional Todoist MCP configuration for task/idea sync.
---

# Personal OS Setup

Three things to set up: your voice, Python environment, and optionally Todoist sync.

## 1. Voice Configuration

Ask these questions conversationally. Be playful and direct.

**The basics:**
- "What's your name and what do you do for work?"
- "Who's your content for? Engineers? Founders? Your future confused self?"

**Personality vibes:**
- "Quick one—are you more 🎯 *straight to the point* or 🌊 *let me tell you a story first*?"
- "When explaining something technical: 📚 *step-by-step teacher* or 💡 *here's the insight, figure it out*?"
- "Caveats and disclaimers: 🤓 *I have 17 edge cases to mention* or ⚡ *main point, moving on*?"

**Optional fun:**
- "Know your Myers-Briggs type? If yes, what is it? If no, no worries."

**Tone calibration:**
- "Scale of 'academic paper' to 'explaining to a friend at a bar'—where do you land?"
- "Emojis: love them, use sparingly, or hard pass?"
- "Swearing in content: fuck yeah, occasionally, or keep it clean?"

### Generate VOICE.md

After gathering answers, read `assets/VOICE_template.md` and fill it in based on responses.

Save to `/VOICE.md` (root of repo).

---

## 2. Python Environment

### Check for uv

```bash
which uv
```

**If uv NOT found**, say something like:

> "Ah. Here's the thing—without `uv`, your Python environments will turn into a tangled mess faster than you can say 'but it works on my machine.'
>
> I'd strongly recommend installing it:
> ```bash
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ```
>
> Want to install it now, or proceed at your own risk?"

**If uv IS found:**

> "Nice! You have `uv`. Your future self thanks you."

### Set up environment

```bash
uv sync
```

---

## 3. Todoist MCP Setup (Optional)

Ask the user:

> "Do you want to set up Todoist sync? This lets you capture ideas in Todoist and sync them to your local `KANBAN.md` file (and vice versa).
>
> **Requirements:**
> - A Todoist account (free tier works)
> - A project named **PersonalOS** with **board view** enabled
>
> Want to set this up?"

**If user says NO:**

> "No problem! You can always set it up later by running:
> ```bash
> claude mcp add --transport http todoist https://ai.todoist.net/mcp
> ```
> Then `/mcp` → select todoist → authenticate."

Skip to Wrap Up.

**If user says YES:**

Check if Todoist MCP is already configured:

```bash
claude mcp list | grep -i todoist
```

**If NOT found**, run:

```bash
claude mcp add --transport http todoist https://ai.todoist.net/mcp
```

Then tell the user:

> "Done! Next time you launch Claude, run `/mcp`, select **todoist**, and authenticate via your browser.
>
> **Important:** Make sure you have a project called **PersonalOS** in Todoist with **board view** enabled. That's what syncs with your local `KANBAN.md`.
>
> Use `/sync-todoist` to sync your ideas between here and Todoist."

**If already configured:**

> "Todoist MCP already set up. Nice.
>
> Just make sure you have a **PersonalOS** project in Todoist with board view—that's where your ideas sync to."

---

## Wrap Up

> "Setup complete!
> - ✅ Voice configured (saved to VOICE.md)
> - ✅ Python environment ready
> - ✅ Todoist MCP configured (use `/process-backlog` to process and sync backlog items) ← *only if they set it up*
>
> **Next step:** Before drafting content, set up your platform voices:
> 1. Place your best posts in `1-content/01-blog/04-my-top/` (curated, not all)
> 2. Add external examples to `1-content/01-blog/05-swipe-files/` (optional)
> 3. Run `/update-voice blog` to generate your blog-specific voice
> 4. Then you're ready for `/draft-blog [detailed idea for blog post]`"

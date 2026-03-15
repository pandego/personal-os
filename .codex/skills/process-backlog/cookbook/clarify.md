# Cookbook: Clarify

Handle unclear backlog items by asking the user first, research only after clarification.

**Principle:** Don't research the wrong thing by jumping ahead. User knows their intent; ask them.

---

## When to Use

Dispatch here from `process-to-ready.md` when:
- Intent is ambiguous
- Multiple valid interpretations exist
- Critical context is missing
- "What does done look like?" has no clear answer

---

## Workflow

### 1. Ask User First

Use `AskUserQuestion` with targeted questions.

**Primary question:**
> "What did you mean by '[vague item]'?"

**Follow-up options (pick 1-2 most relevant):**
- "What does 'done' look like for this?"
- "Any constraints or preferences I should know?"
- "Is this one task or multiple?"
- "What's the scope boundary?"

**Example:**

```
Backlog item: "voice agent thing"

AskUserQuestion:
  question: "What did you mean by 'voice agent thing'?"
  options:
    - "TTS skill using ElevenLabs"
    - "STT transcription feature"
    - "Full voice assistant (TTS + STT)"
    - "Research voice AI options"
```

### 2. Evaluate User Response

Based on user's clarification:

**Enough detail provided:**
→ Return to `process-to-ready.md` with clarified intent
→ Format as DoR-compliant task

**User says "I don't know, research it":**
→ Proceed to Step 3 (Research)

**User provides partial info:**
→ Ask one more targeted question
→ Maximum 2 rounds of questions

### 3. Research (Only If Requested)

**Only reach this step if user explicitly asks for research.**

Research approaches:
- **Codebase exploration**: Use Task tool with Explore agent
- **Web search**: Use WebSearch for external APIs/tools
- **File reading**: Check existing patterns in codebase

After research, present findings to user:
> "Here's what I found about [topic]:
> - Option A: [description]
> - Option B: [description]
> Which direction would you like?"

### 4. Output

Return clarified task specification to `process-to-ready.md`:

```
Original: "[vague item]"
Clarified intent: "[clear description]"
User constraints: "[any mentioned]"
Ready for DoR formatting: yes/no
```

---

## Question Design

**Good questions:**
- Specific, answerable
- Offer concrete options
- One question at a time

**Bad questions:**
- Open-ended ("Tell me more")
- Multiple questions bundled
- Assumptive ("You want X, right?")

---

## Conversation Limits

- Maximum 2 rounds of questions per item
- If still unclear after 2 rounds:
  > "Let's leave this in Backlog for now. Come back to it when you have more clarity."
- Move to next backlog item

---

## Anti-Pattern: Premature Research

**Don't:**
```
Backlog: "voice agent"
→ Immediately research ElevenLabs API
→ Present detailed TTS implementation plan
→ User: "I meant STT, not TTS"
```

**Do:**
```
Backlog: "voice agent"
→ Ask: "TTS, STT, or both?"
→ User: "STT for transcription"
→ Now research STT options if needed
```

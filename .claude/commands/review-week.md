---
description: Generate a weekly review from dictated notes or transcript
allowed-tools: Read, Write
---

# Generate Weekly Review

Generate a structured weekly review from free-form notes.

## Transcript

$ARGUMENTS - Dictated notes or transcript of the week

## Steps

1. **Read the template**: `3-personal/01-week-reviews/TEMPLATE_week-review.md`
2. **Process the transcript**: Extract goals, outcomes, blockers, learnings, next steps
3. **Create file**: `3-personal/01-week-reviews/02-done/YYYY-MM-DD_week-review.md`
   - Use the Friday date of the reviewed week
   - Note: `01-drafts/` folder is for raw transcripts only, generated reviews go directly to `02-done/`

## Instructions

- Accept messy, spoken-style input. Infer meaning, correct obvious mistakes.
- Don't invent content — only use what's in the transcript.
- Use bullet points. Keep sentences concise.
- Skip empty sections or write "None".
- Infer week date from context (Europe/Paris timezone).
- Mark ambiguous details with "(unclear)" — don't ask questions.
- Correct transcription errors while preserving meaning.

# Update Voice cookbook

Goal: rewrite `VOICE.md` at repo root based on the prose in `3-content/_voice-samples/`.

## Pre-checks

1. Confirm `3-content/_voice-samples/` exists. If not, tell the user the voice samples folder is missing and stop.
2. List `.md` files in that folder, ignoring `README_voice-samples.md`.
3. If fewer than 2 sample files: print `Found {N} sample(s) in 3-content/_voice-samples/. Drop a few more (emails, blog posts, LinkedIn posts, anything in your voice) and re-run.` and stop.

## Step 1: Read the samples

Read every `.md` file in `3-content/_voice-samples/` (other than the README).

## Step 2: Extract patterns

Look for repetition across the samples. Record only patterns you see in at least two samples.

For each of these categories, note up to three concrete patterns:

- Openings: how does the writer begin? Statement? Question? Specific detail?
- Sentence rhythm: short/punchy, long/winding, fragment-heavy, alternating?
- Vocabulary: signature words or phrases the writer uses. Words the writer avoids.
- Structural moves: lists, rhetorical questions, "claim then evidence", call-and-response, etc.
- Closings: how does the writer end? CTA, summary, open question, deadpan?
- Anti-patterns: things the writer never does (em dashes, exclamation marks, hype words, "honestly", whatever is consistently absent).

Quote a short snippet from the samples to anchor each pattern.

## Step 3: Write `VOICE.md`

Overwrite `VOICE.md` at repo root. Replace the placeholder marker. Use this structure:

```md
# VOICE

Patterns extracted from the user's real writing. Apply these when drafting content for them.

## Source
- Samples used: {COUNT} files in `3-content/_voice-samples/`
- Last updated: {YYYY-MM-DD}

## Openings the user uses
- {Pattern}. Example: "{short snippet}"
- ...

## Sentence rhythm
- {Pattern}. Example: "{short snippet}"
- ...

## Vocabulary
### Signature words and phrases
- {word or phrase}
### Words and phrases the user avoids
- {word or phrase}

## Structural moves
- {Move}. Example: "{short snippet}"
- ...

## Closings the user uses
- {Pattern}. Example: "{short snippet}"
- ...

## Anti-patterns (things the user never does)
- {Thing the voice never does}
- ...
```

## Rules

- Quote, do not invent. If a snippet is not in the samples, do not use it.
- If you cannot find at least two samples worth of repetition for a category, write `(not enough signal yet)` under that heading and move on.
- Keep guidance practical, not literary. Another assistant should be able to apply each pattern when drafting.
- Overwrite the file completely. Do not preserve the placeholder marker.

## Confirm

Print: `Saved VOICE.md from {N} samples.`

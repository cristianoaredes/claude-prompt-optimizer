---
description: Rewrite a raw prompt into the prompt-craft formula [VERB] [WHAT] in [WHERE]. [CONSTRAINT].
argument-hint: "<prompt>"
---

# /sharpen — Prompt Sharpener

Takes a raw, vague, or verbose prompt and rewrites it into the prompt-craft formula.

## Formula

```
[VERB] [WHAT] in [WHERE]. [CONSTRAINT].
```

## Behavior

When the user runs `/sharpen <prompt>`:

1. Show the **before** prompt exactly as provided.
2. Use your reasoning to produce a **sharpened** version that follows the formula:
   - **VERB** — a precise action word (`Implement`, `Refactor`, `Investigate`, `Remove`, `Compare`, `Document`, `Test`, `Optimize`…)
   - **WHAT** — the specific thing to act on
   - **WHERE** — the file, module, endpoint, or scope
   - **CONSTRAINT** — a key boundary, invariant, or success criterion
3. Show the **after** prompt clearly labeled.
4. Briefly explain what changed and why it helps (1–2 sentences).

## Examples

**Before:** `can you please help me fix the thing where the login breaks sometimes?`

**After:** `Investigate intermittent login failures in AuthController. Reproduce with existing test suite and report root cause.`

**Before:** `i want you to make the api faster`

**After:** `Optimize response latency on GET /api/search. Target <200 ms p95 without changing the public interface.`

## Important

- Preserve all original intent — do not drop requirements.
- If the prompt is already concise and follows the formula, confirm it and stop.
- Do not execute the sharpened prompt; only return the rewritten text.

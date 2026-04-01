---
description: Switch Claude Code model or provider (Bedrock, Vertex, Opus, fast, custom).
argument-hint: "[status|bedrock|vertex|opus|fast|reset|set MODEL_ID]"
---

# /mode — Model & Provider Switcher

Controls which model and provider Claude Code uses via `~/.claude/settings.json`.

## `/mode status`

Read `settings.json` and display current model configuration:
- `ANTHROPIC_MODEL` (or default if unset)
- `CLAUDE_CODE_SUBAGENT_MODEL`
- `ANTHROPIC_SMALL_FAST_MODEL`
- Active provider (`CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`, or default Anthropic)

## `/mode bedrock`

Set in `env`:
```json
{
  "CLAUDE_CODE_USE_BEDROCK": "1"
}
```
Remind the user to ensure `AWS_PROFILE` or `AWS_ACCESS_KEY_ID` are set in their shell.

## `/mode vertex`

Set in `env`:
```json
{
  "CLAUDE_CODE_USE_VERTEX": "1",
  "ANTHROPIC_VERTEX_PROJECT_ID": "<ask user for GCP project ID if not already set>"
}
```

## `/mode opus`

Set in `env`:
```json
{
  "CLAUDE_CODE_EFFORT_LEVEL": "high",
  "MAX_THINKING_TOKENS": "32000"
}
```
Note: The actual model is selected by the UI — this maximizes the capabilities of whatever Opus model is active.

## `/mode fast`

Set in `env`:
```json
{
  "CLAUDE_CODE_EFFORT_LEVEL": "low",
  "DISABLE_AUTO_COMPACT": "1"
}
```
This minimizes reasoning overhead for quick iteration.

## `/mode set MODEL_ID`

Set in `env`:
```json
{
  "ANTHROPIC_MODEL": "MODEL_ID"
}
```
Example: `/mode set claude-opus-4-5-20251101`

## `/mode reset`

Remove from `env`:
- `ANTHROPIC_MODEL`
- `CLAUDE_CODE_USE_BEDROCK`
- `CLAUDE_CODE_USE_VERTEX`
- `CLAUDE_CODE_SUBAGENT_MODEL`
- `ANTHROPIC_SMALL_FAST_MODEL`

Confirm: "✅ Model settings reset. Using default Anthropic API with auto-selected model."

## Important

- Always merge, never overwrite the full `env` block.
- `CLAUDE_CODE_USE_BEDROCK` and `CLAUDE_CODE_USE_VERTEX` are mutually exclusive — if setting one, unset the other.
- Changing providers requires a restart.

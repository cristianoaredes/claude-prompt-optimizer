---
description: Manage CLAUDE_CODE_EXTRA_BODY and CLAUDE_CODE_EXTRA_METADATA injection into every API request.
argument-hint: "[status|body JSON|metadata JSON|reset]"
---

# /inject — API Injection Controller

Manages `CLAUDE_CODE_EXTRA_BODY` and `CLAUDE_CODE_EXTRA_METADATA` in `~/.claude/settings.json`.

> ⚠️ **Warning**: These values are injected into **every** API request. Use with caution.

## `/inject status`

Read `~/.claude/settings.json` and display the current values:
- `CLAUDE_CODE_EXTRA_BODY` (parsed as pretty JSON if present)
- `CLAUDE_CODE_EXTRA_METADATA` (parsed as pretty JSON if present)

If neither is set, say: "No injection variables set."

## `/inject body '{"key": "value"}'`

1. Parse the existing `CLAUDE_CODE_EXTRA_BODY` value as JSON (if it exists).
2. Deep-merge the user-provided JSON into the existing object.
3. Write the merged result back as a JSON-string value in `env`.

Example:
- Existing: `{"temperature": 0.8}`
- User injects: `{"top_p": 0.9}`
- Result: `{"temperature": 0.8, "top_p": 0.9}`

Confirm: "✅ Merged into `CLAUDE_CODE_EXTRA_BODY`. Restart Claude Code to apply."

## `/inject metadata '{"key": "value"}'`

1. Parse the existing `CLAUDE_CODE_EXTRA_METADATA` value as JSON (if it exists).
2. Deep-merge the user-provided JSON into the existing object.
3. Write the merged result back as a JSON-string value in `env`.

Confirm: "✅ Merged into `CLAUDE_CODE_EXTRA_METADATA`. Restart Claude Code to apply."

## `/inject reset`

Remove both `CLAUDE_CODE_EXTRA_BODY` and `CLAUDE_CODE_EXTRA_METADATA` from the `env` block.

Confirm: "✅ Injection variables removed."

## Important

- Always **merge**, never blindly overwrite existing JSON.
- The values are stored as **JSON strings inside the JSON object** — preserve proper escaping.
- If the user provides invalid JSON, reject the command and show the parse error.
- Remind the user on every modification that this affects **every** API request.

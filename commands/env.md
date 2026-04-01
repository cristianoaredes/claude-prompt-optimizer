---
description: Inspect, set, or reset Claude Code environment variables in settings.json.
argument-hint: "[list|reset|set KEY value]"
---

# /env — Environment Variable Inspector

Manages the `env` block in `~/.claude/settings.json`.

## When run without arguments (`/env`)

Read `~/.claude/settings.json` and display the current `env` block as a table:

| Variable | Value | Source |
|---|---|---|
| (each key) | (each value) | settings.json |

If the `env` block is empty or missing, say: "No custom environment variables set. All defaults active."

## `/env reset`

Remove the entire `env` block from `~/.claude/settings.json`.  
Confirm: "✅ Env block cleared. All variables reset to defaults. Restart Claude Code for changes to take effect."

## `/env set KEY value`

Merge `{"KEY": "value"}` into the `env` block in `~/.claude/settings.json`.  
Always **merge**, never overwrite other keys.  
Confirm: "✅ Set `KEY=value` in settings.json."

## `/env unset KEY`

Remove a single key from the `env` block without touching others.  
Confirm: "✅ Removed `KEY` from settings.json."

## Important

- Always read the file fresh before writing — never use a cached version.
- After any write, show the full updated `env` block for confirmation.
- Remind the user: "Restart Claude Code for env changes to take effect."

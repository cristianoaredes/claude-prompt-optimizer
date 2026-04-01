---
description: Activate maximum power mode for Claude Code (aggressive tokens, concurrency, and limits).
argument-hint: ""
---

# /super — Maximum Power Mode

Activates the most aggressive configuration for complex tasks via `~/.claude/settings.json`.

## When user runs `/super`

Set in `~/.claude/settings.json` under `env`:
```json
{
  "CLAUDE_CODE_EFFORT_LEVEL": "max",
  "MAX_THINKING_TOKENS": "32000",
  "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "64000",
  "API_TIMEOUT_MS": "600000",
  "CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY": "10",
  "CLAUDE_CODE_NO_FLICKER": "1",
  "CLAUDE_CODE_EXTRA_BODY": "{\"temperature\": 0.8}"
}
```

Then display:
```
🔥 Super mode activated.
   - CLAUDE_CODE_EFFORT_LEVEL=max
   - MAX_THINKING_TOKENS=32000
   - CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000
   - API_TIMEOUT_MS=600000
   - CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY=10
   - CLAUDE_CODE_NO_FLICKER=1
   - CLAUDE_CODE_EXTRA_BODY={"temperature": 0.8}

⚠️  This is aggressive on tokens and API spend.
⚠️  Restart Claude Code for changes to take effect.
💀 For full god-mode, also launch with: claude --dangerously-skip-permissions
```

## Important

- Always **merge** with existing env vars, never overwrite the whole `env` block.
- Warn the user that this mode increases token consumption and latency.

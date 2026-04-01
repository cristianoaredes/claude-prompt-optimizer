---
description: Toggle full debug logging to disk (CLAUDE_DEBUG, OTEL_LOG_TOOL_DETAILS, CLAUDE_CODE_DUMP_AUTO_MODE).
argument-hint: "[on|off|dump|status]"
---

# /debug — Debug Mode Controller

Controls Claude Code's internal debug logging system.

## `/debug on`

Set the following in `~/.claude/settings.json` under `env`:
```json
{
  "CLAUDE_DEBUG": "1",
  "CLAUDE_CODE_DEBUG_LOGS_DIR": "/tmp/claude-debug",
  "OTEL_LOG_TOOL_DETAILS": "1",
  "CLAUDE_CODE_DUMP_AUTO_MODE": "1"
}
```

Then display:
```
✅ Debug mode ON. Logs will be written to /tmp/claude-debug/
   - CLAUDE_DEBUG=1          → Verbose internal logging
   - OTEL_LOG_TOOL_DETAILS=1 → Full tool invocation logs
   - CLAUDE_CODE_DUMP_AUTO_MODE=1 → Saves all auto-mode decisions

⚠️  Restart Claude Code for changes to take effect.
⚠️  Disable when done — debug logging is verbose and affects performance.
```

## `/debug off`

Remove these keys from the `env` block:
- `CLAUDE_DEBUG`
- `CLAUDE_CODE_DEBUG_LOGS_DIR`
- `OTEL_LOG_TOOL_DETAILS`
- `CLAUDE_CODE_DUMP_AUTO_MODE`
- `CLAUDE_CODE_DEBUG_LOG_LEVEL`
- `CLAUDE_CODE_FRAME_TIMING_LOG`
- `CLAUDE_CODE_DEBUG_REPAINTS`

Confirm: "✅ Debug mode OFF. Log files remain at /tmp/claude-debug/ for inspection."

## `/debug dump`

Run `ls -lt /tmp/claude-debug/ | head -n 20` and display the most recent log files.
Then show the last 50 lines of the most recent `.log` file.

## `/debug status`

Show which debug vars are currently in `settings.json` and whether `/tmp/claude-debug/` has any files.

## Important

- Never set `OTEL_LOG_USER_PROMPTS=1` — this logs the user's actual prompts to disk, which is a privacy risk.
- Merging only: never overwrite the entire `env` block.

---
description: Enable or disable experimental Agent Teams (multi-process Claude swarms).
argument-hint: "[on|off|status]"
---

# /swarm — Agent Teams Controller

Controls Claude Code's experimental multi-process agent system via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`.

> **Note**: This is different from Coordinator Mode (`/tune multi-agent`). Agent Teams spawns **separate Claude processes** that communicate with each other. Coordinator Mode orchestrates sub-agents within a single process.

## `/swarm status`

Show current swarm configuration from `settings.json`:
- Is `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` set?
- Is `CLAUDE_CODE_COORDINATOR_MODE` set?
- What concurrency level is active?

## `/swarm on`

Set in `env`:
```json
{
  "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1",
  "CLAUDE_CODE_COORDINATOR_MODE": "1",
  "CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY": "5",
  "CLAUDE_CODE_EFFORT_LEVEL": "high",
  "MAX_THINKING_TOKENS": "32000",
  "API_TIMEOUT_MS": "600000"
}
```

Then display:
```
✅ Agent Swarm mode ON.

How to use:
  - Give Claude a large, parallelizable task
  - It will spawn worker agents automatically
  - Workers share a memory file for coordination
  - Each worker runs as a separate Claude process

⚠️  This is experimental. Restart Claude Code to activate.
⚠️  Parallel agents consume tokens proportionally — monitor usage.
```

## `/swarm off`

Remove from `env`:
- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`
- `CLAUDE_CODE_COORDINATOR_MODE`
- `CLAUDE_CODE_IS_COWORK`

Keep concurrency and timeout settings unless the user asks to reset.

Confirm: "✅ Agent Swarm OFF. Claude runs as a single process. Restart to apply."

## Important

- Always merge, never overwrite `env` block.
- The `CLAUDE_CODE_COORDINATOR_MODE` flag enables single-process orchestration even without full swarms.
- For large tasks (> 10k lines, > 20 files), swarm mode can dramatically reduce wall-clock time.

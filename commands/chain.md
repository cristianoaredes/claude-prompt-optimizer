---
description: Interactive macro wizard — chain multiple tuning profiles, modes, and flags in one shot.
argument-hint: "[wizard|apply <combo>]"
---

# /chain — Macro Wizard

Chains multiple plugin configurations into a single applied block, so you don't have to run `/tune`, `/mode`, `/flags`, and `/super` separately.

## Behavior

### `/chain` or `/chain wizard`

Start an interactive wizard:

1. Ask the user what kind of session they're starting:
   - **"Deep architecture work"** → applies `deep-work` + `opus` + `tengu_scratch` + `tengu_thinkback`
   - **"Fast bug fix"** → applies `speed` + `fast` model + disables telemetry
   - **"Agent swarm session"** → applies `multi-agent` + `swarm on` + `super` concurrency
   - **"Audit / reverse engineering"** → applies `audit-mode` + `debug on` + `yolo on`
   - **"Custom"** → let them pick individual pieces

2. Show the exact env vars that will be set.
3. Ask for confirmation.
4. Apply by merging into `~/.claude/settings.json` under `env`.
5. Confirm what was written and remind: "Restart Claude Code for changes to take effect."

### `/chain apply <combo>`

Apply a named combo directly without the wizard:

| Combo | What it sets |
|---|---|
| `/chain apply deep` | `deep-work` profile + `opus` mode + `tengu_scratch` + `tengu_thinkback` |
| `/chain apply fast` | `speed` profile + `fast` mode + `DISABLE_TELEMETRY=1` |
| `/chain apply swarm` | `multi-agent` profile + swarm on + `CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY=10` |
| `/chain apply audit` | `audit-mode` profile + debug on + yolo on |
| `/chain apply god` | `/super` settings + `swarm on` + `tengu_amber_flint` + `tengu_tool_pear` |
| `/chain apply privacy` | `privacy` profile + `DISABLE_TELEMETRY=1` + `DISABLE_ERROR_REPORTING=1` + `DISABLE_AUTOUPDATER=1` |

## Combo Definitions (for reference)

### `deep`
```json
{
  "CLAUDE_CODE_EFFORT_LEVEL": "high",
  "MAX_THINKING_TOKENS": "32000",
  "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "16384",
  "API_TIMEOUT_MS": "600000",
  "CLAUDE_CODE_NO_FLICKER": "1",
  "CLAUDE_INTERNAL_FC_OVERRIDES": "{\"tengu_scratch\":true,\"tengu_thinkback\":true}"
}
```

### `fast`
```json
{
  "CLAUDE_CODE_EFFORT_LEVEL": "low",
  "DISABLE_AUTO_COMPACT": "1",
  "DISABLE_TELEMETRY": "1",
  "DISABLE_ERROR_REPORTING": "1",
  "DISABLE_COST_WARNINGS": "1"
}
```

### `swarm`
```json
{
  "CLAUDE_CODE_COORDINATOR_MODE": "1",
  "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1",
  "CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY": "10",
  "CLAUDE_CODE_EFFORT_LEVEL": "high",
  "MAX_THINKING_TOKENS": "32000",
  "API_TIMEOUT_MS": "600000"
}
```

### `audit`
```json
{
  "CLAUDE_CODE_DUMP_AUTO_MODE": "1",
  "CLAUDE_CODE_DEBUG_LOGS_DIR": "/tmp/claude-audit",
  "OTEL_LOG_TOOL_DETAILS": "1",
  "CLAUDE_CODE_VERIFY_PLAN": "true",
  "CLAUDE_CODE_TWO_STAGE_CLASSIFIER": "thinking",
  "CLAUDE_CODE_AUTO_MODE_MODEL": "claude-sonnet-4-6"
}
```

### `god`
```json
{
  "CLAUDE_CODE_EFFORT_LEVEL": "max",
  "MAX_THINKING_TOKENS": "32000",
  "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "64000",
  "API_TIMEOUT_MS": "600000",
  "CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY": "10",
  "CLAUDE_CODE_NO_FLICKER": "1",
  "CLAUDE_CODE_EXTRA_BODY": "{\"temperature\": 0.8}",
  "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1",
  "CLAUDE_CODE_COORDINATOR_MODE": "1",
  "CLAUDE_INTERNAL_FC_OVERRIDES": "{\"tengu_amber_flint\":true,\"tengu_tool_pear\":true}"
}
```

### `privacy`
```json
{
  "DISABLE_TELEMETRY": "1",
  "DISABLE_ERROR_REPORTING": "1",
  "DISABLE_AUTOUPDATER": "1",
  "DISABLE_INSTALLATION_CHECKS": "1"
}
```

## Application Rules

- Always **merge** the combo JSON into the existing `env` block.
- If the combo and existing env have conflicting keys, the combo wins.
- After writing, display the full updated `env` block for confirmation.
- Always remind: "Restart Claude Code for env changes to take effect."

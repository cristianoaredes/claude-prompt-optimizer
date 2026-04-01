---
name: claude-tuning
description: Pre-built configuration profiles for Claude Code based on reverse-engineered internals. Use /tune to apply.
user-invocable: true
---

# Claude Code Tuning — Power User Profiles

These configurations are derived from reverse-engineering the Claude Code source.
They use only **public-build-compatible** environment variables (no `ant`-only features).

## Quick Apply

Tell Claude: "Apply the [PROFILE_NAME] tuning profile" and it will update your
settings.json env block accordingly.

---

## Profile: `deep-work`

For complex features, architecture, and critical code. Maximizes reasoning depth
at the cost of speed and tokens.

```json
{
  "env": {
    "CLAUDE_CODE_EFFORT_LEVEL": "high",
    "MAX_THINKING_TOKENS": "32000",
    "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "16384",
    "CLAUDE_CODE_NO_FLICKER": "1",
    "API_TIMEOUT_MS": "600000"
  }
}
```

**What each does:**
- `EFFORT_LEVEL=high` — Tells the model to reason more deeply before acting
- `MAX_THINKING_TOKENS=32000` — Doubles the default thinking budget (16k → 32k)
- `MAX_OUTPUT_TOKENS=16384` — Allows longer outputs for complex implementations
- `NO_FLICKER=1` — Fullscreen anti-flicker mode (less terminal redraw noise)
- `API_TIMEOUT=600s` — Prevents timeout on long reasoning chains

---

## Profile: `speed`

For quick fixes, simple changes, and high-velocity iteration. Minimizes overhead.

```json
{
  "env": {
    "CLAUDE_CODE_EFFORT_LEVEL": "low",
    "DISABLE_AUTO_COMPACT": "1",
    "DISABLE_TELEMETRY": "1",
    "DISABLE_ERROR_REPORTING": "1",
    "DISABLE_COST_WARNINGS": "1"
  }
}
```

**What each does:**
- `EFFORT_LEVEL=low` — Minimal reasoning, fast responses
- `DISABLE_AUTO_COMPACT` — Skips context compression (saves time on short sessions)
- `DISABLE_TELEMETRY` + `ERROR_REPORTING` — Zero network overhead for analytics
- `DISABLE_COST_WARNINGS` — No interruptions for spending notifications

---

## Profile: `privacy`

Maximum privacy. No data leaves your machine beyond the API call itself.

```json
{
  "env": {
    "DISABLE_TELEMETRY": "1",
    "DISABLE_ERROR_REPORTING": "1",
    "DISABLE_AUTOUPDATER": "1",
    "DISABLE_INSTALLATION_CHECKS": "1"
  }
}
```

---

## Profile: `ci-pipeline`

Optimized for CI/CD and non-interactive automated runs.

```json
{
  "env": {
    "CLAUDE_CODE_EFFORT_LEVEL": "high",
    "CLAUDE_CODE_STREAMLINED_OUTPUT": "1",
    "DISABLE_TELEMETRY": "1",
    "DISABLE_COST_WARNINGS": "1",
    "DISABLE_AUTOUPDATER": "1",
    "CLAUDE_CODE_DISABLE_MOUSE": "1",
    "CLAUDE_CODE_DISABLE_TERMINAL_TITLE": "1",
    "API_TIMEOUT_MS": "300000"
  }
}
```

**What each does:**
- `STREAMLINED_OUTPUT` — Machine-friendly output format
- `DISABLE_MOUSE` + `TERMINAL_TITLE` — No terminal UI interference
- `API_TIMEOUT=300s` — Generous timeout for CI environments

---

## Profile: `multi-agent`

Enables experimental multi-agent orchestration.

```json
{
  "env": {
    "CLAUDE_CODE_COORDINATOR_MODE": "1",
    "CLAUDE_CODE_EFFORT_LEVEL": "high",
    "MAX_THINKING_TOKENS": "32000",
    "CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY": "5",
    "API_TIMEOUT_MS": "600000"
  }
}
```

**What each does:**
- `COORDINATOR_MODE` — Enables the agent to spawn sub-agents
- `MAX_TOOL_USE_CONCURRENCY=5` — Allows more parallel tool execution
- High thinking budget for orchestration decisions

---

## Profile: `debug-session`

When something is going wrong and you need full visibility.

```json
{
  "env": {
    "CLAUDE_DEBUG": "1",
    "CLAUDE_CODE_DEBUG_LOGS_DIR": "/tmp/claude-debug",
    "OTEL_LOG_TOOL_DETAILS": "1",
    "CLAUDE_CODE_DUMP_AUTO_MODE": "1"
  }
}
```

**What each does:**
- `CLAUDE_DEBUG` — Enables verbose debug logging
- `DEBUG_LOGS_DIR` — Writes debug logs to disk
- `OTEL_LOG_TOOL_DETAILS` — Logs every tool invocation with full details
- `DUMP_AUTO_MODE` — Saves every auto-mode safety decision to disk (inspect at `/tmp/claude-debug/`)

---

## Standalone Tuning Variables (use individually)

### Thinking & Reasoning

| Variable | Values | Effect |
|---|---|---|
| `CLAUDE_CODE_EFFORT_LEVEL` | `low` `medium` `high` `max` | Controls depth of reasoning |
| `MAX_THINKING_TOKENS` | integer (default: 16384) | Token budget for internal reasoning |
| `CLAUDE_CODE_DISABLE_THINKING` | `1` | Turns off thinking completely |

### Context Management

| Variable | Values | Effect |
|---|---|---|
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | `0.0-1.0` (default: ~0.8) | When to trigger auto-compaction |
| `CLAUDE_CODE_BLOCKING_LIMIT_OVERRIDE` | integer | Override the blocking token limit |
| `BASH_MAX_OUTPUT_LENGTH` | integer | Truncate long bash outputs |
| `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS` | integer | Max tokens for file reads |
| `SCROLLBACK_BYTES` | integer | Terminal scrollback buffer size |

### MCP & Tools

| Variable | Values | Effect |
|---|---|---|
| `MCP_TIMEOUT` | ms (default: 60000) | Global MCP timeout |
| `MCP_TOOL_TIMEOUT` | ms (default: 300000) | Per-tool MCP timeout |
| `MAX_MCP_OUTPUT_TOKENS` | integer | Cap MCP tool output size |
| `CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY` | integer | Parallel tool execution limit |

### Network & Retries

| Variable | Values | Effect |
|---|---|---|
| `API_TIMEOUT_MS` | ms (default: 120000) | API call timeout |
| `CLAUDE_CODE_MAX_RETRIES` | integer | Max retry attempts on failure |
| `CLAUDE_STREAM_IDLE_TIMEOUT_MS` | ms | Timeout for idle streams |

---

## How to Apply

### Temporary (session only)
```bash
CLAUDE_CODE_EFFORT_LEVEL=high MAX_THINKING_TOKENS=32000 claude
```

### Persistent (via settings.json)
Add to `~/.claude/settings.json`:
```json
{
  "env": {
    "CLAUDE_CODE_EFFORT_LEVEL": "high",
    "MAX_THINKING_TOKENS": "32000"
  }
}
```

### Via Claude Code itself
```
/config set env.CLAUDE_CODE_EFFORT_LEVEL high
```

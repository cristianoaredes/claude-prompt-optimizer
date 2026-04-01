---
description: Enable or disable internal Claude Code feature flags via CLAUDE_INTERNAL_FC_OVERRIDES.
argument-hint: "[list|enable FLAG|disable FLAG|reset]"
---

# /flags — Internal Feature Flag Controller

Controls `CLAUDE_INTERNAL_FC_OVERRIDES` in `~/.claude/settings.json`.

> These are internal feature flags derived from the Claude Code build. Only flags that **work in the public binary** are listed here. Flags behind `USER_TYPE=ant` guards are excluded — they are dead code in the distributed build.

## Known Working Flags

| Flag | Effect |
|---|---|
| `tengu_thinkback` | Enables "think back" reasoning — model re-reads its own outputs before acting |
| `tengu_scratch` | Enables scratch pad mode — model uses an internal notepad for multi-step planning |
| `tengu_tool_pear` | Enables parallel tool execution with dependency awareness |
| `tengu_amber_flint` | Agent Teams kill switch (set to `true` to enable swarms) |
| `claude_code_verify_plan` | Forces plan verification before execution |

## `/flags list`

Read `CLAUDE_INTERNAL_FC_OVERRIDES` from `settings.json` and display current state.
Also show all known flags and whether they are enabled/disabled/unset.

## `/flags enable FLAG`

Merge `{"FLAG": true}` into the JSON value of `CLAUDE_INTERNAL_FC_OVERRIDES`.

Example — to enable `tengu_thinkback`:
```json
"CLAUDE_INTERNAL_FC_OVERRIDES": "{\"tengu_thinkback\":true}"
```

If other flags are already set, preserve them.

Confirm: "✅ Flag `FLAG` enabled. Restart Claude Code to apply."

## `/flags disable FLAG`

Set `{"FLAG": false}` in the overrides JSON (or remove the key).

## `/flags reset`

Remove `CLAUDE_INTERNAL_FC_OVERRIDES` from the `env` block entirely.

Confirm: "✅ All feature flag overrides cleared."

## Recommended Combos

### Maximum Reasoning
```
/flags enable tengu_thinkback
/flags enable tengu_scratch
```

### Maximum Parallelism
```
/flags enable tengu_tool_pear
/flags enable tengu_amber_flint
```

## Important

- Always parse the existing `CLAUDE_INTERNAL_FC_OVERRIDES` JSON string before modifying — it must remain valid JSON.
- The value is stored as a **JSON string inside a JSON object** — be careful with escaping.
- Restart Claude Code after changes.
- Flags not in the "Known Working Flags" table are likely dead code in the public binary.

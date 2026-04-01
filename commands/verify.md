---
description: Toggle plan verification (CLAUDE_CODE_VERIFY_PLAN) to enable VerifyPlanExecutionTool.
argument-hint: "[on|off]"
---

# /verify — Plan Verification Toggle

Toggles `CLAUDE_CODE_VERIFY_PLAN` in `~/.claude/settings.json`.

This enables the `VerifyPlanExecutionTool` in builds where it wasn't dead-code-eliminated.

## `/verify on`

Set in `~/.claude/settings.json` under `env`:
```json
{
  "CLAUDE_CODE_VERIFY_PLAN": "true"
}
```

Then display:
```
✅ Plan verification ON.
   - CLAUDE_CODE_VERIFY_PLAN=true
     → Enables VerifyPlanExecutionTool, which validates plan steps before execution.

⚠️  Restart Claude Code for changes to take effect.
```

## `/verify off`

Remove `CLAUDE_CODE_VERIFY_PLAN` from the `env` block.

Confirm: "✅ Plan verification OFF."

## Important

- Always **merge**, never overwrite the full `env` block.
- Explain that this only works if the current build still includes `VerifyPlanExecutionTool`; in some public builds it may be a no-op.

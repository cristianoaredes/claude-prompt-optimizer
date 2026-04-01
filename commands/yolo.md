---
description: Tune the auto-mode (YOLO) classifier — two-stage safety, model override, and disk auditing.
argument-hint: "[status|on|off]"
---

# /yolo — Auto-Mode Classifier Tuner

Controls the YOLO (auto-mode) classifier configuration in `~/.claude/settings.json`, derived from the internal `yoloClassifier.ts` logic.

## `/yolo status`

Read `~/.claude/settings.json` and show the current YOLO-related env vars:
- `CLAUDE_CODE_TWO_STAGE_CLASSIFIER`
- `CLAUDE_CODE_AUTO_MODE_MODEL`
- `CLAUDE_CODE_DUMP_AUTO_MODE`

For each var, display its value or "unset".

## `/yolo on`

Set in `~/.claude/settings.json` under `env`:
```json
{
  "CLAUDE_CODE_TWO_STAGE_CLASSIFIER": "thinking",
  "CLAUDE_CODE_AUTO_MODE_MODEL": "claude-sonnet-4-6",
  "CLAUDE_CODE_DUMP_AUTO_MODE": "1"
}
```

Then display:
```
🚀 YOLO mode ON.
   - CLAUDE_CODE_TWO_STAGE_CLASSIFIER=thinking
     → Enables a two-stage safety classifier before auto-mode actions
   - CLAUDE_CODE_AUTO_MODE_MODEL=claude-sonnet-4-6
     → Overrides the model used for auto-mode decisions
   - CLAUDE_CODE_DUMP_AUTO_MODE=1
     → Writes every auto-mode decision to disk for auditing

⚠️  Restart Claude Code for changes to take effect.
```

## `/yolo off`

Remove these keys from the `env` block:
- `CLAUDE_CODE_TWO_STAGE_CLASSIFIER`
- `CLAUDE_CODE_AUTO_MODE_MODEL`
- `CLAUDE_CODE_DUMP_AUTO_MODE`

Confirm: "✅ YOLO config removed. Auto-mode reverts to defaults."

## Important

- Always **merge**, never overwrite the full `env` block.
- Changing the auto-mode model can affect safety and accuracy — warn the user.

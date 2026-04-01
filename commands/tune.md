---
description: Show or apply Claude Code performance tuning profiles (deep-work, speed, privacy, ci-pipeline, multi-agent, debug-session).
argument-hint: "[profile]"
---

# /tune — Claude Code Tuning Profiles

Show the user the available tuning profiles from the `claude-tuning` skill.

## Behavior

When the user runs `/tune` without arguments, display this summary:

| Profile | Use case | Key effect |
|---|---|---|
| `deep-work` | Complex features, architecture | Max reasoning (32k thinking tokens) |
| `speed` | Quick fixes, iteration | Minimal overhead, low effort |
| `privacy` | Sensitive work | Zero telemetry |
| `ci-pipeline` | CI/CD automation | Streamlined output, no UI |
| `multi-agent` | Large tasks | Coordinator mode + parallel tools |
| `debug-session` | Troubleshooting | Full debug logging to disk |

Then ask which profile to apply.

## When user specifies a profile (e.g., `/tune deep-work`)

1. Read the profile definition from the `claude-tuning` skill
2. Show the env vars that will be set
3. Apply them to `~/.claude/settings.json` under the `env` key
4. Confirm what was changed

## Important

- Always **merge** with existing env vars, never overwrite the whole block
- When switching profiles, remove vars from the PREVIOUS profile that aren't in the new one
- The `privacy` profile should warn that it disables auto-updates (security patches)

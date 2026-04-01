# claude-prompt-optimizer

A Claude Code plugin that makes every session sharper — less tokens, more precision, security by default, and performance tuning profiles based on reverse-engineered internals.

## What's Inside

### 1. Prompt Sharpener (`/sharpen`)

A slash command that rewrites raw, vague, or verbose prompts into the prompt-craft formula:

```
[VERB] [WHAT] in [WHERE]. [CONSTRAINT].
```

**Example:**

| Before | After |
|---|---|
| "Could you please help me refactor the auth service?" | "Refactor the auth service. Preserve the public interface." |
| "Eu gostaria que você me ajudasse a criar um login" | "Criar um login. Use o padrão existente no projeto." |

### 2. Session Start Hook

A lightweight `SessionStart` hook that injects a reminder at the beginning of every session: be direct, be specific, and use `/sharpen` when needed.

### 3. Performance Tuning Profiles (Skill + Command)

Pre-built configuration profiles derived from reverse-engineering 494 environment variables in the Claude Code source. Use `/tune` to apply:

| Profile | Use case | Key effect |
|---|---|---|
| `deep-work` | Complex features, architecture | 32k thinking tokens, high effort |
| `speed` | Quick fixes, iteration | Low effort, no overhead |
| `privacy` | Sensitive work | Zero telemetry |
| `ci-pipeline` | CI/CD automation | Streamlined output, no UI |
| `multi-agent` | Large tasks | Coordinator mode + parallel tools |
| `debug-session` | Troubleshooting | Full debug logging to `/tmp/` |
| `api-hacker` | Advanced API manipulation | Inject custom body/metadata to API calls |
| `safety-off` | Trusted/local envs only | Disables command-injection checks (dangerous) |
| `audit-mode` | Reverse engineering Claude | Dumps auto-mode decisions, enables plan verification |

### 4. Power Commands

Commands that expose hidden Claude Code superpowers:

- **`/super`** — Maximum power mode (max effort, 32k thinking, 64k output, 10x concurrency)
- **`/inject`** — Inject arbitrary JSON into every API request body (`CLAUDE_CODE_EXTRA_BODY`)
- **`/yolo`** — Tune the auto-mode safety classifier (two-stage, model override, disk dumps)
- **`/verify`** — Toggle `VerifyPlanExecutionTool` where available
- **`/mode`** — Switch models/providers (Bedrock, Vertex, Opus, fast, custom)
- **`/env`** — Inspect and manage Claude Code environment variables
- **`/swarm`** — Enable experimental Agent Teams (multi-process)
- **`/debug`** — Toggle full debug logging

### 5. CLAUDE.md Templates

Ready-to-use instruction templates based on the actual system prompt sections from the leaked Claude Code source:

- **`CLAUDE.engineer.md`** — Disciplined engineering standards (minimal changes, no speculative abstractions)
- **`CLAUDE.verbose.md`** — Rich, flowing updates for long-running sessions
- **`CLAUDE.minimal.md`** — Absolute minimum chatter for quick tasks
- **`CLAUDE.aggressive.md`** — Challenge assumptions, flag adjacent bugs, act like a peer

Copy any template to your project root as `CLAUDE.md` or `CLAUDE.local.md` to override default Claude behavior.

### 6. Prompt Craft (Skill)

A quick reference for writing effective prompts. The 80/20 of prompt engineering in one page.

## Installation

```bash
# Add the marketplace source and enable the plugin
claude config set extraKnownMarketplaces.prompt-optimizer '{"source":{"source":"github","repo":"cristianoaredes/claude-prompt-optimizer"}}'
claude config set enabledPlugins.prompt-optimizer@prompt-optimizer true
```

Or manually in `~/.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "prompt-optimizer": {
      "source": { "source": "github", "repo": "cristianoaredes/claude-prompt-optimizer" }
    }
  },
  "enabledPlugins": {
    "prompt-optimizer@prompt-optimizer": true
  }
}
```

## Philosophy

> The best prompt engineering for Claude Code isn't a smart rewriter — it's a well-crafted CLAUDE.md and knowing your runtime's hidden knobs.

This plugin doesn't try to be clever. It does four simple things:
1. Sharpens prompts on demand (`/sharpen`)
2. Injects session reminders via hooks
3. Ships quality standards (`CLAUDE.md` templates)
4. Exposes tuning knobs most users don't know exist (documented, categorized, tested)

## Requirements

- Claude Code with plugin support
- Python 3.8+ (for the `SessionStart` hook)

## How It Was Built

The tuning profiles and templates come from a deep reverse-engineering of the Claude Code source (494 `process.env` variables catalogued). Only variables and code paths that work in the **public build** are included — though we also document `ant`-gated features that survive as runtime checks in certain distributions.

## License

MIT

# claude-prompt-optimizer

A Claude Code plugin that makes every session sharper — less tokens, more precision, security by default, and performance tuning profiles based on reverse-engineered internals.

## What's Inside

### 1. Prompt Sharpener (Hook)

A `UserPromptSubmit` hook that strips verbal filler from your prompts before they reach the model.

| You type | Claude receives |
|---|---|
| "Could you please help me refactor the auth service?" | "Refactor the auth service?" |
| "Eu gostaria que você me ajudasse a criar um login" | "Criar um login" |
| "Necesito que implementes autenticación JWT" | "Implementes autenticación JWT" |

Supports English, Portuguese, and Spanish. Only removes padding — never changes your intent.

### 2. Engineering Standards (CLAUDE.md)

Persistent rules injected into every conversation:
- Code quality non-negotiables (input validation, error handling, typed interfaces)
- Security by default (auth, DB, APIs, files — applied automatically)
- Architecture principles (simplicity-first, composition, DI)
- Testing strategy (behavior-based, not implementation-based)
- Git workflow (commit message standards)

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

### 4. Prompt Craft (Skill)

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

This plugin doesn't try to be clever. It does three simple things:
1. Strips filler (60 lines of Python)
2. Ships quality standards (1 markdown file)
3. Exposes tuning knobs most users don't know exist (documented, categorized, tested)

## Requirements

- Claude Code with plugin support
- Python 3.8+ (for the hook)

## How It Was Built

The tuning profiles come from a deep reverse-engineering of the Claude Code source (494 `process.env` variables catalogued). Only variables that work in the **public build** are included — no `ant`-only features that get dead-code-eliminated at build time.

## License

MIT

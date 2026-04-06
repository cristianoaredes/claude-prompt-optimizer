# claude-prompt-optimizer — Claude Code Plugin for Prompt Engineering & AI Tuning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-blue)](https://github.com/cristianoaredes/aredes-marketplace)

A power-user Claude Code plugin: sharpen prompts, run agent workflows, tune performance profiles, and control hidden internals — all from slash commands.

---

## What is this?

**claude-prompt-optimizer** is a Claude Code plugin that gives you direct control over Claude's behavior through 15 slash commands, 2 skills, 9 tuning profiles, and 4 `CLAUDE.md` templates.

It was built by analyzing Claude Code's internal architecture — cataloguing environment variables, reading the system prompt assembly, and studying the hook schema. Every feature here works in the public build.

This is not a prompt rewriter. It is a **control layer**: precise commands that expose knobs Claude Code ships with but doesn't surface by default.

---

## Skills

Two skills are available as Claude Code knowledge bases:

### `prompt-craft`
Quick reference for writing effective Claude Code prompts. Teaches the `[VERB] [WHAT] in [WHERE]. [CONSTRAINT].` formula, identifies what wastes tokens, and clarifies when to add vs. omit context.

### `claude-tuning`
Complete reference for all tuning environment variables, 9 pre-built configuration profiles, feature flag documentation, and instructions for applying settings temporarily or persistently.

---

## Commands

### Prompt Engineering

| Command | What it does |
|---|---|
| `/sharpen <prompt>` | Rewrites a vague or verbose prompt into the `[VERB] [WHAT] in [WHERE]. [CONSTRAINT].` formula. Shows before/after and explains the change. Does not execute the sharpened prompt. |

### Agent-Driven Workflows

| Command | What it does |
|---|---|
| `/build <what to build>` | Full 5-phase development lifecycle: Explore → Plan → Implement → Verify → Report. Spawns subagents for exploration, planning, and adversarial verification. |
| `/refactor <what to refactor>` | Safe 5-phase refactoring: maps blast radius, captures baseline tests, executes one file at a time with checkpoints, verifies all call sites were updated. |
| `/pipeline [test\|lint\|typecheck\|build\|all]` | Local CI. Auto-detects project type (Node, Rust, Go, Python) and runs the appropriate validation chain in sequence with pass/fail reporting per stage. |

### Performance Tuning

| Command | What it does |
|---|---|
| `/tune [profile]` | Apply a pre-built performance profile. Run without arguments to see all profiles. |
| `/super` | Maximum power mode: `EFFORT_LEVEL=max`, 32k thinking tokens, 64k output, 10x tool concurrency. |
| `/chain [wizard\|apply <combo>]` | Macro wizard. Apply stacked configurations (`deep`, `fast`, `swarm`, `audit`, `god`, `privacy`) in one shot, with confirmation before writing. |

### API & Runtime Controls

| Command | What it does |
|---|---|
| `/inject [status\|body JSON\|metadata JSON\|reset]` | Manage `CLAUDE_CODE_EXTRA_BODY` and `CLAUDE_CODE_EXTRA_METADATA` — arbitrary JSON injected into every API request. Deep-merges, never overwrites. |
| `/mode [bedrock\|vertex\|opus\|fast\|set MODEL_ID\|reset]` | Switch model or provider. Supports AWS Bedrock, Google Vertex, and custom model IDs. |
| `/env [list\|set KEY value\|unset KEY\|reset]` | Inspect and manage the `env` block in `~/.claude/settings.json`. |
| `/flags [list\|enable FLAG\|disable FLAG\|reset]` | Control `CLAUDE_INTERNAL_FC_OVERRIDES`. Known working flags: `tengu_thinkback`, `tengu_scratch`, `tengu_tool_pear`, `tengu_amber_flint`. |
| `/swarm [on\|off\|status]` | Enable experimental Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`), which spawns separate Claude processes that communicate with each other. |
| `/yolo [on\|off\|status]` | Tune the auto-mode safety classifier: two-stage mode, model override, and disk auditing of every decision. |
| `/verify [on\|off]` | Toggle `CLAUDE_CODE_VERIFY_PLAN` to enable `VerifyPlanExecutionTool` where available. |
| `/debug [on\|off\|dump\|status]` | Toggle full debug logging: `CLAUDE_DEBUG`, `OTEL_LOG_TOOL_DETAILS`, `CLAUDE_CODE_DUMP_AUTO_MODE`. Logs write to `/tmp/claude-debug/`. |

---

## Tuning Profiles

Use `/tune <profile>` to apply any of these to `~/.claude/settings.json`:

| Profile | Best for | Key effect |
|---|---|---|
| `deep-work` | Architecture, complex features | 32k thinking tokens, high effort, extended timeout |
| `speed` | Quick fixes, high-velocity iteration | Low effort, no telemetry, no cost warnings |
| `privacy` | Sensitive or offline work | Zero telemetry, no auto-updater, no install checks |
| `ci-pipeline` | CI/CD automation | Streamlined output, no terminal UI interference |
| `multi-agent` | Large parallelizable tasks | Coordinator mode, 5x tool concurrency |
| `debug-session` | Troubleshooting Claude behavior | Full debug logs to disk, auto-mode decision dumps |
| `api-hacker` | Advanced API control | Custom body/metadata injection, beta headers |
| `safety-off` | Trusted local environments only | Disables command injection check, fast classifier |
| `audit-mode` | Reverse engineering internals | Dumps auto-mode decisions, plan verification |

---

## CLAUDE.md Templates

Four templates are included in `templates/`. Copy any one to your project root as `CLAUDE.md` or `CLAUDE.local.md` to override Claude's default behavior:

| Template | Best for |
|---|---|
| `CLAUDE.engineer.md` | Disciplined engineering: minimal changes, no speculative abstractions, verify before claiming success |
| `CLAUDE.verbose.md` | Rich updates for long-running sessions |
| `CLAUDE.minimal.md` | Absolute minimum chatter for quick tasks |
| `CLAUDE.aggressive.md` | Challenge assumptions, flag adjacent bugs, act like a peer engineer |

---

## Hooks (Optional)

Two hook implementations are included in `hooks/` but are not registered automatically (to avoid marketplace validation errors):

- **`session-inject.py`** (`SessionStart`) — Injects a reminder at the start of every session: be direct, be specific, use `/sharpen` when needed.
- **`post-tool-guard.py`** (`PostToolUse`) — Nudges after key actions: run tests after `FileWriteTool`, confirm intent after destructive `BashTool`, review findings after `AgentTool`.

To activate them manually:

```bash
cp hooks/session-inject.py ~/.claude/hooks/prompt-optimizer-session-start.py
chmod +x ~/.claude/hooks/prompt-optimizer-session-start.py
cp hooks/post-tool-guard.py ~/.claude/hooks/prompt-optimizer-post-tool.py
chmod +x ~/.claude/hooks/prompt-optimizer-post-tool.py
```

---

## Installation

### Via aredes-marketplace

Browse and install from the [aredes-marketplace](https://github.com/cristianoaredes/aredes-marketplace).

### Direct install

```bash
git clone https://github.com/cristianoaredes/claude-prompt-optimizer.git
cd claude-prompt-optimizer
./install.sh
```

Then restart Claude Code:

```bash
exit && claude
```

The install script:
1. Copies the plugin to `~/.claude/plugins/cache/prompt-optimizer/`
2. Symlinks all 15 commands into `~/.claude/.claude/commands/`
3. Cleans up any stale plugin registration in `installed_plugins.json` and `settings.json` to prevent marketplace validation errors

### Requirements

- Claude Code with plugin support
- Python 3.8+ (only if you install the optional hooks)

---

## Usage Examples

```
# Sharpen a vague prompt before sending it
/sharpen "can you make the login faster"

# Apply maximum reasoning for a complex task
/super

# Stack deep-work + thinking flags in one shot
/chain apply deep

# Run full CI validation for your project
/pipeline all

# Build a feature with full agent lifecycle
/build "add rate limiting to POST /api/upload"

# Safe refactoring with blast-radius analysis
/refactor "AuthService to use dependency injection"

# Apply a performance profile
/tune deep-work

# Enable internal feature flags
/flags enable tengu_thinkback
/flags enable tengu_scratch

# Inspect current environment variables
/env
```

---

## SEO Keywords

Claude Code plugin · prompt optimizer · prompt engineering · CLAUDE.md · AI prompt tuning · Claude skills · Claude Code tuning · agent workflow · prompt sharpener · Claude Code slash commands · Claude Code performance · AI engineering productivity

---

## License

MIT — see [LICENSE](LICENSE).

---

by [Cristiano Arêdes](https://github.com/cristianoaredes) · [aredes-marketplace](https://github.com/cristianoaredes/aredes-marketplace)

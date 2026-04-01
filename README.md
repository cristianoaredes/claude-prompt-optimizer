# claude-prompt-optimizer

> A power-user toolkit for Claude Code. Reverse-engineered from 494 environment variables and the actual system prompt architecture of the leaked source.

This isn't a prompt rewriter. It's a **control layer** that exposes Claude Code's hidden knobs, injects session intelligence via hooks, ships battle-tested `CLAUDE.md` templates, and runs full agent-driven workflows.

---

## What You Get

### 1. `/sharpen` — Prompt Optimizer

Rewrite vague prompts into the formula that Claude Code actually prefers:

```
[VERB] [WHAT] in [WHERE]. [CONSTRAINT].
```

| Before | After |
|---|---|
| "Could you please help me refactor the auth service?" | "Refactor the auth service. Preserve the public interface." |
| "i want you to make the api faster" | "Optimize response latency on GET /api/search. Target <200 ms p95 without changing the public interface." |

---

### 2. Hooks — Silent Session Intelligence

Two hooks that run automatically, derived from the actual Claude Code hook schema (`src/types/hooks.ts`):

- **`SessionStart`** — Injects a reminder at the beginning of every session: be direct, be specific, use `/sharpen` when needed.
- **`PostToolUse`** — Nudges the model after key actions:
  - After `FileWriteTool`: "Consider running relevant tests before moving on."
  - After destructive `BashTool`: "Confirm this was intentional."
  - After `AgentTool`: "Review the agent's findings carefully before the next step."

> **Why this works:** The old `UserPromptSubmit` hook tried to return `updatedPrompt`, a field that **does not exist** in the Claude Code schema. We fixed it by using `SessionStart` with `initialUserMessage` — a primitive that actually survives validation.

---

### 3. Workflow Orchestrators

Commands that drive multi-phase work using `AgentTool`, `TaskCreateTool`, and the main-thread tool loop:

#### `/build <what to build>`
A full agent-driven development lifecycle:
1. **Explore** — `AgentTool` with `subagent_type="Explore"` maps the codebase
2. **Plan** — `AgentTool` with `subagent_type="Plan"` creates a detailed implementation plan
3. **Implement** — You execute with `FileEditTool` / `FileWriteTool`
4. **Verify** — `AgentTool` with `subagent_type="verification"` performs adversarial review
5. **Report** — Summarize findings, verdict, and risks

#### `/refactor <what to refactor>`
Safe refactoring with blast-radius awareness:
1. **Explore Impact** — Map all call sites and tests
2. **Plan** — File-by-file edit sequence with checkpoints
3. **Safety Check** — Baseline test run before touching code
4. **Execute** — Incremental edits with validation every 2-3 files
5. **Verify** — Full test run + verification agent review

#### `/pipeline [test|lint|typecheck|build|all]`
Local CI. Auto-detects your project type (Node, Rust, Go, Python) and runs the appropriate validation chain in order: **test → lint → typecheck → build**.

#### `/chain [wizard|apply <combo>]`
Macro wizard. Applies stacked configurations in one shot:

| Combo | Effect |
|---|---|
| `deep` | `deep-work` + max thinking + `tengu_scratch` + `tengu_thinkback` |
| `fast` | `speed` + low effort + no telemetry |
| `swarm` | Agent Teams + Coordinator Mode + 10x concurrency |
| `audit` | Debug dumps + YOLO classifier logs + plan verification |
| `god` | `/super` + swarm + `tengu_amber_flint` + `tengu_tool_pear` |
| `privacy` | Zero telemetry, no auto-updater, no installation checks |

---

### 4. Power Commands — Hidden Knobs Exposed

Commands derived from reverse-engineering the Claude Code source:

- **`/super`** — Maximum power mode (`EFFORT_LEVEL=max`, 32k thinking, 64k output, 10x concurrency)
- **`/inject`** — Manage `CLAUDE_CODE_EXTRA_BODY` and `CLAUDE_CODE_EXTRA_METADATA` (injected into every API request)
- **`/yolo`** — Tune the auto-mode safety classifier (two-stage, model override, disk auditing)
- **`/verify`** — Toggle `CLAUDE_CODE_VERIFY_PLAN` (enables `VerifyPlanExecutionTool` where available)
- **`/mode`** — Switch models/providers (Bedrock, Vertex, Opus, fast, custom)
- **`/env`** — Inspect and manage environment variables in `settings.json`
- **`/swarm`** — Enable experimental Agent Teams
- **`/debug`** — Toggle full debug logging

---

### 5. Tuning Profiles — 9 Pre-Built Configs

Use `/tune <profile>` to apply:

| Profile | For | Key effect |
|---|---|---|
| `deep-work` | Architecture, complex features | 32k thinking, high effort, anti-flicker |
| `speed` | Quick fixes | Low effort, no telemetry, no cost warnings |
| `privacy` | Sensitive work | Zero telemetry, no auto-updater |
| `ci-pipeline` | Automation | Streamlined output, no UI interference |
| `multi-agent` | Large tasks | Coordinator mode + parallel tools |
| `debug-session` | Troubleshooting | Full debug logs to `/tmp/` |
| `api-hacker` | Advanced API control | Inject custom body/metadata + beta headers |
| `safety-off` | ⚠️ Trusted envs only | Disables command-injection checks |
| `audit-mode` | Reverse engineering | Dumps auto-mode decisions, plan verification |

---

### 6. CLAUDE.md Templates — Override the System Prompt

These templates are derived from the **actual sections** of the Claude Code system prompt (`src/constants/prompts.ts`). Because `CLAUDE.md` instructions override default behavior, these are high-leverage:

- **`CLAUDE.engineer.md`** — Disciplined engineering standards (minimal changes, no speculative abstractions, verify before claiming success)
- **`CLAUDE.verbose.md`** — Rich, flowing updates for long-running sessions
- **`CLAUDE.minimal.md`** — Absolute minimum chatter for quick tasks
- **`CLAUDE.aggressive.md`** — Challenge assumptions, flag adjacent bugs, act like a peer engineer

Copy any template to your project root as **`CLAUDE.md`** or **`CLAUDE.local.md`** to activate it.

---

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

---

## Requirements

- Claude Code with plugin support
- Python 3.8+ (for the `SessionStart` and `PostToolUse` hooks)

---

## How It Was Built

This plugin was built by analyzing the **leaked Claude Code source** (March 2026), cataloguing 494 `process.env` variables, reading the actual system prompt assembly in `src/constants/prompts.ts`, and studying the hook schema in `src/types/hooks.ts`.

We only include variables and code paths that work in the **public build**, though we also document features gated by runtime checks that may survive in certain distributions.

---

## License

MIT

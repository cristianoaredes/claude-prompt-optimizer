# CLAUDE.md Templates

A collection of ready-to-use Claude Code instruction templates.

## Which template to use

| Template | Best for |
|----------|----------|
| `CLAUDE.engineer.md` | Everyday coding tasks. Keeps changes minimal, avoids speculative abstractions, and enforces verification before claiming success. |
| `CLAUDE.verbose.md` | Long-running or complex sessions where the user may step away. Provides fuller context and flowing prose. |
| `CLAUDE.minimal.md` | Quick queries and well-defined micro-tasks. Reduces chatter to the absolute minimum. |
| `CLAUDE.aggressive.md` | Users who want Claude to challenge assumptions, flag adjacent bugs, and act like a peer engineer. |

## How to install

1. Choose one or more templates.
2. Copy them into your project root as **`CLAUDE.md`** or **`CLAUDE.local.md`**.
3. Claude Code will automatically pick them up and apply the instructions to all interactions in that project.

You can also place them under **`.claude/rules/*.md`** for multi-file organization.

## Mix and match

These templates are written as standalone sections. Feel free to combine them:
- Use `CLAUDE.engineer.md` + `CLAUDE.minimal.md` for no-nonsense, disciplined engineering.
- Use `CLAUDE.engineer.md` + `CLAUDE.verbose.md` when working on complex features with a user who wants rich updates.
- Add `CLAUDE.aggressive.md` on top of any base template to increase assertiveness.

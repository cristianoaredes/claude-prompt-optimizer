---
name: prompt-craft
description: Quick reference for writing effective Claude Code prompts.
user-invocable: true
---

# Prompt Craft — Quick Reference

## The 80/20

The CLAUDE.md handles quality standards, security, and engineering principles
automatically. You don't need to repeat them. Your job is to be **specific about intent**.

## Formula

```
[VERB] [WHAT] in [WHERE]. [CONSTRAINT].
```

Examples:
- `Implement rate limiting on POST /api/upload. Max 10 req/min per IP.`
- `Refactor AuthService to use dependency injection. Keep the public interface.`
- `Investigate the timeout on /api/search. Hypothesis: N+1 query in UserRepository.`

## What Wastes Tokens

| Wastes tokens | Free alternative |
|---|---|
| Describing a pattern that exists in your codebase | "Follow the pattern in `AuthService`" |
| Asking Claude to explain what it will do | Just tell it to do it |
| "Could you please..." | "Implement X in Y" |
| Repeating what's already in CLAUDE.md | It's already in the system prompt |

## When to Add Context

- **Debug:** include the exact error or stack trace
- **New feature:** reference something similar that already exists
- **Refactor:** say what must NOT change

## When NOT to Add Context

- Claude already has workspace access — don't describe directory structure
- Security rules are in CLAUDE.md — don't repeat them
- If a project-level CLAUDE.md exists, local patterns are already loaded

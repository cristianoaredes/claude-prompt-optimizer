# Engineering Standards

These standards are injected into every Claude Code conversation via CLAUDE.md.
They ensure consistent quality without repeating rules in every prompt.

## Engineering Principles
- **Deliver value, not complexity.** Every abstraction must justify its existence.
- **Prefer boring technology.** Use proven patterns over clever solutions.
- **Smallest viable change.** Don't refactor what doesn't need refactoring.
- **Errors are first-class citizens.** Handle them explicitly; never swallow exceptions.
- **Security by default.** Validate inputs, sanitize outputs, use parameterized queries.

## Code Quality — Non-Negotiable
Before writing any implementation:
1. Check for existing patterns in the codebase first — follow them.
2. Validate all external inputs at system boundaries (zod, joi, or equivalent).
3. Handle errors explicitly — no empty catch blocks, no silent failures.
4. Use typed interfaces over `any`. If a type is unknown, narrow it.
5. Write code that reads top-down. If a function needs a comment to explain *what* it does, rename it.

## Security — Embedded, Not Bolted On
Apply these automatically without being asked:
- **Auth:** constant-time token comparison, generic error messages (401/403), never leak internal details.
- **Database:** parameterized queries only. Transactions for multi-step writes with rollback.
- **APIs:** explicit timeouts, retry with backoff for 429/5xx, secrets from env vars only.
- **Files:** validate MIME server-side, sanitize filenames, enforce size limits.
- **Never** hardcode secrets, disable TLS verification, or use `eval`/`exec` on user input.

## Architecture Decisions
- Start with the simplest architecture that works. Add layers only when pain appears.
- Prefer composition over inheritance.
- Prefer explicit dependency injection over global state.
- One responsibility per module. If you can't name it in 3 words, it's doing too much.

## Testing Strategy
- Test behavior, not implementation. Tests should survive refactors.
- Cover the happy path + one error path + one edge case. Not every permutation.
- Integration tests for critical paths (auth, payments, data integrity).
- Don't mock what you don't own — use test doubles for your own interfaces.

## Git Workflow
- Commit messages: imperative mood, lowercase, no period. Max 72 chars.
  - Good: `add jwt refresh token rotation`
  - Bad: `Added JWT refresh token rotation feature.`
- One logical change per commit.

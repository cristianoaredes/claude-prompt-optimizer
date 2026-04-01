---
description: Safe refactoring workflow — explore impact, plan changes, execute with checkpoints, and verify.
argument-hint: "<what to refactor>"
---

# /refactor — Safe Refactoring Workflow

Executes a disciplined, reversible refactoring using the Explore → Plan → Implement → Test → Verify cascade.

## The 5-Phase Protocol

### Phase 1: Explore Impact
**Goal:** Find every file, test, and dependency affected by the refactoring.

1. Create task `"refactor-impact"` (status `in_progress`)
2. Use `AgentTool` with `subagent_type`: `"Explore"` to map the blast radius.
3. Specifically ask the agent to find:
   - All call sites of the function/class being refactored
   - All tests that exercise it
   - Any configuration, types, or interfaces that reference it
4. Summarize findings and mark task `completed`.

### Phase 2: Plan Refactoring
**Goal:** Define the exact sequence of edits.

1. Create task `"refactor-plan"` (status `in_progress`)
2. Use `AgentTool` with `subagent_type`: `"Plan"` to produce a refactoring plan.
3. The plan MUST include:
   - Pre-refactoring safety checks (e.g., "all tests pass before changes")
   - Exact file-by-file edit sequence
   - Post-refactoring validation steps
4. Review with the user if the plan touches >5 files or changes public APIs.
5. Mark task `completed`.

### Phase 3: Safety Check
**Goal:** Capture baseline state.

1. Create task `"refactor-safety"` (status `in_progress`)
2. Run the relevant test suite (or lint/typecheck if no tests exist).
3. If baseline fails, report it and ask the user whether to proceed or fix baseline first.
4. Mark task `completed`.

### Phase 4: Execute
**Goal:** Apply the planned edits incrementally.

1. Create task `"refactor-execute"` (status `in_progress`)
2. Execute the plan **one file at a time**.
3. After every 2-3 files, run a quick validation (tests, lint, or typecheck).
4. If a validation fails, stop, diagnose, and fix before continuing.
5. Mark task `completed`.

### Phase 5: Verify
**Goal:** Confirm the refactoring is safe and complete.

1. Create task `"refactor-verify"` (status `in_progress`)
2. Run the full test suite (or lint/typecheck).
3. Use `AgentTool` with `subagent_type`: `"verification"` to review:
   - That all call sites were updated
   - That no dead code was left behind
   - That types and interfaces remain consistent
4. Report the verifier verdict faithfully.
5. Mark task `completed` and summarize the changes.

## Safety Rules

- **Prefer editing over creating.** Refactoring should reshape existing code, not bloat the codebase.
- **Never delete without verifying usage first.** Use Grep to confirm a symbol is unused before removing it.
- **Preserve public interfaces unless the plan explicitly changes them.**
- If at any point the scope grows beyond what the user asked, pause and confirm.

---
description: Full agent-driven build workflow — explore, plan, implement, and verify in one command.
argument-hint: "<what to build>"
---

# /build — Agent-Driven Build Workflow

Executes a complete software development lifecycle using Claude Code's built-in agent types as a cascade.

## The 5-Phase Protocol

When the user runs `/build <what to build>`, you MUST follow this exact workflow. Do not skip phases.

### Phase 1: Explore
**Goal:** Understand the codebase context relevant to the request.

1. Create a persistent task using `TaskCreateTool`:
   - `taskListId`: `"build-workflow"`
   - `title`: `"Phase 1: Explore codebase"`
   - `status`: `"in_progress"`
2. Spawn an **Explore agent** via `AgentTool` with:
   - `subagent_type`: `"Explore"`
   - `prompt`: A focused request to find all relevant files, patterns, and existing implementations for `<what to build>`
3. Summarize the explore findings in 2-3 sentences.
4. Update the task status to `"completed"`.

### Phase 2: Plan
**Goal:** Produce a detailed, actionable implementation plan.

1. Create a task: `"Phase 2: Plan implementation"` (status `in_progress`)
2. Spawn a **Plan agent** via `AgentTool` with:
   - `subagent_type`: `"Plan"`
   - `prompt`: The explore findings + a request for a step-by-step implementation plan with specific files to modify/create
3. Review the plan. If it is too vague or misses critical files, ask the user before proceeding.
4. Update the task to `completed`.

### Phase 3: Implement
**Goal:** Execute the plan using your main-thread tools.

1. Create a task: `"Phase 3: Implement"` (status `in_progress`)
2. Work through the plan **one step at a time**:
   - Read files before modifying
   - Use `FileEditTool` or `FileWriteTool`
   - Run tests or validation commands after significant changes
3. If you get stuck or the plan needs major revision, pause and ask the user.
4. Update the task to `completed`.

### Phase 4: Verify
**Goal:** Independent adversarial verification of the implementation.

1. Create a task: `"Phase 4: Verify implementation"` (status `in_progress`)
2. Spawn a **verification agent** via `AgentTool` with:
   - `subagent_type`: `"verification"`
   - `prompt`: The original request, the plan, all files changed, and instructions to verify correctness, edge cases, and test coverage
3. Report the verifier's findings **faithfully**:
   - If PASS: briefly confirm and spot-check 2-3 commands from the verifier's report
   - If FAIL: report the issues, fix them, and re-run the verifier
   - If PARTIAL: report what passed and what could not be verified
4. Update the task to `completed`.

### Phase 5: Report
**Goal:** Present the outcome to the user.

1. Create a final task: `"Build workflow complete"` (status `completed`)
2. Summarize:
   - What was built
   - Key files changed
   - Verifier verdict
   - Any remaining risks or follow-ups

## Important Rules

- **Never skip the verification agent.** You are the one reporting to the user; you own the gate.
- **Use `TaskCreateTool` for every phase.** This makes the workflow durable and transparent.
- **If `AgentTool` with `subagent_type` fails** (e.g., the agent type is unavailable in this build), fall back to doing the phase yourself with main-thread tools and note the fallback to the user.
- Do not batch multiple plan steps before confirming progress with the user.

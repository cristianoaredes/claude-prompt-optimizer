# Engineering Standards

## 🚫 Negative Constraints (CRITICAL)
- NEVER invent, hallucinate, or guess methods/properties. ALWAYS check the source code first.
- NEVER edit files blindly. ALWAYS run tools to read/search the file before applying edits to ensure you know the target structure.
- NEVER add features or refactor code beyond what was explicitly asked.
- NEVER add docstrings, comments, or type annotations to code you didn't change.
- NEVER add error handling, fallbacks, or validation for scenarios that mathematically or logically cannot happen.
- NEVER create generic helpers, utilities, or abstractions for one-time operations. Do not over-engineer.
- NEVER design for hypothetical future requirements.

## 🛠 Actions & Tool Usage
- ALWAYS carefully consider reversibility and blast radius before running bash commands.
- For destructive actions (rm -rf, git push, database changes), ALWAYS confirm with the user first.
- Resolve merge conflicts directly in the file rather than discarding changes.
- If you find a lock file, investigate what holds it rather than blindly deleting it.

## 🧪 Verification
- ALWAYS verify your code actually works before reporting completion. Run tests, execute scripts, check output.
- If you cannot verify, STATE SO EXPLICITLY rather than claiming success.
- Report outcomes faithfully: if tests fail or a bash command returns an error, say so with the relevant output.

# Engineering Standards

## Code Style
- Don't add features, refactor code, or make "improvements" beyond what was asked.
- A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't need extra configurability.
- Don't add docstrings, comments, or type annotations to code you didn't change.
- Only add comments where the logic isn't self-evident or encodes a hidden constraint.
- Don't add error handling, fallbacks, or validation for scenarios that can't happen.
- Only validate at system boundaries (user input, external APIs).
- Don't use feature flags or backwards-compatibility shims when you can just change the code.
- Don't create helpers, utilities, or abstractions for one-time operations.
- Don't design for hypothetical future requirements.

## Actions
- Carefully consider reversibility and blast radius.
- For destructive actions (rm -rf, git push, database changes), always confirm first.
- Resolve merge conflicts rather than discarding changes.
- If you find a lock file, investigate what holds it rather than deleting it.

## Verification
- Before reporting completion, verify it actually works: run tests, execute scripts, check output.
- If you can't verify, say so explicitly rather than claiming success.
- Report outcomes faithfully: if tests fail, say so with the relevant output.

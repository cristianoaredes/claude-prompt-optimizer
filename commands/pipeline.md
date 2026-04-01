---
description: Run a local CI-like pipeline — tests, lint, typecheck, build — in sequence with per-stage reporting.
argument-hint: "[test|lint|typecheck|build|all]"
---

# /pipeline — Local CI Pipeline

Runs a sequence of validation commands like a CI pipeline, reporting pass/fail for each stage.

## Behavior

### `/pipeline` (no args)

Detect the project type and run the default pipeline:

| Detected | Stages |
|---|---|
| `package.json` present with `test` script | `npm test` → `npm run lint` (or biome/eslint) → `npx tsc --noEmit` |
| `Cargo.toml` | `cargo test` → `cargo clippy` → `cargo check` |
| `go.mod` | `go test ./...` → `go vet ./...` → `go build ./...` |
| Python with `pytest` | `pytest` → `ruff check .` (or `flake8`) → `mypy .` |
| `Makefile` with `test` target | `make test` |

### `/pipeline test`
Run only the test stage.

### `/pipeline lint`
Run only the lint stage.

### `/pipeline typecheck`
Run only the typecheck stage.

### `/pipeline build`
Run only the build stage.

### `/pipeline all`
Explicitly run all detected stages in order.

## Execution Protocol

For each stage:
1. Announce the stage name.
2. Run the command via `BashTool`.
3. Report the result:
   - **PASS** (exit 0): green check, 1-line summary
   - **FAIL** (exit != 0): red X, show the first 20 lines of stderr/stdout that explain the failure
   - **SKIP**: if the stage has no detectable command
4. If any stage FAILS:
   - Stop the pipeline (fail-fast)
   - Show a summary of which stage failed
   - Do not proceed to subsequent stages
5. If all stages PASS:
   - Show a summary table

## Example Output

```
✅ test    — 42 tests passed
✅ lint    — no issues
✅ typecheck — no errors
❌ build   — failed with exit code 1

Pipeline halted at build stage.
```

## Important

- Always run stages in the order: **test → lint → typecheck → build**
- Use `BashTool` with a timeout of 120s per stage.
- If a stage command is not found, skip it rather than fail.
- Do not attempt to auto-fix failures unless explicitly asked.

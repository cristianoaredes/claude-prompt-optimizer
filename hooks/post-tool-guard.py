#!/usr/bin/env python3
"""PostToolUse hook — injects workflow nudges based on which tool just ran.

No dependencies beyond Python 3.8+ stdlib.
"""

import json
import sys


def is_destructive_bash(command: str) -> bool:
    destructive = ["rm -rf", "drop ", "delete from", "truncate ", "kill -9", "dd if="]
    cmd_lower = command.lower()
    return any(d in cmd_lower for d in destructive)


def get_nudge(event: dict) -> str | None:
    tool_name = event.get("tool_name", "")
    tool_input = event.get("tool_input", {}) or {}
    tool_output = event.get("tool_output", "")

    if tool_name in ("FileWriteTool", "FileWrite"):
        path = tool_input.get("path", "")
        return (
            f"You just wrote to {path}. "
            "If there are relevant tests, consider running them before moving on. "
            "Also verify the file has no syntax errors."
        )

    if tool_name in ("FileEditTool", "FileEdit"):
        path = tool_input.get("path", "")
        return (
            f"You just edited {path}. "
            "Verify the edit didn't break syntax or imports. "
            "If tests exist for this file, consider running them."
        )

    if tool_name in ("BashTool", "Bash"):
        command = tool_input.get("command", "")
        if is_destructive_bash(command):
            return (
                "⚠️ You just ran a potentially destructive bash command. "
                "Confirm this was intentional and that no unintended data was lost."
            )
        if "git push" in command or "git push --force" in command:
            return (
                "You just pushed code. Ensure the push was to the correct branch "
                "and that CI checks are expected to pass."
            )

    if tool_name in ("AgentTool", "Agent"):
        agent_type = tool_input.get("subagent_type", "general-purpose")
        return (
            f"The {agent_type} agent has returned its findings. "
            "Review the output carefully before proceeding to the next step. "
            "If the agent's findings are incomplete or unclear, consider spawning another agent with a more specific prompt."
        )

    if tool_name in ("TaskCreateTool", "TaskCreate"):
        return (
            "A new task was created. Keep the task list updated as you complete steps. "
            "Mark tasks completed promptly rather than batching updates."
        )

    return None


def main():
    try:
        event = json.loads(sys.stdin.read())
        nudge = get_nudge(event)

        if nudge:
            json.dump(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "PostToolUse",
                        "additionalContext": nudge,
                    }
                },
                sys.stdout,
                ensure_ascii=False,
            )
        else:
            print("{}")
    except Exception:
        print("{}")


if __name__ == "__main__":
    main()

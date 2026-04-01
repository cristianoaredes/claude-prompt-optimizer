#!/usr/bin/env python3
"""SessionStart hook — injects a lightweight reminder at session start.

No dependencies beyond Python 3.8+ stdlib.
"""

import json
import os
import sys


def main():
    try:
        plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
        config_path = (
            os.path.join(plugin_root, ".claude-plugin", "plugin.json")
            if plugin_root
            else ""
        )

        plugin_name = "prompt-optimizer"
        if config_path and os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                plugin_name = cfg.get("name", plugin_name)

        initial_user_message = (
            "Session reminder: be direct and specific. "
            "Use the /sharpen command if you want help optimizing a prompt."
        )
        additional_context = (
            f"Plugin '{plugin_name}' is active. "
            "It provides prompt-craft guidance, tuning profiles, and the /sharpen command."
        )

        json.dump(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "initialUserMessage": initial_user_message,
                    "additionalContext": additional_context,
                }
            },
            sys.stdout,
            ensure_ascii=False,
        )
    except Exception:
        print("{}")


if __name__ == "__main__":
    main()

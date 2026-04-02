#!/usr/bin/env python3
"""PostToolUseFailure hook — intercepts tool execution errors to auto-correct the LLM.

No dependencies beyond Python 3.8+ stdlib.
"""

import json
import sys


def generate_correction(tool_name: str, tool_input: dict, error: str) -> str:
    """Generates an immediate negative constraint based on the failure text."""
    error_lower = error.lower()
    
    if tool_name in ("BashTool", "Bash"):
        command = tool_input.get("command", "")
        
        # Directory issues
        if "no such file or directory" in error_lower or "not found" in error_lower:
            return (
                "SYSTEM (AUTO-CORRECTION): Your bash command failed due to a missing file or directory.\n"
                "NEVER blindly guess paths again. ALWAYS run `list_dir` or `ls` first to verify the current "
                "directory structure before attempting to access files or run project-specific scripts."
            )
            
        # Permission issues
        if "permission denied" in error_lower:
            return (
                "SYSTEM (AUTO-CORRECTION): Permission denied.\n"
                "Do NOT attempt to run this exact command again without ensuring you have the necessary permissions "
                "(e.g., using sudo if completely unavoidable, checking file mod, or using a different path)."
            )
            
        # Package manager issues (often run in wrong dir)
        if "could not find a pubspec.yaml" in error_lower or "package.json not found" in error_lower:
            return (
                "SYSTEM (AUTO-CORRECTION): You ran a package manager command in a directory without the manifest file.\n"
                "NEVER run `pub`, `npm`, `yarn`, etc. without verifying you are in the correct project root.\n"
                "Find the project root first, then run the command passing the correct `cwd` or `cd` into it."
            )

    elif tool_name in ("FileEditTool", "FileEdit", "ReplaceFileContent"):
        # Targeting issues replacing exact strings
        if "could not successfully apply any edits" in error_lower or "target content not found" in error_lower:
            return (
                "SYSTEM (AUTO-CORRECTION): Your file edit failed because the target string was not exact.\n"
                "NEVER try to guess the target string. ALWAYS read the file contents using `view_file` beforehand, "
                "copy the exact lines to replace, and ensure you include identical whitespace/indentation."
            )

    # Generic fallback auto-correction
    return (
        "SYSTEM (AUTO-CORRECTION): Your previous tool use failed with the error above.\n"
        "NEVER retry the exact same approach blindly. Pause, analyze the error, and verify your assumptions "
        "before making a new attempt."
    )


def main():
    try:
        input_data = json.loads(sys.stdin.read())
        tool_name = input_data.get("tool_name", "")
        tool_input = input_data.get("tool_input", {})
        error = input_data.get("error", "")
        
        if not tool_name or not error:
            print("{}")
            return
            
        correction = generate_correction(tool_name, tool_input, error)

        # Inject additionalContext with the specific correction
        json.dump(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUseFailure",
                    "additionalContext": correction,
                }
            },
            sys.stdout,
            ensure_ascii=False,
        )
    except Exception:
        print("{}")


if __name__ == "__main__":
    main()

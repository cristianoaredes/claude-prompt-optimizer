#!/usr/bin/env python3
"""UserPromptSubmit hook — classifies user intent and injects negative constraints.

No dependencies beyond Python 3.8+ stdlib.
"""

import json
import sys
import re


def classify_intent(prompt: str) -> str:
    """Classifies the prompt to determine the likely intent."""
    prompt_lower = prompt.lower()
    
    # Feature / Coding intent words
    code_intent_keywords = [
        "create", "build", "implement", "add", "make", "write", 
        "refactor", "update", "change", "edit", "fix", "resolve", "bug"
    ]
    
    # Query / Analysis intent words
    query_intent_keywords = [
        "explain", "how", "why", "where", "what", "find", 
        "analyze", "review", "check", "look", "read", "search"
    ]
    
    # Evaluate matches
    code_matches = sum(1 for word in code_intent_keywords if re.search(r"\b" + word + r"\b", prompt_lower))
    query_matches = sum(1 for word in query_intent_keywords if re.search(r"\b" + word + r"\b", prompt_lower))
    
    if code_matches > 0 and code_matches >= query_matches:
        return "CODE_INTENT"
    elif query_matches > code_matches:
        return "QUERY_INTENT"
    
    # Default to code intent for safety and stricter constraints
    return "CODE_INTENT"


def get_constraints(intent: str) -> str:
    """Returns the negative constraints appropriate for the classified intent."""
    if intent == "CODE_INTENT":
        return (
            "SYSTEM REMINDER (CODE INTENT DETECTED):\n"
            "- NEVER invent or hallucinate methods/properties. ALWAYS check the source code first.\n"
            "- NEVER edit files blindly. ALWAYS read/search the file before applying edits to ensure you know the target structure.\n"
            "- NEVER assume a file's location. ALWAYS verify the path first.\n"
            "- ONLY implement what was explicitly asked. Do not over-engineer or add hypothetical future requirements.\n"
            "- ALWAYS run tests or execute verification scripts before reporting completion."
        )
    else:
        return (
            "SYSTEM REMINDER (QUERY INTENT DETECTED):\n"
            "- DO NOT make any code modifications unless explicitly asked to do so later.\n"
            "- ALWAYS use read-only robust search tools (`grep_search`, `list_dir`, `view_file`) comprehensively to answer the query.\n"
            "- Provide direct, concise answers without hallucinating implementation details."
        )


def extract_and_save_trauma(prompt: str) -> str:
    """Extracts trauma/learn rules and saves to global memory."""
    match = re.match(r"^(?:learn|trauma):\s*(.*)", prompt, re.IGNORECASE | re.DOTALL)
    if match:
        rule = match.group(1).strip()
        if rule:
            import os
            trauma_dir = os.path.expanduser("~/.claude")
            os.makedirs(trauma_dir, exist_ok=True)
            trauma_path = os.path.join(trauma_dir, "global_traumas.md")
            
            with open(trauma_path, "a", encoding="utf-8") as f:
                f.write(f"- {rule}\n")
                
            return (
                "SYSTEM (TRAUMA MEMORY SAVED):\n"
                f"You successfully saved the following rule to global memory: '{rule}'\n"
                "Acknowledge this to the user and confirm that you will remember this in the future."
            )
    return None

def main():
    try:
        # UserPromptSubmit hook receives a JSON object on stdin
        input_data = json.loads(sys.stdin.read())
        prompt = input_data.get("prompt", "")
        
        if not prompt:
            print("{}")
            return
            
        trauma_context = extract_and_save_trauma(prompt)
        
        if trauma_context:
            constraints = trauma_context
        else:
            intent = classify_intent(prompt)
            constraints = get_constraints(intent)

        # We return additionalContext to be injected into the system prompt for this turn
        json.dump(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": constraints,
                }
            },
            sys.stdout,
            ensure_ascii=False,
        )
    except Exception:
        # In case of any error, fail silently by returning empty JSON
        print("{}")


if __name__ == "__main__":
    main()

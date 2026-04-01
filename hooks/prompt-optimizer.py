#!/usr/bin/env python3
"""
prompt-optimizer — Lightweight prompt sharpener for Claude Code.

Does ONE thing: strips verbal padding from prompts.
Quality standards, security, patterns → live in CLAUDE.md, not here.

No dependencies beyond Python 3.8+ stdlib.
"""

import json, sys, re

# Filler prefixes that waste tokens (order: longer matches first)
FILLER = [
    # Portuguese — long phrases first
    r"(?i)^(eu\s+)?(gostaria\s+que\s+voc[eê]\s+(me\s+ajudasse\s+a\s+)?)",
    r"(?i)^(eu\s+)?(precisaria\s+que\s+voc[eê]\s+(me\s+ajudasse\s+a\s+)?)",
    r"(?i)^(eu\s+)?(preciso\s+que\s+voc[eê]\s+)",
    r"(?i)^(eu\s+)?(quero\s+que\s+voc[eê]\s+)",
    r"(?i)^(voc[eê]\s+poderia\s+(me\s+ajudar\s+a\s+)?)",
    r"(?i)^(pode\s+por\s+favor|por\s+favor)\s+",
    r"(?i)^me\s+ajud[ea]\s+a\s+",
    r"(?i)^poderia\s+me\s+(ajudar\s+a\s+)?",
    # English
    r"(?i)^(i\s+need\s+you\s+to|could\s+you\s+please|can\s+you\s+please|please)\s+",
    r"(?i)^(i\s+would\s+like\s+you\s+to|i\s+want\s+you\s+to)\s+",
    r"(?i)^(help\s+me\s+to|help\s+me)\s+",
    # Spanish
    r"(?i)^(me\s+gustar[ií]a\s+que\s+)",
    r"(?i)^(necesito\s+que\s+)",
    r"(?i)^(podr[ií]as?\s+(ayudarme\s+a\s+)?)",
    r"(?i)^(por\s+favor\s+)",
]

def strip_filler(text: str) -> str:
    result = text
    for p in FILLER:
        result = re.sub(p, "", result, count=1)
        if result != text:
            break  # Only apply the first match
    result = result.strip()
    if result and result[0].islower():
        result = result[0].upper() + result[1:]
    return result

def main():
    try:
        event = json.loads(sys.stdin.read())
        prompt = event.get("prompt", "")

        # Don't touch: empty, short, slash commands, simple yes/no
        if not prompt or len(prompt.split()) < 10 or prompt.startswith("/"):
            print("{}")
            return
        if re.match(r"^\s*(sim|n[aã]o|ok|yes|no|s|n|y|si|continue|continua)\s*$", prompt, re.I):
            print("{}")
            return

        cleaned = strip_filler(prompt)

        # Only output if we actually removed filler, not just capitalization
        if not cleaned or cleaned.lower() == prompt.strip().lower():
            print("{}")
            return

        json.dump({"hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "updatedPrompt": cleaned,
        }}, sys.stdout, ensure_ascii=False)
    except Exception:
        print("{}")

if __name__ == "__main__":
    main()

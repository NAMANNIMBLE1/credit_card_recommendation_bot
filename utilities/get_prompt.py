import os
from pathlib import Path

def get_prompt_template() -> str:
    """
    Reads the prompt.txt file from the prompt directory and returns its content as a string.
    Returns:
        str: The prompt template
    """
    prompt_path = Path(__file__).resolve().parent.parent / "prompt" / "prompt.txt"
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read().strip()
    

# print(get_prompt_template()) # for checking purpose
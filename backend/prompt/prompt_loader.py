# backend/prompt/prompt_loader.py

import os
from backend.config import SOURCE_FOLDER

def load_prompt():
    prompt_path = os.path.join(SOURCE_FOLDER, 'Prompt.txt')

    if not os.path.isfile(prompt_path):
        print("[PromptLoader] Prompt.txt not found.")
        return ""

    with open(prompt_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    if not content:
        print("[PromptLoader] Prompt.txt is empty.")
    return content

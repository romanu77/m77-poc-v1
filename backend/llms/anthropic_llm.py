# backend/llms/anthropic_llm.py

import anthropic
from backend.config import API_KEYS, MODEL_SETTINGS

def call_anthropic(prompt):
    client = anthropic.Anthropic(api_key=API_KEYS["anthropic"])
    model = MODEL_SETTINGS["anthropic"]["model"]

    try:
        response = client.messages.create(
            model=model,
            max_tokens=1024,
            temperature=0.3,
            system="You are a helpful assistant.",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()
    except Exception as e:
        print(f"[Anthropic] Error: {e}")
        return "Error while contacting Anthropic."

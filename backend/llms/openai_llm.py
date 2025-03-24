# backend/llms/openai_llm.py

from openai import OpenAI
from backend.config import API_KEYS, MODEL_SETTINGS

def call_openai(prompt):
    client = OpenAI(api_key=API_KEYS["openai"])
    model = MODEL_SETTINGS["openai"]["model"]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[OpenAI] Error: {e}")
        return "Error while contacting OpenAI."

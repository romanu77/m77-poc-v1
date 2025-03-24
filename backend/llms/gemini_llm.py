# backend/llms/gemini_llm.py

import google.generativeai as genai
from backend.config import API_KEYS, MODEL_SETTINGS

def call_gemini(prompt):
    api_key = API_KEYS["gemini"]
    model_name = MODEL_SETTINGS["gemini"]["model"]

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini] Error: {e}")
        return "Error while contacting Gemini."

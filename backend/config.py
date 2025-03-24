# backend/config.py

import os
from dotenv import load_dotenv
load_dotenv()

# Choose between: "openai", "anthropic", "gemini"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")

# API Keys (replace with your real keys or load from environment)
API_KEYS = {
    "openai": os.getenv("OPENAI_API_KEY", "your-openai-key"),
    "anthropic": os.getenv("ANTHROPIC_API_KEY", "your-anthropic-key"),
    "gemini": os.getenv("GEMINI_API_KEY", "your-gemini-key")
}

# Model settings (can be expanded for each provider)
MODEL_SETTINGS = {
    "openai": {
        "model": "gpt-3.5-turbo"
    },
    "anthropic": {
        "model": "claude-3-opus-20240229"
    },
    "gemini": {
        "model": "gemini-pro"
    }
}

# Source folder path
SOURCE_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'sources')

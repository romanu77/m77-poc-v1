# backend/chat.py

from backend.prompt.prompt_loader import load_prompt
from backend.llms.openai_llm import call_openai
from backend.llms.anthropic_llm import call_anthropic
from backend.llms.gemini_llm import call_gemini
from backend.config import LLM_PROVIDER

def generate_answer(user_question, vectorstore):
    if vectorstore is None:
        return "I have no knowledge base to answer from."

    print("[Chat] Searching vector store for relevant context...")
    docs = vectorstore.similarity_search(user_question, k=5)

    context = "\n\n".join(doc.page_content for doc in docs)
    prompt = load_prompt()

    full_input = f"{prompt}\n\nContext:\n{context}\n\nQuestion: {user_question}"

    if LLM_PROVIDER == "openai":
        return call_openai(full_input)
    elif LLM_PROVIDER == "anthropic":
        return call_anthropic(full_input)
    elif LLM_PROVIDER == "gemini":
        return call_gemini(full_input)
    else:
        return f"LLM provider '{LLM_PROVIDER}' is not supported."

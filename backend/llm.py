import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

from backend.config import API_KEYS

def ask_llm(message, context_docs, prompt_template):
    context_text = "\n\n".join([doc.page_content for doc in context_docs])
    
    prompt = prompt_template.replace("{{context}}", context_text).replace("{{question}}", message)

    llm = ChatOpenAI(
        openai_api_key=API_KEYS["openai"],
        temperature=0.3,
        model_name="gpt-3.5-turbo"
    )

    response = llm([SystemMessage(content=prompt_template), HumanMessage(content=prompt)])
    return response.content

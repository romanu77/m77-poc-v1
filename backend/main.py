# backend/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from backend.loader.files import load_all_files
from backend.loader.links import load_all_links
from backend.vector_store import build_vectorstore_from_text
from backend.chat import generate_answer
from backend.logger.chat_logger import log_message  # 🔁 Import logger

app = FastAPI()

# Enable CORS for frontend use (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load all data and build vectorstore
print("[App] Loading files and links...")
file_text = load_all_files()
link_text = load_all_links()
combined_text = file_text + "\n" + link_text

print("[App] Building vectorstore...")
VECTORSTORE = build_vectorstore_from_text(combined_text)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    question = data.get("message", "").strip()

    if not question:
        return {"answer": "Please provide a question."}

    log_message("User", question)  # 🔁 Log user message
    answer = generate_answer(question, VECTORSTORE)
    log_message("Bot", answer)     # 🔁 Log bot response

    return {"answer": answer}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)

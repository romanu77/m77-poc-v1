# backend/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn
import os

from backend.loader.files import load_all_files
from backend.loader.links import load_all_links
from backend.vector_store import build_vectorstore_from_text
from backend.chat import generate_answer
from backend.logger.chat_logger import log_message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load vectorstore
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

    log_message("User", question)
    answer = generate_answer(question, VECTORSTORE)
    log_message("Bot", answer)

    return {"answer": answer}

# 👇 Adaugă ruta pentru index.html
@app.get("/")
async def serve_index():
    return FileResponse(os.path.join("frontend", "index.html"))

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from backend.vector_store import build_vectorstore_from_text, get_relevant_documents
from backend.llm import ask_llm
from backend.file_loader import load_files_and_links
from backend.prompt_loader import load_prompt

app = FastAPI()

# 🔥 Absolute path to the frontend directory
frontend_path = os.path.abspath("frontend")

# ✅ Enable CORS (required for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Serve static files (JS, CSS, images, etc.)
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# 🔄 Load documents and vector store on startup
print("[App] Loading files and links...")
combined_text = load_files_and_links()

print("[App] Building vectorstore...")
VECTORSTORE = build_vectorstore_from_text(combined_text)

print("[App] Loading prompt...")
PROMPT_TEMPLATE = load_prompt()

# 🧠 Chat endpoint
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")

    print("[Chat] Searching vector store for relevant context...")
    context_docs = get_relevant_documents(VECTORSTORE, message)

    print("[Chat] Calling LLM...")
    response = ask_llm(message, context_docs, PROMPT_TEMPLATE)
    return {"answer": response}

# 🏠 Serve index.html for root route
@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))

# 🔁 Fallback route for SPA support
@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    return FileResponse(os.path.join(frontend_path, "index.html"))

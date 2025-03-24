from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

from backend.vector_store import build_vectorstore_from_text, get_relevant_documents
from backend.llm import ask_llm
from backend.loader.files import load_all_files, load_all_links
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
file_text = load_all_files()
link_text = load_all_links()
combined_text = file_text + "\n" + link_text

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
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_path = os.path.join(frontend_path, "index.html")
    print(f"Serving: {index_path}")
    return FileResponse(index_path, media_type="text/html")

# 🔁 Fallback route for SPA support
@app.get("/{full_path:path}", response_class=HTMLResponse)
async def catch_all(full_path: str):
    index_path = os.path.join(frontend_path, "index.html")
    print(f"Catch-all: serving {index_path}")
    return FileResponse(index_path, media_type="text/html")

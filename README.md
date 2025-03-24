# Modular AI Chatbot (Multi-LLM, File & Link-Based)

This is a modular, production-ready AI chatbot that supports multiple language models (LLMs), including OpenAI, Anthropic, and Gemini. It is trained on custom data sources such as PDFs, TXT files, and website links. The project is designed to be easily adapted for various use cases.

---

## 🌐 Features

- Multi-LLM support: OpenAI (default), Anthropic, Gemini *(easily switchable)*
- Custom training via:
  - `prompt.txt` – initial instructions for the bot
  - `.txt` and `.pdf` files – added to the `/sources` folder
  - `links.txt` – URLs from which content is fetched
- Chunked text + embeddings with FAISS vector store
- API endpoint `/chat` for questions
- Clean frontend (`index.html`) with dark/light toggle

---

## 📁 Folder Structure

```
chatbot/
├── backend/
│   ├── main.py                # FastAPI server + vector build
│   ├── config.py              # LLM provider and API keys
│   ├── chat.py                # Chat logic with context injection
│   ├── vector_store.py        # FAISS embedding creation
│   ├── loader/
│   │   ├── files.py           # Load text/pdf files
│   │   └── links.py           # Load URLs
│   ├── prompt/
│   │   └── prompt_loader.py   # Load Prompt.txt
│   └── llms/
│       └── openai_llm.py      # OpenAI integration
├── frontend/
│   ├── index.html             # User interface
│   └── style.css              # UI design (dark/light mode)
├── sources/
│   ├── prompt.txt             # System prompt (optional)
│   ├── links.txt              # List of URLs (one per line)
│   └── *.txt / *.pdf          # Training files
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your API key (OpenAI by default)

```bash
export OPENAI_API_KEY="sk-your-key-here"
```

You can also set the provider in `config.py`:

```python
LLM_PROVIDER = "openai"  # or "anthropic", "gemini"
```

### 3. Run the backend

```bash
uvicorn backend.main:app --reload
```

### 4. Open the frontend

Simply open `frontend/index.html` in your browser.

---

## 🧠 How to Train the Bot

- Add your instructions to `sources/prompt.txt`
- Place `.txt` and `.pdf` files in the `sources/` folder
- Add links (one per line) to `sources/links.txt`
- Restart the backend to rebuild the knowledge base

---

## 🛠 To Do (Future Features)

- Add Anthropic and Gemini support in `/llms`
- Add Google Sheets & Calendar integration (for booking systems)
- Add file upload via frontend

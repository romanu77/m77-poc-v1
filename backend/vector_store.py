from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from backend.config import API_KEYS

def build_vectorstore_from_text(raw_text):
    if not raw_text.strip():
        print("[VectorStore] No content to index.")
        return None

    print("[VectorStore] Splitting text into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    documents = splitter.create_documents([raw_text])

    print("[VectorStore] Generating embeddings...")
    embeddings = OpenAIEmbeddings(openai_api_key=API_KEYS["openai"])

    print("[VectorStore] Creating FAISS vector store...")
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore

def get_relevant_documents(vectorstore, query: str, k: int = 4):
    return vectorstore.similarity_search(query, k=k)

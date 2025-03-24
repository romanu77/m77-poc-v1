# backend/loader/files.py

import os
from backend.config import SOURCE_FOLDER
from PyPDF2 import PdfReader

def read_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"[FileLoader] Failed to read TXT {file_path}: {e}")
        return ""

def read_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        print(f"[FileLoader] Failed to read PDF {file_path}: {e}")
    return text

def load_all_files():
    supported_exts = {
        '.txt': read_txt,
        '.pdf': read_pdf,
    }

    full_text = ""
    for filename in os.listdir(SOURCE_FOLDER):
        ext = os.path.splitext(filename)[1].lower()
        if ext in supported_exts:
            file_path = os.path.join(SOURCE_FOLDER, filename)
            print(f"[FileLoader] Reading {filename}...")
            full_text += supported_exts[ext](file_path) + "\n"

    return full_text.strip()

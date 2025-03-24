# backend/loader/links.py

import os
import requests
from bs4 import BeautifulSoup
from backend.config import SOURCE_FOLDER

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove script, style, and noscript elements
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        # Extract visible text
        text = soup.get_text(separator=" ", strip=True)
        return text
    except Exception as e:
        print(f"[LinkLoader] Failed to fetch {url}: {e}")
        return ""

def load_all_links():
    link_file = os.path.join(SOURCE_FOLDER, "links.txt")
    if not os.path.isfile(link_file):
        print("[LinkLoader] links.txt not found.")
        return ""

    with open(link_file, "r", encoding="utf-8") as f:
        links = [line.strip() for line in f if line.strip()]

    all_text = ""
    for link in links:
        print(f"[LinkLoader] Fetching {link}...")
        all_text += extract_text_from_url(link) + "\n"

    return all_text.strip()

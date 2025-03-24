# backend/logger/chat_logger.py

import os
from datetime import datetime

LOGS_FOLDER = "logs"
os.makedirs(LOGS_FOLDER, exist_ok=True)

# Create log file with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"chat_{timestamp}.txt"
log_path = os.path.join(LOGS_FOLDER, log_filename)

def log_message(sender: str, message: str):
    time_str = datetime.now().strftime("[%H:%M:%S]")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{time_str} {sender}: {message.strip()}\n")

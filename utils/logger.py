# utils/logger.py

import os
from datetime import datetime
from utils.config import LOG_PATH

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

def log_event(message: str):
    """
    Olayları zaman damgası ile loglar.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] {message}\n"
    with open(f"{LOG_PATH}venom.log", "a") as f:
        f.write(line)

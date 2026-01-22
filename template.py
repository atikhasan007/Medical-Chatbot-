import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # ✅ Create directory if not exists
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    # ✅ Create empty file if not exists
    if not os.path.exists(filepath) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")

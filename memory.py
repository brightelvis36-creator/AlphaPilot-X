import json
import os
from datetime import datetime

MEMORY_FILE = "alphapilot_memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}


def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def remember(key, value):
    data = load_memory()

    data[key] = {
        "value": value,
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_memory(data)


def recall(key):
    data = load_memory()

    if key in data:
        return data[key]["value"]

    return None


def forget(key):
    data = load_memory()

    if key in data:
        del data[key]
        save_memory(data)
        return True

    return False


def get_all_memory():
    return load_memory()

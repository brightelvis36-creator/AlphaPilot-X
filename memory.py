import json
import os

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
    data[key] = value
    save_memory(data)

def get_all_memory():
    return load_memory()

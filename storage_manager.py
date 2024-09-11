import json
import os

DATA_FILE = "orders.json"

def save_orders(orders):
    """Speichert die Aufträge in einer JSON-Datei."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=4)

def load_orders():
    """Lädt die Aufträge aus einer JSON-Datei."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

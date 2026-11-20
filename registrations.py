import json
import os 

FILE = "products.json"

def save_data(products):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

lista = load_data()
lista.append({"id": len(lista) + 1, "nome": "Ana", "telefone": "9999-0000"})
save_data(lista)
print(lista)
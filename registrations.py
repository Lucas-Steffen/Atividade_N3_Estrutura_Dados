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

def read_text(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Campo obrigatório")

def read_intNumber(message):
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("Não pode ser negativo.")
            else:
                return value
        except ValueError:
            print("Digite um número válido")

def read_float(message):
    while True:
        try:
            value = float(input(message).replace(",", "."))
            if value < 0:
                print("Não pode ser negativo.")
            else:
                return value
        except ValueError:
            print("Digite um número válido")

def include(products):
    new_id = max((p["id"] for p in products), default=0) + 1
    product = {
        "id": new_id,
        "name": read_text("Nome: "),
        "category": read_text("Categoria: "),
        "price": read_float("Preco: "),
        "quantity": read_intNumber("Quantidade: ")
    }
    products.append(product)
    save_data(products)
    print("Produto incluído com sucesso!")

products = load_data()
include(products)
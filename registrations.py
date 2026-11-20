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

def findById(products, product_id):
    for p in products:
        if p["id"] == product_id:
            return p 
    return None

def include(products):
    new_id = max((p["id"] for p in products), default=0) + 1
    product = {
        "id": new_id,
        "name": read_text("Nome: "),
        "category": read_text("Categoria: "),
        "price": read_float("Preço: "),
        "quantity": read_intNumber("Quantidade: ")
    }
    
    products.append(product)
    save_data(products)
    print("Produto incluído com sucesso!")

def change(products):
    product_id = read_intNumber("Id: ")
    product = findById(products, product_id)
    if product is None:
        print("Não foi possível localizar esse produto.")
        return
    
    product["name"] = read_text("Novo Nome: ")
    product["category"] = read_text("Nova Categoria: ")
    product["price"] = read_float("Novo Preço: ")
    product["quantity"] = read_intNumber("Nova Quantidade: ")

    save_data(products)
    print("Produto alterado com sucesso!")

def delete(products):
    product_id = read_intNumber("Id: ")
    product = findById(products, product_id)
    if product is None:
        print("Não foi possível localizar esse produto.")
        return

    confirm = read_text("Tem certeza que seja excluir esse produto (s/n)? ").lower()
    if confirm != 's':
        print("Exclusão cancelada")
        return
    
    products.remove(product)
    save_data(products)
    print("Produto excluído com sucesso!")
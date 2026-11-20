import json
import os 

FILE = "products.json"

def menu():
    products = load_data()          
    while True:
        print("\n=== MENU ===")
        print("0 - Ver todos")
        print("1 - Incluir")
        print("2 - Atualizar")
        print("3 - Excluir")
        print("9 - Sair")
        option = input("Opção: ").strip()

        if option == "0":
            view_menu(products)
        elif option == "1":
            include(products)
        elif option == "2":
            change(products)
        elif option == "3":
            delete(products)
        elif option == "9":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

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

    show_products([product])
    print("\nQual campo deseja atualizar?")
    print("1 - Nome")
    print("2 - Categoria")
    print("3 - Preço")
    print("4 - Quantidade")
    print("5 - Todos")
    print("0 - Cancelar")
    option = input("Opção: ").strip()

    if option == "1":
        product["name"] = read_text("Novo Nome: ")
    elif option == "2":
        product["category"] = read_text("Nova Categoria: ")
    elif option == "3":
        product["price"] = read_float("Novo Preço: ")
    elif option == "4":
        product["quantity"] = read_intNumber("Nova Quantidade: ")
    elif option == "5":
        product["name"] = read_text("Novo Nome: ")
        product["category"] = read_text("Nova Categoria: ")
        product["price"] = read_float("Novo Preço: ")
        product["quantity"] = read_intNumber("Nova Quantidade: ")
    elif option == "0":
        print("Atualização cancelada.")
        return
    else:
        print("Opção inválida.")
        return

    save_data(products)
    print("Produto alterado com sucesso!")

def delete(products):
    product_id = read_intNumber("Id: ")
    product = findById(products, product_id)
    if product is None:
        print("Não foi possível localizar esse produto.")
        return

    confirm = read_text("Tem certeza que deseja excluir esse produto (s/n)? ").lower()
    if confirm != 's':
        print("Exclusão cancelada")
        return
    
    products.remove(product)
    save_data(products)
    print("Produto excluído com sucesso!")

def show_products(products):
    if not products:
        print("Nenhum produto encontrado.")
        return
    print(f"\n{'ID':<5}{'Nome':<25}{'Categoria':<18}{'Preço':>10}{'Qtd':>6}")
    print("-" * 64)
    for p in products:
        print(f"{p['id']:<5}{p['name']:<25}{p['category']:<18}{p['price']:>10.2f}{p['quantity']:>6}")

def search_by_id(products):
    product_id = read_intNumber("Id: ")
    product = findById(products, product_id)
    if product is None:
        print("Produto não encontrado.")
    else:
        show_products([product])

def search_by_name(products):
    term = read_text("Nome: ").lower()
    found = []
    for p in products:
        if term in p["name"].lower():
            found.append(p)
    show_products(found)

def search_by_category(products):
    term = read_text("Categoria: ").lower()
    found = []
    for p in products:
        if term in p["category"].lower():
            found.append(p)
    show_products(found)

def sort_by_name(products):
    # .lower() para "banana" não ficar depois de "Caju"
    show_products(sorted(products, key=lambda p: p["name"].lower()))

def sort_by_price(products):
    show_products(sorted(products, key=lambda p: p["price"]))

def view_menu(products):
    show_products(products)
    while True:
        print("\n1 - Buscar por id")
        print("2 - Buscar por nome")
        print("3 - Buscar por categoria")
        print("4 - Ordenar por nome (A-Z)")
        print("5 - Ordenar por preço (menor para maior)")
        print("0 - Voltar")
        option = input("Opção: ").strip()

        if option == "1":
            search_by_id(products)
        elif option == "2":
            search_by_name(products)
        elif option == "3":
            search_by_category(products)
        elif option == "4":
            sort_by_name(products)
        elif option == "5":
            sort_by_price(products)
        elif option == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nPrograma encerrado.")
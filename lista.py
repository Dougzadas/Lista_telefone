agenda = []

def menu():
    print("\nAGENDA")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Buscar")
    print("4. Atualizar")
    print("5. Remover")
    print("6. Favoritar")
    print("7. Listar favoritos")
    print("8. Sair")
    return input("Escolha: ")

def adicionar():
    agenda.append({"nome": input("Nome: "), "tel": input("Telefone: "), "fav": input("Favorito? (s/n): ") == 's'})


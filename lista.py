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

def listar():
    for c in sorted(agenda, key=lambda x: x['nome']):
        print(f"{c['nome']} - {c['tel']} {'★' if c['fav'] else ''}")

def buscar():
    nome = input("Nome: ")
    print(next((f"{c['nome']} - {c['tel']} {'★' if c['fav'] else ''}" for c in agenda if c['nome'] == nome), "Não encontrado"))

def atualizar():
    nome = input("Nome: ")
    for c in agenda:
        if c['nome'] == nome:
            c['nome'] = input("Novo nome: ") or c['nome']
            c['tel'] = input("Novo telefone: ") or c['tel']
            return

def remover():
    global agenda
    agenda = [c for c in agenda if c['nome'] != input("Nome: ")]

def favoritar():
    for c in agenda:
        if c['nome'] == input("Nome: "):
            c['fav'] = not c['fav']
            return

def listar_favoritos():
    for c in sorted([c for c in agenda if c['fav']], key=lambda x: x['nome']):
        print(f"{c['nome']} - {c['tel']} ★")

def main():
    while (op := menu()) != '8':
        {"1": adicionar, "2": listar, "3": buscar, "4": atualizar, "5": remover, "6": favoritar, "7": listar_favoritos}.get(op, lambda: print("Inválido"))()

if __name__ == "__main__":
    main()

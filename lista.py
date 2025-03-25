import json

agenda = []

try:
    with open("agenda.json", "r") as f:
        agenda = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    agenda = []

def salvar_agenda():
    with open("agenda.json", "w") as f:
        json.dump(agenda, f)

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
    try:
        nome = input("Nome: ").strip()
        tel = input("Telefone: ").strip()
        fav = input("Favorito? (s/n): ").strip().lower() == 's'
        if not nome or not tel:
            raise ValueError("Nome e telefone são obrigatórios.")
        agenda.append({"nome": nome, "tel": tel, "fav": fav})
        salvar_agenda()
    except ValueError as e:
        print(f"Erro: {e}")

def listar():
    for c in sorted(agenda, key=lambda x: x['nome']):
        print(f"{c['nome']} - {c['tel']} {'★' if c['fav'] else ''}")

def buscar():
    nome = input("Nome: ").strip()
    print(next((f"{c['nome']} - {c['tel']} {'★' if c['fav'] else ''}" for c in agenda if c['nome'].lower() == nome.lower()), "Não encontrado"))

def atualizar():
    nome = input("Nome: ").strip()
    for c in agenda:
        if c['nome'].lower() == nome.lower():
            c['nome'] = input("Novo nome: ").strip() or c['nome']
            c['tel'] = input("Novo telefone: ").strip() or c['tel']
            salvar_agenda()
            return
    print("Contato não encontrado.")

def remover():
    global agenda
    nome = input("Nome: ").strip()
    agenda = [c for c in agenda if c['nome'].lower() != nome.lower()]
    salvar_agenda()

def favoritar():
    nome = input("Nome: ").strip()
    for c in agenda:
        if c['nome'].lower() == nome.lower():
            c['fav'] = not c['fav']
            salvar_agenda()
            return
    print("Contato não encontrado.")

def listar_favoritos():
    for c in sorted([c for c in agenda if c['fav']], key=lambda x: x['nome']):
        print(f"{c['nome']} - {c['tel']} ★")

def main():
    while (op := menu()) != '8':
        {"1": adicionar, "2": listar, "3": buscar, "4": atualizar, "5": remover, "6": favoritar, "7": listar_favoritos}.get(op, lambda: print("Inválido"))()
    print("Saindo...")

if __name__ == "__main__":
    main()

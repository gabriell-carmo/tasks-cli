tarefas = []

def adicionar(tarefa):
    tarefas.append({"tarefa": tarefa, "feita": False})
    print(f'✅ Tarefa "{tarefa}" adicionada!')

def listar():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n📋 Suas tarefas:")
    for i, t in enumerate(tarefas):
        status = "✅" if t["feita"] else "⬜"
        print(f"{i}. {status} {t['tarefa']}")
    print()

def concluir(indice):
    if indice < 0 or indice >= len(tarefas):
        print("Índice inválido!")
        return
    tarefas[indice]["feita"] = True
    print(f'🎉 Tarefa "{tarefas[indice]["tarefa"]}" concluída!')

def remover(indice):
    if indice < 0 or indice >= len(tarefas):
        print("Índice inválido!")
        return
    removida = tarefas.pop(indice)
    print(f'🗑️ Tarefa "{removida["tarefa"]}" removida!')

# Menu principal
while True:
    print("=== LISTA DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome da tarefa: ")
        adicionar(nome)
    elif opcao == "2":
        listar()
    elif opcao == "3":
        listar()
        idx = int(input("Número da tarefa a concluir: "))
        concluir(idx)
    elif opcao == "4":
        listar()
        idx = int(input("Número da tarefa a remover: "))
        remover(idx)
    elif opcao == "5":
        print("Até logo! 👋")
        break
    else:
        print("Opção inválida, tente novamente.")
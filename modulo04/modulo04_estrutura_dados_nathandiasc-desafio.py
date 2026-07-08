agenda = {}
while True:
    print("\n1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Exibir agenda")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
        print("Contato adicionado!")
    elif opcao == "2":
        nome = input("Nome do contato: ")
        if nome in agenda:
            del agenda[nome]
            print("Contato removido!")
        else:
            print("Contato não encontrado.")
    elif opcao == "3":
        nome = input("Nome do contato: ")
        if nome in agenda:
            print("Telefone:", agenda[nome])
        else:
            print("Contato não encontrado.")
    elif opcao == "4":
        print("\nAgenda de contatos:")
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
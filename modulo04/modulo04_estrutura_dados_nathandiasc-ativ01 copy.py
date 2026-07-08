lista_compras = []
while True:
    print("\n1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        item = input("Digite o item: ")
        lista_compras.append(item)
        print("Item adicionado!")
    elif opcao == "2":
        item = input("Digite o item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print("Item removido!")
        else:
            print("Item não encontrado.")
    elif opcao == "3":
        print("Lista de compras:")
        for item in lista_compras:
            print("-", item)
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
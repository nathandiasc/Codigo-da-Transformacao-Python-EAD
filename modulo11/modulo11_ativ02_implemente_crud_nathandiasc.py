import sqlite3

conexao = sqlite3.connect("clientes.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

conexao.commit()



def inserir_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o e-mail do cliente: ")

    cursor.execute("""
        INSERT INTO Clientes (nome, email)
        VALUES (?, ?)
    """, (nome, email))

    conexao.commit()

    print("Cliente inserido com sucesso!")



def consultar_clientes():
    cursor.execute("SELECT * FROM Clientes")

    clientes = cursor.fetchall()

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        print("\n===== CLIENTES =====")

        for cliente in clientes:
            print(f"ID: {cliente[0]}")
            print(f"Nome: {cliente[1]}")
            print(f"E-mail: {cliente[2]}")
            print("--------------------")



def atualizar_cliente():
    id_cliente = int(input("Digite o ID do cliente que deseja atualizar: "))

    novo_nome = input("Digite o novo nome: ")
    novo_email = input("Digite o novo e-mail: ")

    cursor.execute("""
        UPDATE Clientes
        SET nome = ?, email = ?
        WHERE id = ?
    """, (novo_nome, novo_email, id_cliente))

    conexao.commit()

    if cursor.rowcount > 0:
        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")



def deletar_cliente():
    id_cliente = int(input("Digite o ID do cliente que deseja deletar: "))

    cursor.execute("""
        DELETE FROM Clientes
        WHERE id = ?
    """, (id_cliente,))

    conexao.commit()

    if cursor.rowcount > 0:
        print("Cliente deletado com sucesso!")
    else:
        print("Cliente não encontrado.")



while True:

    print("\n===== SISTEMA DE CLIENTES =====")
    print("1 - Inserir cliente")
    print("2 - Consultar clientes")
    print("3 - Atualizar cliente")
    print("4 - Deletar cliente")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        inserir_cliente()

    elif opcao == "2":
        consultar_clientes()

    elif opcao == "3":
        atualizar_cliente()

    elif opcao == "4":
        deletar_cliente()

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")


conexao.close()
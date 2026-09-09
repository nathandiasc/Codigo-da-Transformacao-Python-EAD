import sqlite3

conexao = sqlite3.connect("tarefas.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
)
""")

conexao.commit()



def adicionar_tarefa():

    descricao = input("Digite a tarefa: ")

    cursor.execute("""
        INSERT INTO tarefas (descricao)
        VALUES (?)
    """, (descricao,))

    conexao.commit()

    print("Tarefa adicionada com sucesso!")



def visualizar_tarefas():

    cursor.execute("SELECT * FROM tarefas")

    tarefas = cursor.fetchall()

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:

        print("\n===== LISTA DE TAREFAS =====")

        for tarefa in tarefas:
            print(f"{tarefa[0]} - {tarefa[1]}")



def excluir_tarefa():

    id_tarefa = int(input("Digite o ID da tarefa que deseja excluir: "))

    cursor.execute("""
        DELETE FROM tarefas
        WHERE id = ?
    """, (id_tarefa,))

    conexao.commit()

    if cursor.rowcount > 0:
        print("Tarefa excluída com sucesso!")
    else:
        print("Tarefa não encontrada.")



while True:

    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Excluir tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        visualizar_tarefas()

    elif opcao == "3":
        excluir_tarefa()

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")


conexao.close()
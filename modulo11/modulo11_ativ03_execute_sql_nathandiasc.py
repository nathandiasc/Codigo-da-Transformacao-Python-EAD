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



print("\n===== TODOS OS CLIENTES =====")

cursor.execute("SELECT * FROM Clientes")

clientes = cursor.fetchall()

if len(clientes) == 0:
    print("Nenhum cliente cadastrado.")
else:
    for cliente in clientes:
        print(cliente)



print("\n===== CLIENTES COM NOME COMEÇANDO COM A =====")

cursor.execute("""
SELECT * FROM Clientes
WHERE nome LIKE 'A%'
""")

clientes_a = cursor.fetchall()

if len(clientes_a) == 0:
    print("Nenhum cliente com nome começando com A.")
else:
    for cliente in clientes_a:
        print(cliente)



print("\n===== CLIENTES EM ORDEM ALFABÉTICA =====")

cursor.execute("""
SELECT * FROM Clientes
ORDER BY nome
""")

clientes_ordenados = cursor.fetchall()

for cliente in clientes_ordenados:
    print(cliente)



print("\n===== QUANTIDADE DE CLIENTES =====")

cursor.execute("""
SELECT COUNT(*) FROM Clientes
""")

quantidade = cursor.fetchone()

print("Quantidade de clientes:", quantidade[0])



print("\n===== BUSCAR CLIENTE =====")

nome_busca = input("Digite o nome que deseja procurar: ")

cursor.execute("""
SELECT * FROM Clientes
WHERE nome = ?
""", (nome_busca,))

resultado = cursor.fetchall()

if len(resultado) == 0:
    print("Cliente não encontrado.")
else:
    for cliente in resultado:
        print(cliente)


conexao.close()
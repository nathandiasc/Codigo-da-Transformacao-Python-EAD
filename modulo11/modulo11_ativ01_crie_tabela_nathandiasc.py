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

print("Banco de dados e tabela Clientes criados com sucesso!")

conexao.close()
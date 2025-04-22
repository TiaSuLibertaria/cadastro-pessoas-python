# cadastro_rapido.py

import sqlite3

# Passo 1: Conectar/criar banco de dados
conexao = sqlite3.connect("cadastro_pessoas.db")
cursor = conexao.cursor()

# Passo 2: Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Passo 3: Pedir dados ao usuário
print("Cadastro de Pessoas")
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")

# Passo 4: Inserir os dados no banco
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))
conexao.commit()

# Passo 5: Mostrar todos os registros salvos
print("\nLista de pessoas cadastradas:")
cursor.execute("SELECT * FROM pessoas")
pessoas = cursor.fetchall()

for pessoa in pessoas:
    print(f"ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade: {pessoa[2]}")

# Passo 6: Encerrar conexão
conexao.close()

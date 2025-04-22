# banco_usuarios.py

import sqlite3

# Passo 1: Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('cadastro.db')

# Passo 2: Criar um cursor (controlador de comandos SQL)
cursor = conexao.cursor()

# Passo 3: Criar a tabela 'usuarios'
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Passo 4: Inserir 3 registros
usuarios = [
    ("João da Silva", "joao@email.com"),
    ("Maria Oliveira", "maria@email.com"),
    ("Carlos Souza", "carlos@email.com")
]

cursor.executemany("INSERT INTO usuarios (nome, email) VALUES (?, ?)", usuarios)

# Passo 5: Salvar as mudanças
conexao.commit()

# Passo 6: Listar todos os registros
cursor.execute("SELECT * FROM usuarios")
dados = cursor.fetchall()

print("Usuários cadastrados:")
for usuario in dados:
    print(usuario)

# Passo 7: Fechar a conexão
conexao.close()

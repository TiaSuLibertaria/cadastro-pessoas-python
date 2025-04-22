# media_idades.py

# Passo 1: Abrir o arquivo no modo leitura
with open('dados.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Passo 2: Inicializar variáveis
soma = 0
quantidade = 0

# Passo 3: Processar cada linha
for linha in linhas:
    nome, idade = linha.strip().split(',')
    soma += int(idade)
    quantidade += 1

# Passo 4: Calcular a média
media = soma / quantidade

# Passo 5: Mostrar o resultado
print(f"A média de idade é: {media}")
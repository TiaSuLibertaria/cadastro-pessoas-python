# salvar_nome_tkinter.py

import tkinter as tk
from tkinter import messagebox

# Passo 1: Criar a janela principal
janela = tk.Tk()
janela.title("Salvar Nome")
janela.geometry("300x150")

# Passo 2: Criar rótulo e campo de entrada
rotulo = tk.Label(janela, text="Digite seu nome:")
rotulo.pack(pady=5)

entrada = tk.Entry(janela, width=30)
entrada.pack(pady=5)

# Passo 3: Criar função para salvar nome
def salvar_nome():
    nome = entrada.get()
    if nome.strip() == "":
        messagebox.showwarning("Aviso", "Por favor, digite um nome.")
        return
    
    with open("nomes.txt", "a") as arquivo:
        arquivo.write(nome + "\n")
    
    entrada.delete(0, tk.END)
    messagebox.showinfo("Sucesso", "Nome salvo com sucesso!")

# Passo 4: Criar botão e vincular à função
botao = tk.Button(janela, text="Salvar", command=salvar_nome)
botao.pack(pady=10)

# Passo 5: Rodar o loop principal da janela
janela.mainloop()

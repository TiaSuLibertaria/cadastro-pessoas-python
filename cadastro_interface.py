import sqlite3
import tkinter as tk
from tkinter import messagebox, Toplevel, ttk



# Banco de dados
conexao = sqlite3.connect("cadastro_pessoas.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")
conexao.commit()
conexao.close()

# Função para salvar
def salvar_pessoa():
    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if nome.strip() == "" or not idade.isdigit():
        messagebox.showwarning("Atenção", "Preencha os campos corretamente.")
        return

    conexao = sqlite3.connect("cadastro_pessoas.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, int(idade)))
    conexao.commit()
    conexao.close()

    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)
    messagebox.showinfo("Sucesso", "Pessoa cadastrada com sucesso!")

# Função para excluir
def excluir_pessoa(tree):
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione uma pessoa para excluir.")
        return

    pessoa_id = tree.item(item_selecionado)["values"][0]

    conexao = sqlite3.connect("cadastro_pessoas.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM pessoas WHERE id = ?", (pessoa_id,))
    conexao.commit()
    conexao.close()

    tree.delete(item_selecionado)
    messagebox.showinfo("Sucesso", "Pessoa excluída com sucesso.")

# ✅ Função para editar (agora FORA da função mostrar_lista)
def editar_pessoa(tree):
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione uma pessoa para editar.")
        return

    pessoa = tree.item(item_selecionado)["values"]
    pessoa_id, nome_antigo, idade_antiga = pessoa

    janela_editar = Toplevel(janela)
    janela_editar.title("Editar Pessoa")

    tk.Label(janela_editar, text="Novo nome:").pack(pady=5)
    entrada_nome_novo = tk.Entry(janela_editar, width=30)
    entrada_nome_novo.insert(0, nome_antigo)
    entrada_nome_novo.pack()

    tk.Label(janela_editar, text="Nova idade:").pack(pady=5)
    entrada_idade_nova = tk.Entry(janela_editar, width=30)
    entrada_idade_nova.insert(0, str(idade_antiga))
    entrada_idade_nova.pack()

    def salvar_edicao():
        novo_nome = entrada_nome_novo.get()
        nova_idade = entrada_idade_nova.get()

        if novo_nome.strip() == "" or not nova_idade.isdigit():
            messagebox.showwarning("Erro", "Preencha os dados corretamente.")
            return

        conexao = sqlite3.connect("cadastro_pessoas.db")
        cursor = conexao.cursor()
        cursor.execute("UPDATE pessoas SET nome = ?, idade = ? WHERE id = ?", (novo_nome, int(nova_idade), pessoa_id))
        conexao.commit()
        conexao.close()

        messagebox.showinfo("Sucesso", "Pessoa atualizada com sucesso.")
        janela_editar.destroy()
        janela_lista.destroy()
        mostrar_lista()

    tk.Button(janela_editar, text="Salvar Alterações", command=salvar_edicao).pack(pady=10)

# Função para mostrar a lista
def mostrar_lista():
    global janela_lista
    conexao = sqlite3.connect("cadastro_pessoas.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    conexao.close()

    janela_lista = Toplevel(janela)
    janela_lista.title("Pessoas Cadastradas")

    tree = ttk.Treeview(janela_lista, columns=("ID", "Nome", "Idade"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Idade", text="Idade")

    for pessoa in pessoas:
        tree.insert("", tk.END, values=pessoa)

    tree.pack(padx=10, pady=10)

    btn_excluir = tk.Button(janela_lista, text="Excluir Pessoa Selecionada", command=lambda: excluir_pessoa(tree))
    btn_excluir.pack(pady=5)

    btn_editar = tk.Button(janela_lista, text="Editar Pessoa Selecionada", command=lambda: editar_pessoa(tree))
    btn_editar.pack(pady=5)

# Interface principal
janela = tk.Tk()
style = ttk.Style(janela)
style.theme_use("clam")  # temas disponíveis: clam, alt, default, classic

# Personalizando Treeview
style.configure("Treeview",
                background="#f0f0f0",
                foreground="black",
                rowheight=25,
                fieldbackground="#f0f0f0")

style.map("Treeview", background=[("selected", "#cce5ff")])

# Botões
style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white", font=("Arial", 10, "bold"))

janela.title("Cadastro de Pessoas")
janela.geometry("300x200")

tk.Label(janela, text="Nome:").pack(pady=5)
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack()

tk.Label(janela, text="Idade:").pack(pady=5)
entrada_idade = tk.Entry(janela, width=30)
entrada_idade.pack()

ttk.Button(janela, text="Salvar", command=salvar_pessoa).pack(pady=10)

ttk.Button(janela, text="Mostrar Cadastros", command=mostrar_lista).pack()

janela.mainloop()

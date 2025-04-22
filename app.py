from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('cadastro_pessoas.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    pessoas = conn.execute('SELECT * FROM pessoas').fetchall()
    conn.close()
    return render_template('index.html', pessoas=pessoas)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    idade = request.form['idade']
    if nome and idade.isdigit():
        conn = get_db_connection()
        conn.execute('INSERT INTO pessoas (nome, idade) VALUES (?, ?)', (nome, int(idade)))
        conn.commit()
        conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM pessoas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

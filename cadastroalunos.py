import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('alunos.db')
cursor = conn.cursor()

# Criação da tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        matricula TEXT PRIMARY KEY,
        nome TEXT,
        data_nascimento TEXT,
        email TEXT,
        endereco TEXT,
        contato_aluno TEXT,
        nome_responsavel TEXT,
        contato_responsavel TEXT,
        grau_escolaridade TEXT,
        identidade TEXT
    )
''')
conn.commit()

# Função para gerar matrícula
def gerar_matricula():
    cursor.execute('SELECT COUNT(*) FROM alunos')
    contador_aluno = cursor.fetchone()[0] + 1
    agora = datetime.datetime.now()
    ano = agora.year
    mes = agora.month
    numero_sequencial = f'{contador_aluno:04d}'
    matricula = f'{ano}{mes:02d}{numero_sequencial}'
    return matricula

# Função para calcular idade
def calcular_idade(data_nascimento):
    hoje = datetime.datetime.now()
    idade_anos = hoje.year - data_nascimento.year
    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade_anos -= 1
    return idade_anos

# Função para validar data de nascimento
def validar_data_nascimento(data_str):
    try:
        if len(data_str) != 8 or not data_str.isdigit():
            raise ValueError("Formato inválido")
        dia = int(data_str[:2])
        mes = int(data_str[2:4])
        ano = int(data_str[4:])
        data_nascimento = datetime.datetime(ano, mes, dia)
        idade_anos = calcular_idade(data_nascimento)
        if idade_anos < 4:
            raise ValueError("Aluno deve ter pelo menos 4 anos de idade")
        return data_nascimento
    except ValueError as e:
        messagebox.showerror("Erro", f"{e}. Tente novamente.")
        return None

# Função para cadastrar aluno no banco de dados
def cadastrar_aluno():
    def cadastrar():
        nome = entry_nome.get().strip().title()
        data_nascimento_str = entry_data_nascimento.get().strip()
        data_nascimento = validar_data_nascimento(data_nascimento_str)
        email = entry_email.get().strip()
        rua = entry_rua.get().strip().title()
        bairro = entry_bairro.get().strip().title()
        numero = entry_numero.get().strip()
        contato_aluno = entry_contato_aluno.get().strip()
        nome_responsavel = entry_nome_responsavel.get().strip().title()
        contato_responsavel = entry_contato_responsavel.get().strip()
        identidade = entry_identidade.get().strip()
        grau_escolaridade = entry_grau_escolaridade.get().strip().title()

        if (nome and data_nascimento and email and rua and bairro and numero and contato_aluno
            and nome_responsavel and contato_responsavel and identidade and grau_escolaridade):
            
            matricula = gerar_matricula()
            cursor.execute('''
                INSERT INTO alunos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (matricula, nome, data_nascimento.strftime("%d/%m/%Y"), email, 
                  f'Rua: {rua}, Bairro: {bairro}, Número: {numero}', contato_aluno, 
                  nome_responsavel, contato_responsavel, grau_escolaridade, identidade))
            conn.commit()
            messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")
            limpar_campos()
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos corretamente.")

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_data_nascimento.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_rua.delete(0, tk.END)
        entry_bairro.delete(0, tk.END)
        entry_numero.delete(0, tk.END)
        entry_contato_aluno.delete(0, tk.END)
        entry_nome_responsavel.delete(0, tk.END)
        entry_contato_responsavel.delete(0, tk.END)
        entry_identidade.delete(0, tk.END)
        entry_grau_escolaridade.delete(0, tk.END)

    cadastrar_window = tk.Toplevel()
    cadastrar_window.title("Cadastrar Aluno")

    label_nome = tk.Label(cadastrar_window, text="Nome do Aluno:")
    label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_nome = tk.Entry(cadastrar_window, width=50)
    entry_nome.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

    label_data_nascimento = tk.Label(cadastrar_window, text="Data de Nascimento (ddmmaaaa):")
    label_data_nascimento.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    entry_data_nascimento = tk.Entry(cadastrar_window, width=20)
    entry_data_nascimento.grid(row=1, column=1, padx=10, pady=5)

    label_email = tk.Label(cadastrar_window, text="E-mail:")
    label_email.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    entry_email = tk.Entry(cadastrar_window, width=50)
    entry_email.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

    label_rua = tk.Label(cadastrar_window, text="Rua:")
    label_rua.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    entry_rua = tk.Entry(cadastrar_window, width=50)
    entry_rua.grid(row=3, column=1, padx=10, pady=5, columnspan=2)

    label_bairro = tk.Label(cadastrar_window, text="Bairro:")
    label_bairro.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
    entry_bairro = tk.Entry(cadastrar_window, width=50)
    entry_bairro.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

    label_numero = tk.Label(cadastrar_window, text="Número da Residência:")
    label_numero.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
    entry_numero = tk.Entry(cadastrar_window, width=20)
    entry_numero.grid(row=5, column=1, padx=10, pady=5)

    label_contato_aluno = tk.Label(cadastrar_window, text="Contato do Aluno (11 dígitos):")
    label_contato_aluno.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
    entry_contato_aluno = tk.Entry(cadastrar_window, width=20)
    entry_contato_aluno.grid(row=6, column=1, padx=10, pady=5)

    label_nome_responsavel = tk.Label(cadastrar_window, text="Nome do Responsável:")
    label_nome_responsavel.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
    entry_nome_responsavel = tk.Entry(cadastrar_window, width=50)
    entry_nome_responsavel.grid(row=7, column=1, padx=10, pady=5, columnspan=2)

    label_contato_responsavel = tk.Label(cadastrar_window, text="Contato do Responsável (11 dígitos):")
    label_contato_responsavel.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)
    entry_contato_responsavel = tk.Entry(cadastrar_window, width=20)
    entry_contato_responsavel.grid(row=8, column=1, padx=10, pady=5)

    label_identidade = tk.Label(cadastrar_window, text="RG do Aluno (7 a 11 dígitos):")
    label_identidade.grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)
    entry_identidade = tk.Entry(cadastrar_window, width=20)
    entry_identidade.grid(row=9, column=1, padx=10, pady=5)

    label_grau_escolaridade = tk.Label(cadastrar_window, text="Grau de Escolaridade:")
    label_grau_escolaridade.grid(row=10, column=0, padx=10, pady=5, sticky=tk.W)
    entry_grau_escolaridade = tk.Entry(cadastrar_window, width=50)
    entry_grau_escolaridade.grid(row=10, column=1, padx=10, pady=5, columnspan=2)

    btn_cadastrar = tk.Button(cadastrar_window, text="Cadastrar", command=cadastrar)
    btn_cadastrar.grid(row=11, column=1, padx=10, pady=15)

    btn_limpar = tk.Button(cadastrar_window, text="Limpar Campos", command=limpar_campos)
    btn_limpar.grid(row=11, column=2, padx=10, pady=15)

    cadastrar_window.mainloop()

# Função para consultar aluno
def consultar_aluno():
    def consultar():
        matricula = entry_matricula_consulta.get().strip()
        cursor.execute('SELECT * FROM alunos WHERE matricula=?', (matricula,))
        aluno = cursor.fetchone()

        if aluno:
            messagebox.showinfo("Consulta de Aluno", f'''
                Nome: {aluno[1]}
                Data de Nascimento: {aluno[2]}
                E-mail: {aluno[3]}
                Endereço: {aluno[4]}
                Contato: {aluno[5]}
                Nome do Responsável: {aluno[6]}
                Contato do Responsável: {aluno[7]}
                Grau Escolaridade: {aluno[8]}
                Matrícula: {aluno[0]}
                Identidade: {aluno[9]}
            ''')
        else:
            messagebox.showerror("Erro", f"Aluno com matrícula {matricula} não encontrado.")

    consultar_window = tk.Toplevel()
    consultar_window.title("Consultar Aluno")

    label_matricula_consulta = tk.Label(consultar_window, text="Matrícula do Aluno:")
    label_matricula_consulta.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_matricula_consulta = tk.Entry(consultar_window, width=20)
    entry_matricula_consulta.grid(row=0, column=1, padx=10, pady=5)

    btn_consultar = tk.Button(consultar_window, text="Consultar", command=consultar)
    btn_consultar.grid(row=1, column=1, padx=10, pady=15)

    consultar_window.mainloop()

# Função para excluir aluno
def excluir_aluno():
    def excluir():
        matricula = entry_matricula_excluir.get().strip()
        cursor.execute('SELECT nome FROM alunos WHERE matricula=?', (matricula,))
        aluno = cursor.fetchone()

        if aluno:
            confirmar = messagebox.askquestion("Confirmar Exclusão", f"Você tem certeza que deseja excluir o aluno {aluno[0]}?")
            if confirmar == 'yes':
                cursor.execute('DELETE FROM alunos WHERE matricula=?', (matricula,))
                conn.commit()
                messagebox.showinfo("Sucesso", f"Aluno com matrícula {matricula} excluído com sucesso.")
        else:
            messagebox.showerror("Erro", f"Aluno com matrícula {matricula} não encontrado.")

    excluir_window = tk.Toplevel()
    excluir_window.title("Excluir Aluno")

    label_matricula_excluir = tk.Label(excluir_window, text="Matrícula do Aluno:")
    label_matricula_excluir.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_matricula_excluir = tk.Entry(excluir_window, width=20)
    entry_matricula_excluir.grid(row=0, column=1, padx=10, pady=5)

    btn_excluir = tk.Button(excluir_window, text="Excluir", command=excluir)
    btn_excluir.grid(row=1, column=1, padx=10, pady=15)

    excluir_window.mainloop()

# Função para listar todos os alunos
def listar_alunos():
    listar_window = tk.Toplevel()
    listar_window.title("Listar Alunos")

    scrollbar = tk.Scrollbar(listar_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(listar_window, yscrollcommand=scrollbar.set, width=100, height=20)
    listbox.pack(padx=10, pady=10)

    cursor.execute('SELECT nome, matricula FROM alunos')
    alunos = cursor.fetchall()
    for aluno in alunos:
        listbox.insert(tk.END, f"Nome: {aluno[0]}, Matrícula: {aluno[1]}")

    scrollbar.config(command=listbox.yview)

    listar_window.mainloop()

# Função principal para exibir o menu
def menu_principal():
    root = tk.Tk()
    root.title("Sistema de Gerenciamento de Alunos")

    label_titulo = tk.Label(root, text="Menu Principal", font=("Helvetica", 16))
    label_titulo.pack(pady=20)

    btn_cadastrar_aluno = tk.Button(root, text="Cadastrar Aluno", width=30, command=cadastrar_aluno)
    btn_cadastrar_aluno.pack(pady=10)

    btn_consultar_aluno = tk.Button(root, text="Consultar Aluno", width=30, command=consultar_aluno)
    btn_consultar_aluno.pack(pady=10)

    btn_excluir_aluno = tk.Button(root, text="Excluir Aluno", width=30, command=excluir_aluno)
    btn_excluir_aluno.pack(pady=10)

    btn_listar_alunos = tk.Button(root, text="Listar Alunos", width=30, command=listar_alunos)
    btn_listar_alunos.pack(pady=10)

    btn_sair = tk.Button(root, text="Sair", width=30, command=root.quit)
    btn_sair.pack(pady=10)

    root.mainloop()

# Executar o menu principal
if __name__ == "__main__":
    menu_principal()

# Fechar conexão com o banco de dados ao final
conn.close()
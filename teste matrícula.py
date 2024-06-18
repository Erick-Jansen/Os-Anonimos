import os
import datetime

# Inicialização de uma lista para armazenar os dados dos alunos
alunos = []
contador_aluno = 0

def gerar_matricula():
    global contador_aluno
    agora = datetime.datetime.now()
    ano = agora.year
    mes = agora.month
    contador_aluno += 1
    numero_sequencial = f'{contador_aluno:04d}'  # Número sequencial com 4 dígitos
    matricula = f'{ano}{mes:02d}{numero_sequencial}'
    return matricula

def cadastrar_aluno():
    nome = input('Insira o nome do aluno: ')
    idade = int(input('Insira a idade do aluno: '))
    email = input('Insira o e-mail do aluno: ')
    contato = input('Insira o número para contato: ')
    matricula = gerar_matricula()

    aluno = {
        'nome': nome,
        'idade': idade,
        'email': email,
        'contato': contato,
        'matricula': matricula
    }
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}\n")

def consultar_aluno():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, E-mail: {aluno['email']}, Contato: {aluno['contato']}, Matrícula: {aluno['matricula']}")
        print("")

def excluir_aluno():
    matricula = input("Digite a matrícula do aluno a ser excluído: ")
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            alunos.remove(aluno)
            print(f"Aluno com matrícula {matricula} excluído com sucesso!\n")
            return
    print(f"Aluno com matrícula {matricula} não encontrado.\n")

def menu():
    while True:
        print("\nMenu Principal: \n")
        print("1. Cadastrar Aluno")
        print("2. Consultar Aluno")
        print("3. Excluir Aluno")
        print("4. Sair")
        opcao = input("Digite sua opção: \n -->")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            consultar_aluno()
        elif opcao == "3":
            excluir_aluno()
        elif opcao == "4":
            break
        else:
            print("Opção inválida! Escolha uma das opções disponíveis")

if __name__ == "__main__":
    menu()



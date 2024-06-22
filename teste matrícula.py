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

def calcular_idade(data_nascimento):
    hoje = datetime.datetime.now()
    idade_anos = hoje.year - data_nascimento.year

    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade_anos -= 1

    return idade_anos

def cadastrar_aluno():
    while True:
        nome = input('Insira o nome do aluno (nome e sobrenome): ').strip().title()
        if ' ' in nome and all(part.isalpha() for part in nome.split()):
            break
        else:
            print("Por favor, insira um nome válido contendo apenas letras, com pelo menos um nome e um sobrenome.")
    
    while True:
        try:
            dia = int(input('Insira o dia de nascimento (DD): '))
            mes = int(input('Insira o mês de nascimento (MM): '))
            ano = int(input('Insira o ano de nascimento (AAAA): '))
            data_nascimento = datetime.datetime(ano, mes, dia)
            idade_anos = calcular_idade(data_nascimento)
            break
        except ValueError:
            print("Data de nascimento inválida. Tente novamente.")
    
    while True:
        email = input('Insira o e-mail do aluno: ').strip()
        if "@" in email and email.endswith(".com"):
            break
        else:
            print("Por favor, insira um e-mail válido contendo '@' e terminando com '.com'.")

    rua = input('Insira a rua do aluno: ').strip().title()
    bairro = input('Insira o bairro do aluno: ').strip().title()
    
    while True:
        numero = input('Insira o número da residência do aluno: ').strip()
        if numero.isdigit():
            break
        else:
            print("Por favor, insira um número válido para a residência.")

    endereco = f'Rua: {rua}, Bairro: {bairro}, Número: {numero}'

    while True:
        contato_aluno = input('Insira o número de contato do aluno (11 dígitos): ').strip()
        if contato_aluno.isdigit() and len(contato_aluno) == 11:
            contato_aluno_formatado = f'({contato_aluno[:2]}) {contato_aluno[2]} {contato_aluno[3:7]}-{contato_aluno[7:]}'
            break
        else:
            print("Por favor, insira um número de contato válido com 11 dígitos.")

    while True:
        nome_responsavel = input('Escreva o nome do responsável: ').strip().title()
        if ' ' in nome_responsavel and all(part.isalpha() for part in nome_responsavel.split()):
            break
        else:
            print("Por favor, insira um nome válido contendo apenas letras, com pelo menos um nome e um sobrenome.")

    while True:
        contato_responsavel = input('Escreva o número para contato do responsável (11 dígitos): ').strip()
        if contato_responsavel.isdigit() and len(contato_responsavel) == 11:
            contato_responsavel_formatado = f'({contato_responsavel[:2]}) {contato_responsavel[2]} {contato_responsavel[3:7]}-{contato_responsavel[7:]}'
            break
        else:
            print("Por favor, insira um número de contato válido com 11 dígitos.")

    while True:
        identidade = input('Escreva o RG do aluno (7 a 11 dígitos): ').strip()
        if identidade.isdigit() and 7 <= len(identidade) <= 11:
            identidade_formatada = f'{identidade[:-1]}-{identidade[-1]}'
            break
        else:
            print("Por favor, insira um RG válido com 7 a 11 dígitos.")
    
    grau_escolaridade = input('Qual o grau que o aluno está sendo matrículado?: ').strip().title()
    
    matricula = gerar_matricula()
    
    aluno = {
        'nome': nome,
        'data_nascimento': data_nascimento.strftime("%d/%m/%Y"),
        'idade_anos': idade_anos,
        'email': email,
        'endereco': endereco,
        'contato_aluno': contato_aluno_formatado,
        'nome_responsavel': nome_responsavel,
        'contato_responsavel': contato_responsavel_formatado,
        'grau_escolaridade': grau_escolaridade,
        'matricula': matricula,
        'identidade': identidade_formatada,
    }
    
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}\n")
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def consultar_aluno():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Data de Nascimento: {aluno['data_nascimento']}, Idade: {aluno['idade_anos']} anos, E-mail: {aluno['email']}, Endereço: {aluno['endereco']}, Contato: {aluno['contato_aluno']}, Matrícula: {aluno['matricula']}, Identidade: {aluno['identidade']}")
        print("")
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def excluir_aluno():
    os.system('cls' if os.name == 'nt' else 'clear')
    matricula = input("Digite a matrícula do aluno a ser excluído: ")
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            confirmar = input(f'Você tem certeza que gostaria de excluir o aluno {aluno["nome"]} do sistema? \n Se sim, confirme com "s", caso não tecle enter. \n--> ')
            if confirmar.lower() == 's':
                alunos.remove(aluno)
                print(f"Aluno com matrícula {matricula} excluído com sucesso!\n")
            else:
                print("Exclusão cancelada.\n")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            return
    print(f"Aluno com matrícula {matricula} não encontrado.\n")
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

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
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    menu()

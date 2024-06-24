import os
import datetime


alunos = []
contador_aluno = 0

def gerar_matricula():                                  
    global contador_aluno
    agora = datetime.datetime.now()
    ano = agora.year
    mes = agora.month
    contador_aluno += 1
    numero_sequencial = f'{contador_aluno:04d}'
    matricula = f'{ano}{mes:02d}{numero_sequencial}'
    return matricula

def calcular_idade(data_nascimento):
    hoje = datetime.datetime.now()
    idade_anos = hoje.year - data_nascimento.year
    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade_anos -= 1
    return idade_anos

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
        print(f"{e}. Tente novamente.")
        return None

def cadastrar_aluno():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        nome = input('Insira o nome do aluno (nome e sobrenome): ').strip().title()
        if ' ' in nome and all(part.isalpha() for part in nome.split()):
            break
        else:
            print("Por favor, insira um nome válido contendo apenas letras, com pelo menos um nome e um sobrenome.")
    
    while True:
        data_nascimento_str = input('Insira a data de nascimento do aluno (ddmmaaaa): ').strip()
        data_nascimento = validar_data_nascimento(data_nascimento_str)
        if data_nascimento:
            idade_anos = calcular_idade(data_nascimento)
            break

    while True:
        email = input('Insira o e-mail do aluno: ').strip()
        if "@" in email and email.endswith(".com"):
            break
        else:
            print("Por favor, insira um e-mail válido contendo '@' e terminando com '.com'.")

    rua = input('Insira a rua do aluno: ').strip().title()
    bairro = input('Insira o bairro do aluno: ').strip().title()
    
    while True:
        numero = input('Insira o número da residência do aluno (até 6 dígitos): ').strip()
        if numero.isdigit() and len(numero) <= 6:
            break
        else:
            print("Por favor, insira um número válido para a residência com até 6 dígitos.")

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
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if not alunos:
            print("Nenhum aluno cadastrado.\n")
        else:
            print("a. Consultar aluno por matrícula")
            print("b. Consultar dados dos responsáveis")
            print("c. Listar todos os alunos matriculados")
            print("d. Voltar ao menu principal")
            opcao = input("Digite sua opção (a, b, c ou d): ")

            if opcao == "a":
                matricula = input("Digite a matrícula do aluno: ").strip()
                encontrado = False
                for aluno in alunos:
                    if aluno['matricula'] == matricula:
                        encontrado = True
                        print(f"\nDados do Aluno:\nNome: {aluno['nome']}\nData de Nascimento: {aluno['data_nascimento']}\nIdade: {aluno['idade_anos']} anos\nE-mail: {aluno['email']}\nEndereço: {aluno['endereco']}\nContato: {aluno['contato_aluno']}\nNome do Responsável: {aluno['nome_responsavel']}\nContato do Responsável: {aluno['contato_responsavel']}\nGrau Escolaridade: {aluno['grau_escolaridade']}\nMatrícula: {aluno['matricula']}\nIdentidade: {aluno['identidade']}")
                        break
                if not encontrado:
                    print(f"Aluno com matrícula {matricula} não encontrado.")
            elif opcao == "b":
                matricula = input("Digite o nome completo do aluno para consultar os dados dos responsáveis: ").strip()
                encontrado = False
                for aluno in alunos:
                    if aluno['matricula'] == matricula:
                        encontrado = True
                        print(f"\nDados do Responsável:\nNome: {aluno['nome_responsavel']}\nContato: {aluno['contato_responsavel']}")
                        break
                if not encontrado:
                    print(f"Aluno de matrícula {matricula} não encontrado.")
            elif opcao == "c":
                print("\nLista de todos os alunos matriculados:")
                for aluno in alunos:
                    print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}")
            elif opcao == "d":
                break
            else:
                print("Opção inválida! Por favor, escolha a, b, c ou d.")
        
        input("\nPressione Enter para continuar...")

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




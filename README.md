# Os-Anonimos

Matrícula do Aluno (README)

```mermaid
graph TD
    A[Menu_Principal] -->|1. Cadastrar Aluno| B[Cadastrar Aluno]
    A -->|2. Consultar Aluno| C[Consultar Aluno]
    A -->|3. Excluir Aluno| D[Excluir Aluno]
    A -->|4. Sair| E[Sair]

    B --> B1[Insira o nome do aluno nome e sobrenome]
    B1 --> B2{Nome válido?}
    B2 -->|Sim| B3[Insira a data de nascimento]
    B2 -->|Não| B1
    B3 --> B4{Data válida e aluno tem pelo menos 4 anos?}
    B4 -->|Sim| B5[Insira o e-mail]
    B4 -->|Não| B3
    B5 --> B6{E-mail válido?}
    B6 -->|Sim| B7[Insira a rua]
    B6 -->|Não| B5
    B7 --> B8[Insira o bairro]
    B8 --> B9[Insira o número da residência]
    B9 --> B10{Número válido?}
    B10 -->|Sim| B11[Insira o número de contato do alunO]
    B10 -->|Não| B9
    B11 --> B12{Contato válido?}
    B12 -->|Sim| B13[Insira o nome do responsável]
    B12 -->|Não| B11
    B13 --> B14{Nome do responsável válido?}
    B14 -->|Sim| B15[Insira o número de contato do responsável]
    B14 -->|Não| B13
    B15 --> B16{Contato válido?}
    B16 -->|Sim| B17[Insira o RG do aluno]
    B16 -->|Não| B15
    B17 --> B18{RG válido?}
    B18 -->|Sim| B19[Insira o grau de escolaridade]
    B18 -->|Não| B17
    B19 --> B20[Gerar matrícula]
    B20 --> B21[Salvar dados do aluno]
    B21 --> A

    C -->|Se há alunos cadastrados| C1[Listar alunos]
    C1 --> A
    C -->|Se não há alunos cadastrados| C2[Mensagem: Nenhum aluno cadastrado]
    C2 --> A

    D --> D1[Digite a matrícula do aluno a ser excluído]
    D1 --> D2{Matrícula encontrada?}
    D2 -->|Sim| D3[Confirmação de exclusão]
    D2 -->|Não| D6[Mensagem: Matrícula não encontrada]
    D3 -->|Confirmar| D4[Excluir aluno]
    D4 --> D5[Mensagem: Aluno excluído com sucesso]
    D3 -->|Cancelar| A
    D5 --> A
    D6 --> A

    E --> F[Fim]


```

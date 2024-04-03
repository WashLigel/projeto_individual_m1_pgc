# Função para exibir o menu
def exibir_menu():
    menu = """
╔═════════════════════════════════════╗
║           MENU DE OPÇÕES            ║
╠═════════════════════════════════════╣
║ 1. Buscar candidatos por critérios  ║
║═════════════════════════════════════╣
║ 2. Adicionar ou excluir funcionários║
║═════════════════════════════════════╣
║              3. Sair                ║
╚═════════════════════════════════════╝
"""
    print(menu)

# Função para buscar candidatos com base nos critérios digitados pelo usuário
def buscar_candidato_por_critérios(candidatos, nota_e, nota_t, nota_p, nota_s):
    candidatos_encontrados = []
    for candidato in candidatos:
        resultado = candidato["resultado"]
        e, t, p, s = resultado.split("_")
        if int(e[1:]) >= nota_e and int(t[1:]) >= nota_t and int(p[1:]) >= nota_p and int(s[1:]) >= nota_s:
            candidato_com_pontuacao = candidato["nome"] + " " + resultado
            candidatos_encontrados.append(candidato_com_pontuacao)
    return candidatos_encontrados

# Lista de candidatos e seus resultados
candidatos = [
    {"nome": "João", "resultado": "e5_t10_p8_s8"},
    {"nome": "Maria", "resultado": "e10_t7_p7_s8"},
    {"nome": "Pedro", "resultado": "e8_t5_p4_s9"},
    {"nome": "Ana", "resultado": "e2_t2_p2_s1"},
    {"nome": "Carlos", "resultado": "e10_t10_p8_s9"}
]

# Função para adicionar um novo funcionário
def adicionar_funcionario():
    nome = input("Digite o nome do novo funcionário: ")
    resultado = input("Digite o resultado do novo funcionário no formato 'ex_tx_px_sx': ")
    candidatos.append({"nome": nome, "resultado": resultado})
    print(f"Funcionário {nome} adicionado com sucesso!")

# Função para excluir um funcionário
def excluir_funcionario():
    nome = input("Digite o nome do funcionário que deseja excluir: ")
    for candidato in candidatos:
        if candidato["nome"] == nome:
            candidatos.remove(candidato)
            print(f"Funcionário {nome} excluído com sucesso!")
            return
    print(f"Funcionário {nome} não encontrado.")

# Exemplo de utilização
while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nota_e = int(input("Digite a nota mínima desejada para E: "))
        nota_t = int(input("Digite a nota mínima desejada para T: "))
        nota_p = int(input("Digite a nota mínima desejada para P: "))
        nota_s = int(input("Digite a nota mínima desejada para S: "))

        candidatos_encontrados = buscar_candidato_por_critérios(candidatos, nota_e, nota_t, nota_p, nota_s)

        if candidatos_encontrados:
            print("Candidatos disponíveis com notas maiores ou iguais às informadas:")
            for candidato in candidatos_encontrados:
                print(candidato)
        else:
            print("Nenhum candidato disponível com as notas mínimas informadas.")
    elif opcao == "2":
        sub_opcao = input("Digite 'a' para adicionar um funcionário ou 'e' para excluir um funcionário: ")
        if sub_opcao == "a":
            adicionar_funcionario()
        elif sub_opcao == "e":
            excluir_funcionario()
        else:
            print("Opção inválida! Por favor, digite 'a' para adicionar ou 'e' para excluir.")
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")

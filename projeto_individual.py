# Lista de candidatos e seus resultados
candidatos = [
    {"nome": "João", "resultado": "e5_t10_p8_s8"},
    {"nome": "Arthur", "resultado": "e10_t7_p7_s8"},
    {"nome": "Yasmin", "resultado": "e8_t5_p4_s9"},
    {"nome": "Fernanda", "resultado": "e2_t2_p2_s1"},
    {"nome": "Karla", "resultado": "e10_t10_p8_s9"}
]

# Função para calcular a diferença absoluta entre as notas de um candidato e as notas digitadas
def diferenca_notas(candidato, nota_e, nota_t, nota_p, nota_s):
    resultado = candidato["resultado"]
    e, t, p, s = resultado.split("_")
    diff_e = abs(int(e[1:]) - nota_e)
    diff_t = abs(int(t[1:]) - nota_t)
    diff_p = abs(int(p[1:]) - nota_p)
    diff_s = abs(int(s[1:]) - nota_s)
    return diff_e + diff_t + diff_p + diff_s

# Função para buscar candidato com notas mais próximas das notas digitadas
def buscar_candidato_proximo(candidatos, nota_e, nota_t, nota_p, nota_s):
    candidato_proximo = None
    menor_diferenca = float('inf')  # Inicializa a menor diferença com infinito
    for candidato in candidatos:
        diferenca = diferenca_notas(candidato, nota_e, nota_t, nota_p, nota_s)
        if diferenca < menor_diferenca:
            candidato_proximo = candidato
            menor_diferenca = diferenca
    return candidato_proximo

# Menu de opções
def menu():
    print("""
  ___________________________________________________________________
 |                                                                   |
 |                   Menu:                                           |
 |                                                                   |
 |   [1] Buscar candidato por critérios                              |
 |   [2] Sair                                                        |
 |___________________________________________________________________|
""")

# Exemplo de utilização
while True:
    menu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nota_e = int(input("Digite a nota mínima desejada para E: "))
        nota_t = int(input("Digite a nota mínima desejada para T: "))
        nota_p = int(input("Digite a nota mínima desejada para P: "))
        nota_s = int(input("Digite a nota mínima desejada para S: "))

        candidato_proximo = buscar_candidato_proximo(candidatos, nota_e, nota_t, nota_p, nota_s)

        if candidato_proximo:
            print("Candidato mais próximo das notas informadas:")
            print("Nome:", candidato_proximo["nome"])
            print("Notas:", candidato_proximo["resultado"])
        else:
            print("Nenhum candidato disponível.")
    elif opcao == "2":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, digite um número de opção válido.")

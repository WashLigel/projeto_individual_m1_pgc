# Lista de candidatos e seus resultados
candidatos = [
    {"nome": "Candidato 1", "resultado": "e5_t10_p8_s8"},
    {"nome": "Candidato 2", "resultado": "e10_t7_p7_s8"},
    {"nome": "Candidato 3", "resultado": "e8_t5_p4_s9"},
    {"nome": "Candidato 4", "resultado": "e2_t2_p2_s1"},
    {"nome": "Candidato 5", "resultado": "e10_t10_p8_s9"}
]

# Função para buscar candidatos com base nos critérios digitados pelo usuário
def buscar_candidato_por_critérios(candidatos, nota_e, nota_t, nota_p, nota_s):
    candidatos_encontrados = []
    for candidato in candidatos:
        resultado = candidato["resultado"]
        e, t, p, s = resultado.split("_")
        if int(e[1:]) >= nota_e and int(t[1:]) >= nota_t and int(p[1:]) >= nota_p and int(s[1:]) >= nota_s:
            candidatos_encontrados.append(candidato["nome"])
    return candidatos_encontrados

# Exemplo de utilização
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

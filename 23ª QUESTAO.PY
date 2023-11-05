def calcular_estatisticas_espectadores(respostas):
    total_idade_otimo = 0
    count_otimo = 0
    count_regular = 0
    count_bom = 0

    for idade, opiniao in respostas:
        if opiniao == 3:
            total_idade_otimo += idade
            count_otimo += 1
        elif opiniao == 1:
            count_regular += 1
        elif opiniao == 2:
            count_bom += 1

    if count_otimo > 0:
        media_idade_otimo = total_idade_otimo / count_otimo
        print(f"A média de idade das pessoas que responderam ótimo é {media_idade_otimo:.2f}.")

    print(f"A quantidade de pessoas que respondeu regular é {count_regular}.")

    total_pessoas = len(respostas)
    percentual_bom = (count_bom / total_pessoas) * 100
    print(f"A percentagem de pessoas que respondeu bom é {percentual_bom:.2f}%.")

respostas = []
for i in range(15):
    idade = int(input(f"Digite a idade do {i+1}º espectador: "))
    opiniao = int(input(f"Digite a opinião do {i+1}º espectador (Digite 1 para regular, 2 para bom, 3 para ótimo): "))
    respostas.append((idade, opiniao))

calcular_estatisticas_espectadores(respostas)

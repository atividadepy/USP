def calcular_resultados_pesquisa(resultados):
    count_sim = 0
    count_nao = 0
    count_mulheres_sim = 0
    count_homens = 0
    count_homens_nao = 0

    for sexo, resposta in resultados:
        if resposta == 'S':
            count_sim += 1
            if sexo == 'F':
                count_mulheres_sim += 1
        elif resposta == 'N':
            count_nao += 1
            if sexo == 'M':
                count_homens_nao += 1
                count_homens += 1
        if sexo == 'M':
            count_homens += 1

    print(f"O número de pessoas que respondeu sim é {count_sim}.")
    print(f"O número de pessoas que respondeu não é {count_nao}.")
    print(f"O número de mulheres que respondeu sim é {count_mulheres_sim}.")

    if count_homens > 0:
        percentual_homens_nao = (count_homens_nao / count_homens) * 100
        print(f"A percentagem de homens que respondeu não é {percentual_homens_nao:.2f}%.")

resultados = []
for i in range(10):
    sexo = input(f"Digite o sexo da {i+1}ª pessoa (M para masculino, F para feminino): ")
    resposta = input(f"Digite a resposta (S para sim, N para não): ")
    resultados.append((sexo, resposta))

calcular_resultados_pesquisa(resultados)

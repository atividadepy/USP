def calcular_medias_faixa_etaria(dados):
    faixas_etarias = {
        "1 a 10 anos": [],
        "11 a 20 anos": [],
        "21 a 30 anos": [],
        "maiores de 30": []
    }
    for idade, peso in dados:
        if idade >= 1 and idade <= 10:
            faixas_etarias["1 a 10 anos"].append(peso)
        elif idade >= 11 and idade <= 20:
            faixas_etarias["11 a 20 anos"].append(peso)
        elif idade >= 21 and idade <= 30:
            faixas_etarias["21 a 30 anos"].append(peso)
        else:
            faixas_etarias["maiores de 30"].append(peso)

    for faixa, pesos in faixas_etarias.items():
        if pesos:
            media_peso = sum(pesos) / len(pesos)
            print(f"A média de peso para a faixa etária {faixa} é {media_peso:.2f}.")
        else:
            print(f"Não há pessoas na faixa etária {faixa}.")

dados = []
for i in range(15):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    dados.append((idade, peso))

calcular_medias_faixa_etaria(dados)

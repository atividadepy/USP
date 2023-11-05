idades = []
alturas = []
while True:
    idade = int(input("Digite a idade (0 para finalizar): "))
    if idade <= 0:
        break
    altura = float(input("Digite a altura: "))
    idades.append(idade)
    alturas.append(altura)

media_alturas_mais_50 = sum(alturas[i] for i in range(len(idades)) if idades[i] > 50) / sum(1 for idade in idades if idade > 50)

print("Média das alturas das pessoas com mais de 50 anos: ", media_alturas_mais_50)
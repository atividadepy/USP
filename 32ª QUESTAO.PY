numeros = []
while True:
    num = int(input("Digite um número (0 para finalizar): "))
    if num == 0:
        break
    numeros.append(num)

numeros_inferiores_35 = sum(1 for num in numeros if num < 35)
media_positivos = sum(num for num in numeros if num > 0) / sum(1 for num in numeros if num > 0)
percentagem_50_100 = sum(1 for num in numeros if 50 <= num <= 100) / len(numeros) * 100
percentagem_10_20_menor_50 = sum(1 for num in numeros if 10 <= num <= 20 and num < 50) / len(numeros) * 100

print("Quantidade de números inferiores a 35: ", numeros_inferiores_35)
print("Média dos números positivos: ", media_positivos)
print("Percentagem de números entre 50 e 100 entre todos os números digitados: ", percentagem_50_100)
print("Percentagem de números entre 10 e 20 entre os números menores que 50: ", percentagem_10_20_menor_50)
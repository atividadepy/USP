numeros = []
while True:
    num = int(input("Digite um número (0 para finalizar): "))
    if num == 0:
        break
    numeros.append(num)

soma_positivos = sum(num for num in numeros if num > 0)
soma_negativos = sum(num for num in numeros if num < 0)

print("Soma dos números positivos: ", soma_positivos)
print("Soma dos números negativos: ", soma_negativos)
print("Soma das duas somas parciais: ", soma_positivos + soma_negativos)
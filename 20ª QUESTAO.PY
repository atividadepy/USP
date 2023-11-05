valores = []
valor = 1
while valor != 0:
    valor = int(input('Digite um valor inteiro e positivo (ou 0 para sair): '))
    if valor < 0:
        print("Numero negativo, digite novamente ")
    elif valor != 0:
        valores.append(valor)
if valores:
    maior = max(valores)
    menor = min(valores)
    print(f'''O maior valor e: {maior}
O menor valor e: {menor}''')
else:
    print("Nenhum valor valido foi digitado ")
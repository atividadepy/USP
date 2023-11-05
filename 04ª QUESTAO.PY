valores = []
for x in range(4):
    valor = float(input('Me diga um valor: '))
    valores.append(valor)
valores.sort()
print('Valores em ordem decrescente: ')
for valor in valores:
    print(valor)

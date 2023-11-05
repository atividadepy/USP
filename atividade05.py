clintes = []
for i in range(2):
    nome = input('M ediga seu nome: ')
    compras_antigas = float(input('Me diga o valor das compras do ano passado: '))
    if (compras_antigas >= 1.000):
        bonus = (compras_antigas * 10) / 100
    else:
        bonus = (compras_antigas * 15) / 100
    clintes.append((nome,compras_antigas,bonus))
for clinte in clintes:
    nome,compras_antigas,bonus = clinte
    print(7*"-=-")
    print(f'clinte {nome}, compras no ano passado: R$ {compras_antigas}, Ganhou um bônos de: R$ {bonus }')
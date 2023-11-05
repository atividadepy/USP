def calcular_rendimento(tipo, valor):
    if tipo == 'Poupança':
        return valor * 0.015
    elif tipo == 'Poupança plus':
        return valor * 0.02
    elif tipo == 'Fundos de renda fixa':
        return valor * 0.04

def menu():
    total_investido = 0
    total_juros = 0
    while True:
        codigo = int(input("Digite o código do cliente (0 para sair): "))
        if codigo <= 0:
            break
        tipo = input("Digite o tipo da conta (Poupança, Poupança plus, Fundos de renda fixa): ")
        valor = float(input("Digite o valor investido: "))
        rendimento = calcular_rendimento(tipo, valor)
        print("Rendimento mensal: ", rendimento)
        total_investido += valor
        total_juros += rendimento
    print("Total investido: ", total_investido)
    print("Total de juros pagos: ", total_juros)

menu()
print('Efetue o pagamento:')
print(7*"-=")

valor_vista  = valor_prazo = valor_total = 0 
for i in range(15):
    codigo = input("Digite o codigo da transação (V para á vista e P para a prazo)")
    valor = float(input("Digite o valor da transação: "))
    valor_total += valor

    if codigo == 'v':
        valor_vista += valor
    else:
        valor_prazo += valor
valor_primeira_prestacao = valor_prazo / 3
print(f''' 
O valor total das compras a vista foi: R${valor_vista:.2f}
O valor total das compras a prazo foi: R${valor_prazo:.2f}
O valor total das compras efetuadas foi: R${valor_total:.2f}
O valor da primeira prestação a prazo foi: R${valor_primeira_prestacao}
''')

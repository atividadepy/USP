acoes = []
while True:
    acao = input("Digite o tipo da ação (F para finalizar): ")
    if acao == "F":
        break
    preco_compra = float(input("Digite o preço de compra da ação: "))
    preco_venda = float(input("Digite o preço de venda da ação: "))
    lucro = preco_venda - preco_compra
    acoes.append((acao, lucro))

lucro_total = sum(lucro for acao, lucro in acoes)
acoes_com_lucro_maior_1000 = sum(1 for acao, lucro in acoes if lucro > 1000)
acoes_com_lucro_menor_200 = sum(1 for acao, lucro in acoes if lucro < 200)

print("Lucro de cada ação: ", [(acao, lucro) for acao, lucro in acoes])
print("Quantidade de ações com lucro superior a R$ 1.000,00: ", acoes_com_lucro_maior_1000)
print("Quantidade de ações com lucro inferior a R$ 200,00: ", acoes_com_lucro_menor_200)
print("Lucro total da empresa: ", lucro_total)
produtos = []
codigo = int(input("Digite o código do produto: "))
while codigo >= 0:
    preco = float(input("Digite o preço de custo do produto: "))
    produtos.append({"codigo": codigo, "preco": preco})
    codigo = int(input("Digite o código do produto: "))
media_preco = sum(produto["preco"] for produto in produtos) / len(produtos)
media_preco_aumento = sum(produto["preco"] * 1.2 for produto in produtos) / len(produtos)
for produto in produtos:
    novo_preco = produto["preco"] * 1.2
    print(f"Código: {produto['codigo']}, Novo preço: {novo_preco}")
print(f"Média dos preços sem aumento: {media_preco}")
print(f"Média dos preços com aumento: {media_preco_aumento}")
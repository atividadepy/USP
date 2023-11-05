preco_base = 5.00
ingresso_base = 120
despesas = 200.00

lucro_maximo = 0.0
preco_maximo = 0.0
ingresso_maximo = 0

for preco_ingresso in range(500, 0, -50):
    preco_real = preco_ingresso / 100
    aumento_ingresso = 26 if preco_real < 5.00 else 0

    ingresso_vendidos = ingresso_base + aumento_ingresso
    lucro_esperado = (preco_real * ingresso_vendidos) - despesas

    if lucro_esperado > lucro_maximo:
        lucro_maximo = lucro_esperado
        preco_maximo = preco_real
        ingresso_maximo = ingresso_vendidos
        print(f'O preço do ingresso: R$ {preco_real:.2f}, ingressos vendidos: {ingresso_vendidos}, lucro esperado: {lucro_esperado}')
    print('\nLucro Maximo Esperando: ')
    print(f'Preço do ingresso: R$ {preco_maximo}')
    print(f'Quantidade de ingressos vendidos: {ingresso_maximo}')
    print(f'Total de lucro: {lucro_maximo}')
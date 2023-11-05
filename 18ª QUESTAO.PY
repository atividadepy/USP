def calcular_preco(valor_carro):
    desconto_avista = 0.2
    acrescimo_parcela = {
        6: 0.03,
        12: 0.06,
        18: 0.09,
        24: 0.12,
        30: 0.15,
        36: 0.18,
        42: 0.21,
        48: 0.24,
        54: 0.27,
        60: 0.30,
    }
    preco_avista = valor_carro * (1 - desconto_avista)
    print(f"{preco_avista:.2f } | Á VISTA ")
    for parcela , acrescimos in acrescimo_parcela.items():
        preco_parcela = valor_carro * (1+ acrescimos)
        valor_parcela = preco_parcela / parcela
        print(f"{preco_parcela:.2f} | {parcela} | {valor_parcela:.2f}")
calcular_preco(20000)
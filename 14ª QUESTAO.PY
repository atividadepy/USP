
idade_peso = 0
contador_altura = 0
contador_olhos_azul = 0 
contagem_ruivas_azul = 0
for i in range(20):
    idade = int(input("Me diga sua idade: "))
    peso = float(input("Me diga quantos Kg você tem: "))
    altura = float(input("Me diga sua altura: "))
    cor_olhos = input('''Qual a cor do seus olhos?
    Se for verde digite ( verde )
    Se for azul digite ( azul )
    Se for preto digite ( preto )
    Se for castanho digite ( castalho ):  ''')
    cabelo = input('''Qual a cor do seu cabelo?
    Se for ruiva digite ( R )
    Se for preto digite ( P )
    Se for loiro digite ( L )
    Se for castanho digite ( C )''')
    if idade > 50 and peso < 60:
        idade_peso += 1

    if altura < 1.50:
        contador_altura += 1
    
    if cor_olhos == 'azul':
        contador_olhos_azul += 1

    if cabelo == "r" and cor_olhos != "azul":
        contagem_ruivas_azul += 1 

print(f'A quantidade de pessoas superio a 50 anos e inferior a 60Kg e de: {idade_peso}')
print(f'A media de pessoas com altura inferior a 1.50 foi de 20/{contador_altura}')
print(f'A porcentagem de pessoas com os olhos azuis foi de {(contador_olhos_azul /20) * 100:.2f}%')
print(f'A quantidades de pessoas ruivas que não possui olhos azuis são de 20/{contagem_ruivas_azul}')
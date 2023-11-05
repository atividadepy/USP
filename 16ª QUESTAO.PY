contagem_idade = 0
peso_altura = 0 
percentagem_pessoas = 0
for i in range(10):
    idade = int(input('Me diga sua idade: '))
    peso = int(input('Me diga seu peso: '))
    altura = float(input('Me diga sua altura: '))

    contagem_idade += idade

    if peso > 90 and altura < 1.50:
        peso_altura += 1
    
    if 10 <= idade <= 30 and altura >= 1.90:
        percentagem_pessoas += 1
    
print(f"A media das idades das 10 pessoas e de: {contagem_idade / 10:.1f}")
print(f"A quantidade de pessoas com o peso superior a 90kg e altura inferior a 1.50 e de: {peso_altura}")
print(f"A percentagem de pessoas com a idade entre 10 a 30 anos entre as pessoas que medem mais de 1,90 e de {(percentagem_pessoas / 10) * 100:.2f}%")
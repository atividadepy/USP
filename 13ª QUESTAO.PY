acima_90kg = 0
soma_idade = 0
for i in range(1,8):
    idade = int(input('Me diga sua idade: '))
    peso = int(input('Me diga quantos kg você tem: '))
    soma_idade += idade
    if peso > 90:
        acima_90kg += 1
    
print(f'A quantidade de pessoas acima de 90kg e {acima_90kg}')
print(f'A media das idades das pessoas e {soma_idade / 7}')
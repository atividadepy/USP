acima_50 = 0
contador_pessoas = 0
contador_altura = 0
menos_40kg = 0
for i in range(1,26):
    idade = int(input('Me diga sua idade: '))
    peso = int(input('Me diga seu peso: '))
    altura = float(input('Me diga sua altura: '))

    if idade > 50:
        acima_50 += 1

    if 10 <= idade <= 20:
        contador_altura += altura
        contador_pessoas += 1
        media_altura = contador_altura / contador_pessoas

    if peso <= 40:
        menos_40kg += 1
        porcentagem_kg = (menos_40kg / 25) * 100

print(f'De 25 pessoas, so {acima_50} tem acima de 50 anos.')
print(f'A media de altura das pessoas de 10 a 20 anos são: {media_altura} metros ')
print(f'A porcentagem de pessoas com menos de 40kg e de: {porcentagem_kg}%')
acima_18 = 0
for x in  range(4):
    idade = int(input('Me diga sua idade: '))

    if (idade > 18):
        acima_18 += 1
print(f'{acima_18} São acima de 18 anos ')
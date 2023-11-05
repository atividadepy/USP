faixa1 = faixa2 = faixa3 = faixa4 = faixa5 = 0
for i in range(4):
    idade =  int(input('Me diga sua idade: '))
    if idade < 18:
        faixa1+=1
    elif  18 <= idade <=30:
        faixa2+=1
    elif  31<= idade <= 45:
        faixa3+=1
    elif  46<= idade <= 60:
        faixa4+=1
    else:
        faixa5+=1
total_pesssoas = 4
porcentagem_faixa1 = (faixa1 / total_pesssoas) *100
porcentagem_faixa5 = (faixa5 / total_pesssoas) *100
print(f'''Faixa Etaria 0-17 anos: {faixa1} pessoas
Faixa Etaria 18-30 anos: {faixa2} pessoas
Faixa Etaria 31-45 anos: {faixa3} pessoas
Faixa Etaria 46-60 anos: {faixa4} pessoas
Faixa Etaria 61 anos: {faixa5} pessoas
''')

print(f'Porcentagem de pessoas na faixa Etaria 0-17 anos: {porcentagem_faixa1:.2f}')
print(f'Porcentagem de pessoas na faixa Etaria 61 anos: {porcentagem_faixa5:.2f}')
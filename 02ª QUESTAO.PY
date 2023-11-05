n = int(input('Me diga um numero'))
soma = 0.0
if (n<soma):
    print('[ERRO] Me diga um numero inteiro! ')
else:
    for i in range (1,n+1):
        soma += 1/i
        print(f'A soma e: {soma:.2f}')

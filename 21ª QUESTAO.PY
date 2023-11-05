def calcula_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial

n = int(input("Digite um numero inteiro para calcular o fatorial: "))
resultado = calcula_fatorial(n)
print(f"O fatorial de {n} e {resultado}")
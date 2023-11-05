idades = []
idade = 1  # Inicialização para entrar no loop

while idade != 0:
    idade = int(input("Digite uma idade (ou 0 para sair): "))
    if idade != 0:
        idades.append(idade)

if idades:
    media = sum(idades) / len(idades)
    print(f"A média das idades é: {media:.2f}")
else:
    print("Nenhuma idade válida foi inserida.")

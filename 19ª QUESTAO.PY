idades = []
idade = 1
while idade != 0:
    idade = int(input('Digite sua idade (ou 0 para sair:) '))
    if idade != 0:
        idades.append(idade)
if idades:
    media = sum(idades) / len(idades)
    print(f"A media das idades e {media:.2f}")
else:
    print("Nenhuma idade foi fornecida.")
contagem_idade = 0
contagem_f = 0
contagem_m = 0
for i in range(7):
    idade = int(input("Me diga sua idade: "))
    sexo = input("Me diga seu sexo: M pra masculino e F pra feminino: ")
    
    contagem_idade += idade

    if sexo == "f":
        contagem_f += idade

    if sexo == "m":
        contagem_m += idade

print(f"A media da idade do grupo e de: {contagem_idade / 7:.1f} anos")
print(f"A idade media das mulheres e de: {contagem_f / 7:.1f}")
print(f"A idade media dos homens e de : {contagem_m / 7:.1f}")
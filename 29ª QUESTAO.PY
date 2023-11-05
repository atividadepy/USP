habitantes = []
idade = int(input("Digite uma idade: "))
while idade >= 0:
    sexo = input("Digite o sexo (M/F): ")
    salario = float(input("Digite o salário: "))
    habitantes.append({"idade": idade, "sexo": sexo, "salario": salario})
    idade = int(input("Digite uma idade: "))
media_salarios = sum(habitante["salario"] for habitante in habitantes) / len(habitantes)
maior_idade = max(habitante["idade"] for habitante in habitantes)
menor_idade = min(habitante["idade"] for habitante in habitantes)
menor_salario = min(habitante["salario"] for habitante in habitantes)
for habitante in habitantes:
    if habitante["salario"] == menor_salario:
        idade_sexo_menor_salario = (habitante["idade"], habitante["sexo"])
mulheres_salario_200 = len([habitante for habitante in habitantes if habitante["sexo"] == "F" and habitante["salario"] <= 200])
print(f"Média dos salários do grupo: {media_salarios}")
print(f"Maior idade do grupo: {maior_idade}")
print(f"Menor idade do grupo: {menor_idade}")
print(f"Idade e sexo da pessoa que possui o menor salário: {idade_sexo_menor_salario}")
print(f"Quantidade de mulheres com salário até R$ 200,00: {mulheres_salario_200}")
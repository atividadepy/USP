habitantes = []
salario = float(input("Digite um salário: "))
while salario >= 0:
    filhos = int(input("Digite o número de filhos: "))
    habitantes.append({"salario": salario, "filhos": filhos})
    salario = float(input("Digite um salário: "))
media_salario = sum(habitante["salario"] for habitante in habitantes) / len(habitantes)
media_filhos = sum(habitante["filhos"] for habitante in habitantes) / len(habitantes)
maior_salario = max(habitante["salario"] for habitante in habitantes)
percentagem_salario_150 = len([habitante for habitante in habitantes if habitante["salario"] <= 150]) / len(habitantes) * 100
print(f"Média do salário da população: {media_salario}")
print(f"Média do número de filhos: {media_filhos}")
print(f"Maior salário: {maior_salario}")
print(f"Percentagem de pessoas com salários até R$ 150,00: {percentagem_salario_150}%")
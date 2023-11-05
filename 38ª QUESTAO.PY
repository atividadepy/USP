def calcular_salario(salario):
    if salario <= 350:
        return salario * 1.15
    elif salario <= 600:
        return salario * 1.10
    else:
        return salario

def calcular_ferias(salario):
    return salario * 1.33

def calcular_decimo_terceiro(salario, meses):
    return salario * meses / 12

def menu():
    while True:
        print("Menu de opções:")
        print("1. Novo salário")
        print("2. Férias")
        print("3. Décimo terceiro")
        print("4. Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 4:
            break
        salario = float(input("Digite o salário do funcionário: "))
        if opcao == 1:
            print("Novo salário: ", calcular_salario(salario))
        elif opcao == 2:
            print("Valor das férias: ", calcular_ferias(salario))
        elif opcao == 3:
            meses = int(input("Digite o número de meses de trabalho na empresa (no máximo 12): "))
            print("Valor do décimo terceiro: ", calcular_decimo_terceiro(salario, meses))
        else:
            print("Opção inválida. Tente novamente.")

menu()
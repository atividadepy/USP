def calculadora():
    while True:
        print("Menu de opções:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 5:
            break
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if opcao == 1:
            print("Resultado: ", num1 + num2)
        elif opcao == 2:
            print("Resultado: ", num1 - num2)
        elif opcao == 3:
            print("Resultado: ", num1 * num2)
        elif opcao == 4:
            if num2 != 0:
                print("Resultado: ", num1 / num2)
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Tente novamente.")

calculadora()
def calculadora():
    while True:
        print("Menu de opções:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 5:
            break
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if opcao == 1:
            print("Resultado: ", num1 + num2)
        elif opcao == 2:
            print("Resultado: ", num1 - num2)
        elif opcao == 3:
            print("Resultado: ", num1 * num2)
        elif opcao == 4:
            if num2 != 0:
                print("Resultado: ", num1 / num2)
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Tente novamente.")

calculadora()
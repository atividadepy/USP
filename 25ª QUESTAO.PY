def calcular_dados_alunos(dados):
    notas_finais = []
    total_reprovados = 0
    reprovados_frequencia = 0
    total_alunos = len(dados)

    for aluno in dados:
        matricula, nota1, nota2, nota3, frequencia = aluno
        nota_final = (nota1 + nota2 + nota3) / 3
        notas_finais.append(nota_final)

        if nota_final < 6 or frequencia < 40:
            total_reprovados += 1
            if frequencia < 40:
                reprovados_frequencia += 1

        if nota_final >= 6 and frequencia >= 40:
            mensagem = "Aprovado"
        else:
            mensagem = "Reprovado"

        print(f"Aluno {matricula}: Nota final {nota_final:.2f}, {mensagem}.")

    maior_nota = max(notas_finais)
    menor_nota = min(notas_finais)

    print(f"A maior nota da turma é {maior_nota:.2f}.")
    print(f"A menor nota da turma é {menor_nota:.2f}.")
    print(f"O total de alunos reprovados é {total_reprovados}.")
    if total_alunos > 0:
        percentual_reprovados_frequencia = (reprovados_frequencia / total_alunos) * 100
        print(f"A percentagem de alunos reprovados por frequência abaixo da mínima é {percentual_reprovados_frequencia:.2f}%.")

dados = []
for i in range(10):
    matricula = int(input(f"Digite o número da matrícula do {i+1}º aluno: "))
    nota1 = float(input(f"Digite a primeira nota do {i+1}º aluno: "))
    nota2 = float(input(f"Digite a segunda nota do {i+1}º aluno: "))
    nota3 = float(input(f"Digite a terceira nota do {i+1}º aluno: "))
    frequencia = int(input(f"Digite a frequência do {i+1}º aluno (número de aulas frequentadas): "))
    dados.append((matricula, nota1, nota2, nota3, frequencia))

calcular_dados_alunos(dados)

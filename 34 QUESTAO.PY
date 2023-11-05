votos = [0, 0, 0, 0, 0, 0]  # índices 0-3 para candidatos, 4 para nulos, 5 para brancos

while True:
    voto = int(input("Digite o código do voto (0 para finalizar): "))
    if voto == 0:
        break
    elif 1 <= voto <= 4:
        votos[voto - 1] += 1
    elif voto == 5:
        votos[4] += 1
    elif voto == 6:
        votos[5] += 1

total_votos = sum(votos)
percentual_nulos = votos[4] / total_votos * 100
percentual_brancos = votos[5] / total_votos * 100

print("Total de votos para cada candidato: ", votos[0:4])
print("Total de votos nulos: ", votos[4])
print("Total de votos em branco: ", votos[5])
print("Percentagem de votos nulos sobre o total de votos: ", percentual_nulos)
print("Percentagem de votos em branco sobre o total de votos: ", percentual_brancos)
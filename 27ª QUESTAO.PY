audiencia = {}
canal = int(input("Digite o número do canal: "))
while canal != 0:
    pessoas = int(input("Digite o número de pessoas assistindo: "))
    if canal in audiencia:
        audiencia[canal] += pessoas
    else:
        audiencia[canal] = pessoas
    canal = int(input("Digite o número do canal: "))
total_pessoas = sum(audiencia.values())
for canal, pessoas in audiencia.items():
    percentagem = (pessoas / total_pessoas) * 100
    print(f"Canal {canal}: {percentagem}% de audiência")
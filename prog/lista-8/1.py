nota = float(input("Digite a nota: "))
faltas = int(input("Digite a quantidade de faltas: "))

if nota >= 7 and faltas < 14:
    print("Aprovado")
else:
    print("Reprovado")
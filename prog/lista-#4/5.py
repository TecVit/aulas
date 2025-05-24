n1 = int(input("Primeira Nota: "))
p1 = int(input("Peso da Primeira Nota: "))

n2 = int(input("Segunda Nota: "))
p2 = int(input("Peso da Segunda Nota: "))

n3 = int(input("Terceira Nota: "))
p3 = int(input("Peso da Terceira Nota: "))

n4 = int(input("Quarta Nota: "))
p4 = int(input("Peso da Quarta Nota: "))

media_ponderada = (n1*p1 + n2*p2 + n3*p3+ n4*p4) / (p1 + p2 + p3+p4)

print(f"Média Ponderada: {media_ponderada}")
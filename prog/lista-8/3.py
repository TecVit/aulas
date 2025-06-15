x1 = int(input("Valor de x1: "))
x2 = int(input("Valor de x2: "))

y1 = int(input("Valor de y1: "))
y2 = int(input("Valor de y2: "))

d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)

if d > 10:
    print(f"A distancia dos dois pontos é de {d}. Longe")
else:
    print(f"A distancia dos dois pontos é de {d}. Perto")
n1 = int(input("1º Número: "))
n2 = int(input("2º Número: "))

op = int(input("Escolha uma opção (1 a 3): "))

if op == 1:
    soma = n1 + n2
    print(f"Soma dos números: {soma}")
if op == 2:
    subtracao = n1 - n2
    print(f"Subtração dos números: {subtracao}")
if op == 3:
    multiplicacao = n1 * n2
    print(f"Multiplicação dos números: {multiplicacao}")

if op < 1 or op > 3:
    print("Opção Inválida")
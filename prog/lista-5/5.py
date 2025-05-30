n1 = int(input("1º Número: "))
n2 = int(input("2º Número: "))
n3 = int(input("3º Número: "))
n4 = int(input("4º Número: "))

qtd_pares = 0
qtd_impares = 0

if n1 % 2 == 0:
    qtd_pares += 1
if n2 % 2 == 0:
    qtd_pares += 1
if n3 % 2 == 0:
    qtd_pares += 1
if n4 % 2 == 0:
    qtd_pares += 1

if not n1 % 2 == 0:
    qtd_impares += 1
if not n2 % 2 == 0:
    qtd_impares += 1
if not n3 % 2 == 0:
    qtd_impares += 1
if not n4 % 2 == 0:
    qtd_impares += 1

print(f"Quantidade de números Ímpares: {qtd_impares}")
print(f"Quantidade de números Pares: {qtd_pares}")
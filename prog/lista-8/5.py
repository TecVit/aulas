n = int(input("Digite um número: "))

if n % 2 == 0:
    dobro = n * 2
    print(f"O número {n} é par")
    print(f"O dobro de {n} é {dobro}")
else:
    triplo = n * 3
    print(f"O número {n} é ímpar")
    print(f"O triplo de {n} é {triplo}")
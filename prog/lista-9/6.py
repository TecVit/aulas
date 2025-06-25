n1 = int(input("Digite o valor do 1º Número: "))
n2 = int(input("Digite o valor do 2º Número: "))
n3 = int(input("Digite o valor do 3º Número: "))

if n1 > 0 and n2 > 0 and n3 > 0:
    soma = n1 + n2 + n3
    print(f"A soma dos números é {soma}")

elif n1 < 0 and n2 < 0 and n3 < 0:
    soma = n1 + n2 + n3
    contrario = soma * (-1)
    print(f"O contrário da soma dos números é {contrario}")

elif (n1 > 0 and n2 < 0 and n3 < 0) or (n1 < 0 and n2 > 0 and n3 < 0) or (n1 < 0 and n2 < 0 and n3 > 0):
    print(f"Os números pares são: ", end="")
    if n1 % 2 == 0:
        print(n1, end=" ")
    if n2 % 2 == 0:
        print(n2, end=" ")
    if n3 % 2 == 0:
        print(n3, end=" ")

elif (n1 > 0 and n2 > 0 and n3 < 0) or (n1 < 0 and n2 > 0 and n3 > 0) or (n1 > 0 and n2 < 0 and n3 > 0):
    soma = 0

    if n1 > 0:
        soma = soma + n1
    if n2 > 0:
        soma = soma + n2
    if n3 > 0:
        soma = soma + n3
    
    par = False

    if soma % 2 == 0:
        par = True

    print(f"A soma dos números positivos é {soma}, {"Par" if par else "Impar"}")
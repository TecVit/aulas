n = int(input("Digite um número inteiro: "))

if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:
    print("O número é divisível por 2, 3 e 5.")

elif n % 2 == 0 and n % 3 == 0:
    print("O número é divisível por 2 e 3.")

elif n % 3 == 0 and n % 5 == 0:
    print("O número é divisível por 3 e 5.")

elif n % 2 == 0 and n % 5 == 0:
    print("O número é divisível por 2 e 5.")

elif n % 2 == 0:
    print("O número é divisível por 2.")

elif n % 3 == 0:
    print("O número é divisível por 3.")

elif n % 5 == 0:
    print("O número é divisível por 5.")

else:
    print("O número não é divisível por 2, 3 ou 5.")
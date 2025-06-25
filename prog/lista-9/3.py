l1 = int(input("Digite o 1º lado: "))
l2 = int(input("Digite o 2º lado: "))
l3 = int(input("Digite o 3º lado: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    # Já q não temos base e altura
    # Utilizamos a Fórmula de Herão :)
    s = (l1 + l2 + l3) / 2
    a = ((s * (s - l1)) *  (s - l2) * (s - l3)) ** (1 / 2)
    
    if l1 == l2 and l2 == l3:
        print(f"Triângulo Equilátero")
    elif l1 == l2 and l3 != l2:
        print(f"Triângulo Isósceles")
    elif l1 != l2 and l1 != l3:
        print(f"Triângulo Escaleno")
    
    print(f"A área do triângulo é de aproximadamente: {a}u²")
else:
    print("Os lados não formam um triângulo")
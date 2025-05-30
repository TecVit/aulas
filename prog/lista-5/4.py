valor = int(input("Digite o valor do m²: R$"))

formato = int(input('''
Opções de Formatos:\n
(1) Terreno quadrado
(2) Terreno retangular
(3) Terreno triangular\n
Digite o número do formato do terreno? '''))

base = int(input("\nDigite a base (m): "))
altura = int(input("Digite a altura (m): "))

if formato == 1:
    area = base ** 2
    pagar = area * valor
    print(f"\nÁrea: {area}m²")
    print(f"Valor a ser pago: R${pagar}")

if formato == 2:
    area = base * altura
    pagar = area * valor
    print(f"\nÁrea: {area}m²")
    print(f"Valor a ser pago: R${pagar}")

if formato == 3:
    area = (base * altura) / 2
    pagar = area * valor
    print(f"\nÁrea: {area}m²")
    print(f"Valor a ser pago: R${pagar}")
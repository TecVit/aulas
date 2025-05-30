s = str(input("Digite a letra (m) para masculino e (f) para feminino: "))
a = float(input("Digite sua altura: "))

if s == 'm':
    print(f"Seu peso ideal é de {((72.7 * a) - 58)}")

if s == 'f':
    print(f"Seu peso ideal é de {((62.1 * a) - 44.7)}")

if s != 'm' and s != 'f':
    print('Comando inválido')
nota = float(input("Digite uma nota de 0 a 10: "))
conceito = ''

if nota >= 9:
    conceito = 'A'
if nota >= 8:
    conceito = 'B'
if nota >= 7:
    conceito = 'C'
if nota >= 6:
    conceito = 'D'
else:
    conceito = 'F'

print(f"O conceito correspondente é {conceito}")
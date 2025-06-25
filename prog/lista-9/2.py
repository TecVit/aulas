a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

menor = ''
pivo = ''
maior = ''

if a > b and a > c:
    maior = "A"
elif b > a and b > c:
    maior = "B"
elif c > b and c > a:
    maior = "C"

if a > b and a < c or a > c and a < b:
    pivo = "A"
elif b > a and b < c or b > c and b < a:
    pivo = "B"
elif c > b and c < a or c > a and c < b:
    pivo = "C"

if a < b and a < c:
    menor = "A"
elif b < a and b < c:
    menor = "B"
elif c < b and c < a:
    menor = "C"

print(f"{menor}, {pivo}, {maior}")
def maiorNumero(a, b, c):
  maior = a
  if b > maior:
    maior = b
  if c > maior:
    maior = c
  return maior

a = int(input())
b = int(input())
c = int(input())

maior = maiorNumero(a, b, c)
print(f"O maior número é: {maior}")
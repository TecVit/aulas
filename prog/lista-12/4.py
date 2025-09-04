n = int(input('Digite a quantidade de números: '))
s, c = 0, 0

while c < n:
  x = int(input('Digite um número: '))
  s += x
  c += 1

print('A soma é:', s)
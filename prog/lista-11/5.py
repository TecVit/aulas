def media_notas(n1, n2, n3):
  return (n1 + n2 + n3) / 3

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

media = media_notas(n1, n2, n3)
print(f"A média final é: {media:.2f}")
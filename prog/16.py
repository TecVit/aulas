n = int(input())

centena = n // 100
dezena = (n - centena * 100) // 10
unidade = ((n - centena * 100) - (dezena * 10)) // 1

print(centena)
print(dezena)
print(unidade)

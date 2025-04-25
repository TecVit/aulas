x = int(input("Quantidade de balas: "))

distribuidas = x // 3
resto = x % 3

print(f"Cada amigo receberá {distribuidas} bala")
print(f"Haverá {resto} bala não distribuída")
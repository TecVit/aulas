eleitores = int(input("Quantidade de Eleitores: "))
validos = int(input("Válidos: "))
brancos = int(input("Brancos: "))
nulos = int(input("Nulos: "))

porcent_validos = (validos / eleitores) * 100
porcent_brancos = (brancos / eleitores) * 100
porcent_nulos = (nulos / eleitores) * 100

print(f"Válidos: {porcent_validos}%")
print(f"Brancos: {porcent_brancos}%")
print(f"Nulos: {porcent_nulos}%")
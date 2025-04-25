segundos = int(input("Segundos: "))

horas = segundos // 3600
minutos = (segundos - (horas * 3600)) // 60
segundos_restantes = segundos - ((horas * 3600) + (minutos * 60))

print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos_restantes}")
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

# 1 Hora tem 3600 Segundos
# 1 Minuto tem 60 Segundos
# 1 Segundo tem 1 Segundo

total = (horas * 3600) + (minutos * 60) + segundos

print(f"Total em segundos é {total}s")
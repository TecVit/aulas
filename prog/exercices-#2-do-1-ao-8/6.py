horas_normais = int(input("Quantidade de horas normais: ")) # 40
valor_normal = int(input("Valor da hora normal: ")) # 20

valor_extra = int(input("Quantidade de hora extra: ")) # 30
horas_extras = int(input("Valor da hora extra: ")) # 10

salario_base = (horas_normais * valor_normal) + (horas_extras * valor_extra) # (40 x 20) + (30 x 10) = 1.100 Reais
bonus = salario_base * (10 / 100)

salario_total = salario_base + bonus

print(f"O salário total é de R${salario_total:.2f}")
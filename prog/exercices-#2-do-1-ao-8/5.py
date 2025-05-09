horas = int(input("Horas Trabalhadas: ")) # ex: 40 Horas
valor = int(input("Valor da Hora: R$")) # ex: 25 Reais

salario_base = horas * valor # 4.000 Reais
gratificacao = salario_base * (5 / 100) # 200 Reais

salario_total = salario_base + gratificacao # 4.200 Reais

inss = salario_total * (8 / 100) # 336 Reais

salario_liquido = salario_total - inss # 4.200 - 336 = 3864 Reais

print(f"Salário Líquido é de R${salario_liquido}")
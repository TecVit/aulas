salario_atual = int(input("Salário Atual: R$"))
porcentagem_aumento = int(input("Porcentagem de Aumento: "))

salario_final = salario_atual * (1 + (porcentagem_aumento / 100))

print(f"O Salário final é de R${salario_final}")
nome = str(input())
tempo = int(input())
salario = float(input())

print(f"O novo salário de {nome} é R$", end="")
porcentagem_aumento = 1

if tempo >= 9:
    porcentagem_aumento = 1 + (10 / 100)
elif tempo >= 6:
    porcentagem_aumento = 1 + (5 / 100)
elif tempo > 2:
    porcentagem_aumento = 1 + (4 / 100)
else:
    porcentagem_aumento = 1 + (2 / 100)

novo_salario = salario * porcentagem_aumento
print(novo_salario)
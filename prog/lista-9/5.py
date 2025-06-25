nome = str(input())
idade = int(input())
salario = float(input())

print(f"O novo salário de {nome} é R$", end="")
porcentagem_aumento = 1

if idade >= 50:
    porcentagem_aumento = 1 + (21 / 100)
elif idade >= 38:
    porcentagem_aumento = 1 + (18 / 100)
elif idade >= 26:
    porcentagem_aumento = 1 + (15 / 100)
elif idade >= 18:
    porcentagem_aumento = 1 + (12 / 100)

novo_salario = salario * porcentagem_aumento
print(novo_salario)
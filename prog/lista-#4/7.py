custo = int(input("Preço de Custo: R$"))
venda = int(input("Preço de Venda: R$"))

lucro = venda - custo
porcent_lucro = (lucro / custo) * 100

print(f"Lucro total de R${lucro}")
print(f"Porcentagem do Lucro é {porcent_lucro}%")
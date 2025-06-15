salario = float(input("Salário: R$"))
imposto = 1 / 100

if salario <= 2112:
    imposto *= 0
if salario > 2112 and salario <= 2826.65:
    imposto *= 7.5
if salario > 2826.65 and salario <= 3751.05:
    imposto *= 15
if salario > 3751.05 and salario <= 4664.68:
    imposto *= 22.5
if salario > 4664.68:
    imposto *= 27.5

print(f"Imposto: R${salario * imposto}")
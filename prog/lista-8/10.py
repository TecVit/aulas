valor = float(input("Valor principal: R$"))
juros = int(input("Valor do juros ao mês (0 a 100): "))
tempo = int(input("Tempo (mês): "))

juros_finais = valor * (juros / 100) * tempo
total = valor + juros_finais

if total > 1000:
    print("Alerta: valor alto!")

print(f"O valor de juros a ser pago é de R${juros_finais}")
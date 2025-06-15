conta = float(input("Digite o valor da conta: R$"))
nivel = int(input("Digite o nível de serviço (1 a 3): "))
porcentagem_da_gorjeta = 1 / 100

if nivel == 1:
    porcentagem_da_gorjeta *= 5
if nivel == 2:
    porcentagem_da_gorjeta *= 10
if nivel == 3:
    porcentagem_da_gorjeta *= 15

gorjeta = (conta * porcentagem_da_gorjeta)
total_a_pagar = conta + gorjeta

print(f"Valor da gorjeta: R${gorjeta}")
print(f"Total a pagar: R${total_a_pagar}")
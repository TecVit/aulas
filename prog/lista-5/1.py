p1 = int(input("Preço do Produto 1: R$"))
qtd1 = int(input("Quantidade comprada do Produto 1: "))

p2 = int(input("Preço do Produto 2: R$"))
qtd2 = int(input("Quantidade comprada do Produto 2: "))

p3 = int(input("Preço do Produto 3: R$"))
qtd3 = int(input("Quantidade comprada do Produto 3: "))

p4 = int(input("Preço do Produto 4: R$"))
qtd4 = int(input("Quantidade comprada do Produto 4: "))

p5 = int(input("Preço do Produto 5: R$"))
qtd5 = int(input("Quantidade comprada do Produto 5: "))

valor_a_ser_pago = (p1 * qtd1) + (p2 * qtd2) + (p3 * qtd3) + (p4 * qtd4) + (p5 * qtd5)

print(f"\n=====> Preço total da compra: R${valor_a_ser_pago} <=====")

forma_de_pagamento = int(input('''
Digite o número da forma de pagamento??\n
(1) À vista (desconto de 10%)\n
(2) Em duas vezes (valor normal)\n
(3) Em três vezes (acréscimo de 10%)\n
(4) Em quatro vezes (acréscimo de 20%)\n

Número: '''))

if forma_de_pagamento == 1:
    desconto = valor_a_ser_pago * (10 / 100)
    valor_final = valor_a_ser_pago - desconto
    print(f'\nO valor total a ser pago é de R${valor_final}')

if forma_de_pagamento == 2:
    print(f'\nO valor total a ser pago é de R${valor_a_ser_pago}')

if forma_de_pagamento == 3:
    acrescimo = valor_a_ser_pago * (10 / 100)
    valor_final = valor_a_ser_pago + acrescimo
    print(f'\nO valor total a ser pago é de R${valor_final}')

if forma_de_pagamento == 4:
    acrescimo = valor_a_ser_pago * (20 / 100)
    valor_final = valor_a_ser_pago + acrescimo
    print(f'\nO valor total a ser pago é de R${valor_final}')
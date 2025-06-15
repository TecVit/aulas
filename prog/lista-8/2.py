preco = float(input("Digite o preço do produto: R$"))
quantidae = int(input("Digite a quantidade: "))

total = preco * quantidae

if quantidae > 10:
    desconto = total * (10 / 100)
    total = total - desconto
if quantidae >= 5 and quantidae <= 10:
    desconto = total * (5 / 100)
    total = total - desconto
else:
    desconto = 0
    total = total - desconto

print(f"O valor final da compra é R${total}")
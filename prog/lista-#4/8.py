preco = int(input("Preço do Produto: R$"))

imposto = preco * 0.17
lucro = preco * 0.25

preco_final = preco + imposto + lucro

print(f"Preço final do produto: R${preco_final}")
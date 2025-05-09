lapiseiras = int(input("Quantidade de lapiseiras: "))
borrachas = int(input("Quantidade de borrachas: "))

valor_lapiseira = int(input("Valor da lapiseira: "))
valor_borracha = int(input("Valor da borracha: "))

total_base = (lapiseiras * valor_lapiseira) + (borrachas * valor_borracha)
doacao = total_base * (5 / 100)

total_liquido = total_base - doacao

print(f"Salário liquido: {total_liquido}")
lapiseiras = int(input("Quantidade de lapiseiras: "))
borrachas = int(input("Quantidade de borrachas: "))

valor_lapiseira = 2.5
valor_borracha = 0.75

total_base = (lapiseiras * valor_lapiseira) + (borrachas * valor_borracha)
doacao = total_base * (5 / 100)

total_liquido = total_base - doacao

print(f"Salário liquido: {total_liquido}")
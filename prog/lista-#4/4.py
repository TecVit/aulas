reais = int(input("R$"))

n100 = reais // 100
reais = reais % 100

n50 = reais // 50
reais = reais % 50

n20 = reais // 20
reais = reais % 20

n10 = reais // 10
reais = reais % 10

n5 = reais // 5
reais = reais % 5

n2 = reais // 2
reais = reais % 2

print(f"{n100} Nota(s) de 100 Reais")
print(f"{n50} Nota(s) de 50 Reais")
print(f"{n20} Nota(s) de 20 Reais")
print(f"{n10} Nota(s) de 10 Reais")
print(f"{n5} Nota(s) de 5 Reais")
print(f"{n2} Nota(s) de 2 Reais")
print(f"{reais} Moeda(s) de 1 Real")
tr = float(input("Nota do Trabalho de laboratório: "))
av = float(input("Nota do Avaliação Semestral: "))
ex = float(input("Nota do Exame Final: "))

p_tr = 2
p_av = 3
p_ex = 5

mp = ((tr * p_tr) + (av * p_av)  + (ex * p_ex)) / (p_tr + p_av + p_ex)
print(f"Média Final: {mp}")

if mp >= 6:
    print("Aprovado")
if 4 <= mp < 6:
    print("Recuperação")
if 0 <= mp < 4:
    print("Reprovado")
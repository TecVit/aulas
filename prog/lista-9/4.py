nome = str(input())
idade = int(input())

print(f"A faixa etária de {nome} é classificada como: ", end="")

if idade >= 60:
    print("Terceira Idade")
elif idade >= 19:
    print("Adulto")
elif idade >= 13:
    print("Adolescente")
elif idade >= 0:
    print("Criança")
else:
    print("Idade inválida")
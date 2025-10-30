def main():
    n = int(input())
    lista = []

    for i in range(n):
        lista.append(int(input(f"Digite o {i+1}º número: ")))
    
    alvo = int(input("Digite o número alvo: "))

    achou = False
    for i in range(n - 1):
        x, y = lista[i], lista[i+1]
        if (x * y) == alvo:
            print(f"Os números {x} e {y} quanto multiplicados resultam em {alvo}")
            achou = True
            break
    
    if not achou:
        print(f"Não existe dois números distintos que multiplicados resultam em {alvo}")

    return 0

main()
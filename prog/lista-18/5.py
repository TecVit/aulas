def main():
    l1, l2 = [], []

    print(f"===> 1º Lista <===")
    for i in range(1, 5 + 1):
        l1.append(int(input(f"Digite o {i}º número da lista: ")))
    
    print(f"\n===> 2º Lista <===")
    for i in range(1, 5 + 1):
        l2.append(int(input(f"Digite o {i}º número da lista: ")))

    resposta = []
    
    for i in range(5):
        if l1[i] in l2:
            resposta.append(l1[i])
    
    print(f"Os elementos que existem nas duas listas são: {resposta}")

    return 0

main()
def main():
    a, b = [], []
    n = int(input("Digite o tamanho das listas: "))

    print(f"===> 1º Lista <===")
    for i in range(1, n + 1):
        a.append(int(input(f"Digite o {i}º número da lista: ")))
    
    print(f"\n===> 2º Lista <===")
    for i in range(1, n + 1):
        b.append(int(input(f"Digite o {i}º número da lista: ")))

    c = []
    
    c.extend(a)
    c.extend(b)

    c.sort()
    
    print(f"\nOs elementos da lista C são: {c}")

    return 0

main()
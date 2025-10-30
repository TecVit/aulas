def main():
    a = 1
    b = 50
    lista = []

    for i in range(a, b + 1):
        if i % 3 == 0:
            lista.append(i)
            i += 3

    print(f"A lista dos múltiplos de 3 é: {lista}")

    return 0

main()
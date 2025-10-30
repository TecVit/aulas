def main():
    lista = []

    i = 1
    print(f"Digite '0' para cancelar")
    while True:
        numero = int(input(f"Digite o {i}º número: "))
        if numero == 0:
            break

        lista.append(numero)
        i += 1

    lista_inversa = [lista[i] for i in range(len(lista) - 1, -1, -1)]

    print(f"A lista na ordem inversa é {lista_inversa}")

    return 0

main()
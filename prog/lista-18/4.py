def main():
    numeros = []

    i = 1

    while True:
        numero = int(input(f"Digite o {i}º número: "))
        if numero == 0:
            break
            
        numeros.append(numero)
        i += 1
    
    print(f"Os números são {numeros}")
    numeros_inversos = [numeros[i] for i in range(len(numeros) - 1, -1, -1)]
    
    print(f"Os números na ordem inversa são {numeros_inversos}")

    print(f"Valores inversos: ", end="")
    for i in range(len(numeros) - 1, -1, -1):
        if i - 1 == -1:
            print(numeros[i])
        else:
            print(numeros[i], end=" ")

    return 0

main()
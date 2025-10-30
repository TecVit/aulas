def main():
    lista = []

    for i in range(1, 5 + 1):
        lista.append(int(input(f"Digite o {i}º número: ")))

    busca = int(input(f"Digite o número de busca: "))
    resposta = lista.index(busca)
    
    if resposta == -1:
        print(f"Não foi possível encontrar esse número")
    else:
        print(f"O número existe e esta na posição {resposta} (de 0 a 4)")
    
    return 0

main()
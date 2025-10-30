def ordenarLista(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]
    menor = [num for num in lista[1:] if num <= pivo]
    maior = [num for num in lista[1:] if num > pivo]
    
    return ordenarLista(menor) + [pivo] + ordenarLista(maior)

def remove_repetidos(lista):
    nova_lista = []

    for i in range(len(lista)):
        elemento = lista[i]
        if elemento not in nova_lista:
            nova_lista.append(elemento)

    return ordenarLista(nova_lista)

def main():
    lista = [2, 4, 2, 2, 3, 3, 1]
    nova_lista = remove_repetidos(lista)

    print(f"A lista sem elementos repetidos é: {nova_lista}")

    return 0

main()
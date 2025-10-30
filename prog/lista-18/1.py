def tamanho(lista):
    count = 0

    for numero in lista:
        count += 1

    return count

def maior(lista):
    maior = 0
    
    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

def menor(lista):
    menor = 10 ** 8
    
    for numero in lista:
        if numero < menor:
            menor = numero

    return menor

def soma(lista):
    soma = 0

    for i in range(tamanho(lista)):
        soma += lista[i]
        
    return soma

def ordenarLista(lista, tipo):
    # Tipo = 1 | Crescente 
    # Tipo = 2 | Decrescente

    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]
    menor = [num for num in lista[1:] if num <= pivo]
    maior = [num for num in lista[1:] if num > pivo]
    
    if tipo == 1:
        return ordenarLista(menor, tipo) + [pivo] + ordenarLista(maior, tipo)
    elif tipo == 2:
        return ordenarLista(maior, tipo) + [pivo] + ordenarLista(menor, tipo)
    
def main():
    lista = [5, 7, 2, 9, 4, 1, 3]

    print(f"Tamanho da lista: {tamanho(lista)}")
    print(f"Maior número da lista: {maior(lista)}")
    print(f"Menor número da lista: {menor(lista)}")
    print(f"Soma dos números da lista: {soma(lista)}")

    print(f"Lista em ordem crescente: {ordenarLista(lista, 1)}")
    print(f"Lista em ordem decrescente: {ordenarLista(lista, 2)}")
    
    return 0

main()
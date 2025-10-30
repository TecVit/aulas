def temperaturaDoDia(temperaturas, dia):
    return temperaturas[dia - 1]

def maiorTemperatura(temperaturas):
    maior = 0
    
    for numero in temperaturas:
        if numero > maior:
            maior = numero

    return maior

def menorTemperatura(temperaturas):
    menor = 10 ** 8
    
    for numero in temperaturas:
        if numero < menor:
            menor = numero

    return menor

def somaDasTemperaturas(temperaturas):
    soma = 0

    for i in range(len(temperaturas)):
        soma += temperaturas[i]

    return soma

def main():
    temperaturas = [20, 30, 28, 17, 23, 10, 11, 8, 39, 30]
    soma = somaDasTemperaturas(temperaturas)
    dias = len(temperaturas)
    media = soma / dias

    print(f"O primeiro dia teve {temperaturaDoDia(temperaturas, 1)} °C de temperatura°")
    print(f"O último dia teve {temperaturaDoDia(temperaturas, 10)} °C de temperatura")
    print(f"O {temperaturas.index(maiorTemperatura(temperaturas)) + 1}º dia foi o mais quente de todos com {maiorTemperatura(temperaturas)} °C")
    print(f"O {temperaturas.index(menorTemperatura(temperaturas)) + 1}º dia foi o mais frio de todos com {menorTemperatura(temperaturas)} °C")
    print(f"A média das temperaturas foi de {media}°C")

    return 0

main()
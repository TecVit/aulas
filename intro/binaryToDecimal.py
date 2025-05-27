# Palavra BYTE

# Exercício do Slide

B = "0100 0010" # Em Decimal 66
Y = "0101 1001" # Em Decimal 89
T = "0101 0100" # Em Decimal 84
E = "0100 0101" # Em Decimal 69

# Soma da palavra BYTE é 308

# Função que transforma um número Binário em Decimal
def binaryToDecimal(number):
    # Tiramos qualquer espaço em branco
    number = str(number).replace(" ", "")
    
    # Transformamos em uma lista de números para facilitar a leitura
    # de trás para frente
    number = [int(n) for n in number]
    
    # Armazena a soma (decimal) do número binário
    soma = 0

    # Armazena o Expoente
    expo = 0

    # Percorrer os números da direita para esquerda
    for i in range(len(number) - 1, -1, -1):
        # Adicionamos a soma
        # Soma += (1 ou 0) x (2 ** x); (x ∈ N; 0 >= x <= 7)
        soma += number[i] * (2 ** expo)

        # Adicionamos 1 ao expoente para continuar a iteração
        expo += 1

    # Retornamos a soma (Decimal) do número    
    return soma

    
# Essa parte do código existe para testar nossa funcionalidade
while True:
    # Pergunta um número
    n = str(input("Digite um número binário: "))
    
    # Mostra o resultado em Binário
    print(binaryToDecimal(n))
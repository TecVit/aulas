# Palavra BYTE

# Binário
B = "0100 0010" # 66
Y = "0101 1001" # 89
T = "0101 0100" # 84
E = "0100 0101" # 69

# Soma da palavra BYTE é 308

# Função que transforma um número Binário em Decimal
def binaryToDecimal(number):
    number = str(number).replace(" ", "")
    number = [int(n) for n in number]
    
    s = 0
    expo = 0
    for i in range(len(number) - 1, -1, -1):
        s += number[i] * (2 ** expo)
        expo += 1
    
    return s
    
# Essa parte do código existe para testar nossa funcionalidade
while True:
    # Pergunta um número
    n = str(input("Digite um número binário: "))
    
    # Mostra o resultado em Binário
    print(binaryToDecimal(n))
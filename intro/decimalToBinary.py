# Função que transforma um número Decimal em Binário
def decimalToBinary(number):
    
    # Restos das divisões por 2
    restos = ""
    
    # Dividir o número por 2 até ele ser menor ou igual a 0 (Zero)
    while number > 0:
        
        # Resto da divisão por 2
        resto = number % 2
        
        # Vamos atualizar o número sendo o resultado da divisão inteira
        number = number // 2
        
        # Adicionar o resto ao restos
        restos += str(resto)
    
    # Inverter a string de restos para obter o número binário
    # Pois a leitura do número binário é de direita para esquerda
    restos_invertido = restos[::-1]
    
    # Quantidade de zeros a esquerda (assumindo que teremos no máximo 8 dígitos "256 Bits")
    zeros = "0" * (8 - len(restos_invertido))
    
    # Adicionamos os zeros a esquerda
    resultado = str(zeros + restos_invertido)
    
    return resultado[:4] + " " + resultado[4:]

# Essa parte do código existe para testar nossa funcionalidade
while True:
    # Pergunta um número
    n = int(input("Digite um número decimal: "))
    
    # Mostra o resultado em Binário
    print(decimalToBinary(n))
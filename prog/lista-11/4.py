def par_ou_impar(numero):
  if numero % 2 == 0:
    return 0
  else:
    return 1
  
numero = int(input("Digite um número: "))
print("O número é par" if par_ou_impar(numero) == 0 else "O número é ímpar")
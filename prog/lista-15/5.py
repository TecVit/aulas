def main():
  n = int(input("Digite um valor entre 1 e 20: "))
  while n < 1 or n > 20:
    n = int(input("Digite novamente um valor ENTRE 1 e 20: "))
  
  soma = 0
  for i in range(n):
    x = int(input(f"Digite o {i+1}º Número: "))
    soma += x
  
  media = soma / n
  
  print(f"O somatório é {soma}")
  print(f"A média é {media}")

  return 0

main()
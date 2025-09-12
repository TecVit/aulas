def readNumber():
  number = int(input("Digite um número entre (1 e 5): "))
  if number < 1 or number > 5:
    return False
  return number

def main():
  number = False
  while not number:
    number = readNumber()
  
  print(f"O número escolhido é: {number}")

  return 0

main()
def isVogal(letter):
  if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
    return 1
  return 0

def main():
  while True:
    letter = str(input("Digite uma letra: ")).upper()

    if isVogal(letter) == 1:
      print(f"A vogal digitada é: {letter}")
    else:
      print(f"A consoante digitada é: {letter}")
      break
      
  return 0

main()
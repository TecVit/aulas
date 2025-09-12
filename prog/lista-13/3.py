def multiplicationTable(number):
  i = 0

  while i <= 10:
    multiplication = number * i
    print(f"{number} x {i} = {multiplication}")
    i += 1

  return

def main():
  number = int(input("Digite um número: "))
  multiplicationTable(number)
  
  return 0

main()
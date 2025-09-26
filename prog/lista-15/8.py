def main():
  percent_3 = 0
  percent_5 = 0
  
  for i in range(20):
    n = int(input(f"Digite o {i+1}º Número: "))

    if n % 3 == 0:
      percent_3 += 1
    elif n % 5 == 0:
      percent_5 += 1

  print(f"{(percent_3 / 20) * 100}% dos números são divisíveis por 3")
  print(f"{(percent_5 / 20) * 100}% dos números são divisíveis por 5")

  return 0

main()
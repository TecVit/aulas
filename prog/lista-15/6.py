def main():
  MIN = 1
  MAX = 100
  n = int(input(f"Digite um valor entre {MIN} e {MAX}: "))
  while n < MIN or n > MAX:
    n = int(input(f"Digite novamente um valor ENTRE {MIN} e {MAX}: "))
  
  for i in range(10 + 1):
    print(f"{n} x {i} = {n * i}")

  return 0

main()
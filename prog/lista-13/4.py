def multiplesOfSeven():
  i = 0
  c = 0
  r = 0

  while c < 10:
    i += 7
    c += 1
    r += i

  return r

def main():
  response = multiplesOfSeven()
  print(f"O soma dos 10 primeiros múltiplos de 7 é: {response}")

  return 0

main()
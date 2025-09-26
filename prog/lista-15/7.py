def main():

  for n in range(1, 10 + 1):
    print(f"| Tabuada do {n} |")
    for i in range(10 + 1):
      print(f"| {n:2} x {i:2} = {(n * i):3} |")
    print()

  return 0

main()
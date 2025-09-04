def menu_salgados():
  print("=== Menu de Salgados ===")
  print("1 - Coxinha")
  print("2 - Pastel")
  print("3 - Empada")
  print("4 - Quibe")

  return int(input("Escolha o código do salgado: "))

codigo = menu_salgados()
print(f"O código escolhido foi: {codigo}")
def media_notas(n1, n2, n3):
  return (n1 + n2 + n3) / 3

def resultado_final(n1, n2, n3, freq):
  media = media_notas(n1, n2, n3)

  print(f"Média do aluno: {media:.2f}")
  print(f"Frequência: {freq:.2f}%")

  return media >= 6.0 and freq >= 75
  
n1 = float(input("Primeira nota (0 a 10): "))
n2 = float(input("Segunda nota (0 a 10): "))
n3 = float(input("Terceira nota (0 a 10): "))

frequencia = float(input("Digite a frequência (0 a 100): "))

resultado = resultado_final(n1, n2, n3, frequencia)

if resultado:
  print("Situação: Aprovado ✅")
else:
  print("Situação: Reprovado ❌")
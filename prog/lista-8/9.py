peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc >= 30:
    print("Você está na faixa de obesidade")
if imc >= 25 and imc < 30:
    print("Você está na faixa de sobrepeso")
if imc >= 18.5 and imc < 25:
    print("Você está na faixa normal")
if imc < 18.5:
    print("Você está na faixa abaixo do peso")
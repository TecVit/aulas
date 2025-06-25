p1 = int(input("Digite a idade do 1º Participante: "))
p2 = int(input("Digite a idade do 2º Participante: "))
p3 = int(input("Digite a idade do 3º Participante: "))

print("O 1º Participante pertence a:")

if p1 > 15:
    print("Nenhuma categoria")
    
elif p1 >= 13:
    print("Categoria: Juvenil")

elif p1 >= 10:
    print("Categoria: Infantil 4")

elif p1 >= 7:
    print("Categoria: Infantil 3")


elif p1 >= 5:
    print("Categoria: Infantil 2")

else:
    print("Categoria: Infantil 1")

print("O 2º Participante pertence a:")

if p2 > 15:
    print("Nenhuma categoria")

elif p2 >= 13:
    print("Categoria: Juvenil")

elif p2 >= 10:
    print("Categoria: Infantil 4")

elif p2 >= 7:
    print("Categoria: Infantil 3")

elif p2 >= 5:
    print("Categoria: Infantil 2")

else:
    print("Categoria: Infantil 1")

print("O 3º Participante pertence a:")

if p3 > 15:
    print("Nenhuma categoria")

elif p3 >= 13:
    print("Categoria: Juvenil")

elif p3 >= 10:
    print("Categoria: Infantil 4")

elif p3 >= 7:
    print("Categoria: Infantil 3")

elif p3 >= 5:
    print("Categoria: Infantil 2")

else:
    print("Categoria: Infantil 1")
# Feito por Vitor Custodio da Silva

# (A) 25 base (10) para binário.
# 25 / 2 = 12, resto 1
# 12 / 2 = 6, resto 0
# 6 / 2 = 3, resto 0
# 3 / 2 = 1, resto 1
# 1 / 2 = 0, resto 1
# (A) Resposta: 11001
print(bin(25)[2:])

# (B) 156 base (10) para hexadecimal.
# 156 / 16 = 9 resto 12
# 12 = C
# Resposta: 9C
print(hex(156)[2:])

# (C) 1101 base (2) para decimal
# = (1 * 2³) + (1 * 2²) + (0 * 2¹) + (1 * 2⁰)
# = 8 + 4 + 0 + 1
# = 13
# Resposta: 13
print(int("1101", 2))

# (D) 2F base (16) para decimal
# = (2 * 16¹) + (F * 16⁰)
# = 32 + 15 = 47
# Resposta: 47
print(int("2F", 16))

# (E) 73 base (8) para decimal
# = (7 * 8¹) + (3 * 8⁰)
# = 56 + 3 = 59
# Resposta 59
print(int("73", 8))

# (F) 89 base (10) para octal
# Dividindo por 8:
# 89 / 8 = 11, resto 1
# 11 / 8 = 1, resto 3
# 1 / 8 = 0, resto 1
# Resposta: 131
print(oct(89)[2:])

# (G) 101101 base (2) para hexadecimal
# Agrupando de 4 em 4 bits (à direita): 0010 1101 = 2D
# Resposta: 2D
print(hex(int("101101", 2))[2:].upper())

# (H) 1A base (16) para binário
# 1A = (1 * 16¹) + (10 * 16⁰) = 26 decimal
# 26 --> binário = 11010
print(bin(int("1A", 16))[2:])

# (I) 45 base (8) para binário
# 45₈ = (4 * 8¹) + (5 * 8⁰) = 32 + 5 = 37
# 37 --> binário = 100101
print(bin(int("45", 8))[2:])

# (J) 100011 base (2) para octal
# Agrupando de 3 em 3 bits: 100 011 = 4 3
# Resposta: 43
print(oct(int("100011", 2))[2:])

# (K) 200 base (2) --> binário, hexadecimal e octal
# Explicação: 200 não pode ser base 2, já que os
# dígitos 0 e 1 são a representação da base de 2 dígitos
# então ter um número maior que 1, invalida o número
# Sem Resposta

# (L) 11111111 base (2) para decimal
# Por ser 8 dígitos (1), significa o maior número binário
# = 255
print(int("11111111", 2))  # Resposta: 255

# (M) FF base (16) para decimal
# = (15 * 16¹) + (15 * 16⁰) = 240 + 15 = 255
print(int("FF", 16))  # Resposta: 255

# (N) 64 base (10) para binário e hexadecimal
# 64 --> binário = 1000000
# 64 --> hexadecimal = 40
print(bin(64)[2:])
print(hex(64)[2:].upper())

# (O) 177 base (8) para binário
# 177 base (8) = (1 * 8²)+( 7 * 8¹)+  (7 * 8⁰) 
# = 64 + 56 + 7 = 127
print(bin(int("177", 8))[2:])
# 127 base (10) --> binário = 1111111
# print(bin(127)[2:])
# Resposta: 1111111

# (P) 10101010 base (2) para hexadecimal
# Agrupando: 1010 1010 = AA
print(hex(int("10101010", 2))[2:].upper())  # Resposta: AA

# (Q) 3C base (16) para octal
# 3C = (3*16 + 12) = 60 decimal
# 60 --> octal = 74
print(oct(int("3C", 16))[2:])  # Resposta: 74

# (R) 512 base (10) para binário
# 512 --> binário = 1000000000
print(bin(512)[2:])

# (S) 100 base (8) para decimal
# = (1 * 8²) = 64
print(int("100", 8))  # Resposta: 64

# (T) 111000 base (2) para hexadecimal e octal
# 111000 --> decimal = 56
# 56 --> hexadecimal = 38
# 56 --> octal = 70
print(hex(int("111000", 2))[2:].upper())  # hexadecimal
print(oct(int("111000", 2))[2:])  # octal
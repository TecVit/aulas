# Numero de robos por equipe
N = 4

print("=== TIME ALFA ===")

time_alfa = []

for _ in range(N):
    nome = str(input("Nome do robô: "))
    ataque = int(input("Ataque do robô: "))
    defesa = int(input("Defesa do robô: "))
    
    robo = {
        "nome": nome,
        "ataque": ataque,
        "defesa": defesa,
    }

    time_alfa.append(robo)

print("\n=== TIME OMEGA ===")

time_omega = []

for _ in range(N):
    nome = str(input("Nome do robô: "))
    ataque = int(input("Ataque do robô: "))
    defesa = int(input("Defesa do robô: "))
    
    robo = {
        "nome": nome,
        "ataque": ataque,
        "defesa": defesa,
    }

    time_omega.append(robo)

# Combates
vitorias_alfa = 0
vitorias_omega = 0
empates = 0

for i in range(N):
    robo_alfa = time_alfa[i]
    robo_omega = time_omega[i]

    impacto_alfa_no_omega = robo_alfa["ataque"] - robo_omega["defesa"]
    impacto_omega_no_alfa = robo_omega["ataque"] - robo_alfa["defesa"]

    if robo_alfa["ataque"] + robo_alfa["defesa"] > 100:
        impacto_alfa_no_omega = float("-inf")
    if robo_omega["ataque"] + robo_omega["defesa"] > 100:
        impacto_omega_no_alfa = float("-inf")
    
    print(f"DUELO {i+1}: {robo_alfa["nome"]} ({robo_alfa["ataque"]}/{robo_alfa["defesa"]}) x {robo_omega["nome"]} ({robo_omega["ataque"]}/{robo_omega["defesa"]})")
    print(f"Impacto {robo_alfa["nome"]} sobre {robo_omega["nome"]}: {robo_alfa["ataque"]} - {robo_omega["defesa"]} = {"INVÁLIDO" if impacto_alfa_no_omega == float("-inf") else impacto_alfa_no_omega}")
    print(f"Impacto {robo_omega["nome"]} sobre {robo_alfa["nome"]}: {robo_omega["ataque"]} - {robo_alfa["defesa"]} = {"INVÁLIDO" if impacto_omega_no_alfa == float("-inf") else impacto_omega_no_alfa}")
    
    if impacto_alfa_no_omega > impacto_omega_no_alfa:
        print(f"Vencedor: {robo_alfa["nome"]} (Equipe Alfa)")
        vitorias_alfa += 1
    elif impacto_alfa_no_omega < impacto_omega_no_alfa:
        print(f"Vencedor: {robo_omega["nome"]} (Equipe Omega)")
        vitorias_omega += 1
    else:
        print(f"Empate")
        empates += 1
    
    print()

print("--- PLACAR FINAL ---")
print(f"Vitórias Equipe Alfa: {vitorias_alfa}")
print(f"Vitórias Equipe Omega: {vitorias_omega}")
print(f"Empates: {empates}")
print()

if vitorias_alfa > vitorias_omega:
    print("🏆 Equipe Alfa é a grande vencedora!")
elif vitorias_omega > vitorias_alfa:
    print("🏆 Equipe Omega é a grande vencedora!")
else:
    print("🏆 A partida resultou em Empate!")

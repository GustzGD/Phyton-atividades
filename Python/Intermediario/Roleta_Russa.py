import random

escolha1 = "Papel"
escolha2 = "Tesoura"
escolha3 = "Pedra"

escolha = ""
escolhaIAString = ""

pontosIA = 0
pontosHM = 0

print("Jogo: Pedra, Papel e Tesoura\n")

while True:
    print("Escolha (", escolha1, ",", escolha2, ",", escolha3, ")")
    escolha = input("Jogar: ").capitalize()

    if escolha not in [escolha1, escolha2, escolha3]:
        print("Escolha inválida. Tente novamente.")
        continue

    escolhaIA = random.randint(1, 3)
    
    if escolhaIA == 1:
        escolhaIAString = escolha1
    elif escolhaIA == 2:
        escolhaIAString = escolha2
    else:
        escolhaIAString = escolha3

    print(f"\nIA jogou ({escolhaIAString}), você jogou ({escolha})")

    # IA vence
    if escolha == "Papel" and escolhaIAString == "Tesoura":
        pontosIA += 1
        print(f"IA cortou seu papel!\nPlacar:\nVocê: {pontosHM} | IA: {pontosIA}")

    elif escolha == "Tesoura" and escolhaIAString == "Pedra":
        pontosIA += 1
        print(f"IA quebrou sua tesoura!\nPlacar:\nVocê: {pontosHM} | IA: {pontosIA}")

    elif escolha == "Pedra" and escolhaIAString == "Papel":
        pontosIA += 1
        print(f"IA embrulhou sua pedra!\nPlacar:\nVocê: {pontosHM} | IA: {pontosIA}")

    # Humano vence
    elif escolha == "Tesoura" and escolhaIAString == "Papel":
        pontosHM += 1
        print(f"Você cortou o papel da IA!\nPlacar:\nVocê: {pontosHM} | IA: {pontosIA}")

    elif escolha == "Pedra" and escolhaIAString == "Tesoura":
        pontosHM += 1
        print(f"Você quebrou a tesoura da IA!\nPlacar:\nVocê: {pontosHM} | IA: {pontosIA}")

    elif escolha == "Papel" and escolhaIAString == "Pedra":
        pontosHM += 1
        print(f"Você embrulhou a pedra da IA!\nPlacar:\nVocê: {pontosHM} | IA: {pontosIA}")

    # Empate
    elif escolha == escolhaIAString:
        print(f"Empate!\nPlacar:\nVocê: {pontosHM} | IA: {pontosIA}")



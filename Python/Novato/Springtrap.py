import random

print("🎯 Bem-vindo ao Jogo de Adivinhação!")
print("Estou pensando em um número entre 1 e 100...")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("🔻 Muito baixo. Tente novamente.")
        elif palpite > numero_secreto:
            print("🔺 Muito alto. Tente novamente.")
        else:
            print(f"🎉 Parabéns! Você acertou o número em {tentativas} tentativas.")
            break
    except ValueError:
        print("❌ Por favor, digite um número inteiro válido.")

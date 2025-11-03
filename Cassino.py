jogador = input("Qual seu nome?")
poupanca = int(input("Quanto dinheiro você quer depositar? (máximo R$1000)"))
if poupanca > 1000 or poupanca < 0:
    print("Valor indefinido. Definindo para R$500")
    poupanca = 500
import random
num_maquina = random.randint(1,5)
while True:
    palpite = int(input("Para jogar é simples apenas tente adivinhar o número que a máquina escolheu entre 1 a 5: "))
    if palpite == num_maquina:
        print("Parabéns você ganhou 200 reais!")
        poupanca += 200
        num_maquina = random.randint(1, 5)
    elif palpite < num_maquina or palpite > num_maquina:
        print(f"Você errou! Tente novamente")
        poupanca -= 100
    if poupanca <= 0:
        print("Seu dinheiro acabou! Jogo encerrado.")
        break


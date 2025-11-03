import random
computador = random.randint(1, 5)
while True:
    palpite = int(input('Digite um número entre 1 a 5: '))
    if palpite == computador:
        print('Você acertou!')
    if palpite > computador:
        print(f'você errou o número escolhido é menor')
    if palpite < computador:
        print('você errou o número escolhido é maior')
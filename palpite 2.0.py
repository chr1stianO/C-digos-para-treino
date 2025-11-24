import random
numero_computador = random.randint (1, 10)
tentativa = 5
while True:
    num1 = int(input("Escreva dois números que somando eles de algum número entre 1 a 10. Escreva o primeiro número:"))
    num2 = int(input("Escreva o segundo número:"))
    soma = num1 + num2
    if soma > numero_computador:
        print ("A soma dos seus números é maior que o valor da máquina, tente de novo.")
        tentativa -= 1
    if soma < numero_computador:
        print ("A soma dos seus números é menor que o valor da máquina, tente de novo.")
        tentativa -= 1
    if soma == numero_computador:
        print ("Parábens! Você acertou!")
        break
    if tentativa == 0:
        print('tentativas acabadas.')
        break
print ('Coloque as notas para tirar a média.')
n1 = input(float('nota 1: '))
n2 = input(float('nota 2: '))
n3 = input(float('nota 3: '))
n4 = input(float('nota 4: '))
media = n1 + n2 + n3 + n4 / 4
print (f'Sua média é: {media}')
if media >= 6:
    print ('Você foi aprovado!')
else:
    print ('Você foi reprovado!')
print ('-' * 30)
print ('Seja bem-vindo ao cronômetro!')
print ('-' * 30)
esc = input('Quer usar o cronômetro em segundos ou minutos? ')

if esc == 'segundos':
    import time    
    while True:
        contador = input('Quantos segundos quer cronometrar: ')
        if contador.isdigit():
                contador = float(contador)
                break
        else:
            print('Escreva apenas números!')
    while True:
        time.sleep(1)
        contador -= 1.0
        print (contador)
        if contador == 0:
            break
    
if esc == 'minutos':
    import time
    while True:
        contador = input('Quantos minutos quer cronometrar: ')
        if contador.isdigit():
                contador = float(contador)
                break
        else:
            print('Escreva apenas números!')
    min = contador * 60
    while True:
        time.sleep(1)
        min -= 1.0
        print (min)
        if min == 0:
            break
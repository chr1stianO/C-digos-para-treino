import random
print ("escolhendo um sabor aleatório de pizza... ")
import time
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
while True:    
    sabor = random.randint(1, 5)

    if sabor == 1:
        print ("Seu sabor é Calabresa!")
        break
    if sabor == 2:
        print ("Seu sabor é mussarela!")
        break
    if sabor == 3:
        print ("Seu sabor é portuguesa!")
        break
    if sabor == 4:
        print ("Seu sabor é bacon!")
        break
    if sabor == 5:
        print ("Seu sabor é frango!")
        break
#Programa que haga que el usuario intente adivinar un número aleatorio del 1 al 10 y le diga si perdio o gano.
import random
x = 3
aleatorio = random.randint(1, 10)
while x > 0:
    entrada = int(input("Intenta adivinar un número aleatorio del 1 al 10, tienes 3 oportunidades!  = "))
    if entrada == aleatorio:
        print("Has ganado!")
        break
    else:
        x-=1
        print(f"Ahora te quedan {x} oportunidades")
    if x == 0:
        print ("Has perdido!")
        

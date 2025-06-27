#Calculo de el area de una circunferencia solo con un radio dado
import math
try:
    Radio = float(input("Ingresa el radio de la circunferencia  =  "))
    Area  = math.pi*pow(Radio, 2)
    print(f"el area de la circunferencia con radio {Radio} es {Area}")
except ValueError:
    print("Ingresa un número valido!")
except:
    print("Error desconocido")

print("¡Gracias por usar este programa!")
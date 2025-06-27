#Dado funcional de cien caras.
import random
print ("=================\nDADO DE 100 CARAS\n=================\n")
while True:
    girar = input ("Ingresa un punto para girar, si quieres terminar la aplicación, solo escribe -salir-  =  ")
    if girar != "." and girar != "salir":
        print("\nIngresa un punto o salir!!\n")
        continue
    if girar == "salir":
        print("\nHas salido del dado de las cien caras!\n")
        break
    aleatorio = random.randint(0,100)
    print (f"\nEl dado ha girado y salio el número = {aleatorio}\n")



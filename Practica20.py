#Dado con trampa (los que tira Brian jajajaja)
import random as r
import time as t
while True:
    def lanzar_dado():
        girar = input ("Ingresa un enter para girar =  ")
        if girar != "":
            print("\nIngresa un enter!!\n")
        else:
            if r.random()<0.5:
                return 6
            else:
                return r.randint(1, 5)
    
    print ("\nEl dado ha girado = ", lanzar_dado())
    t.sleep(1)
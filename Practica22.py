#Palabras por segundo
txt = input ("Texto =")
palabras = txt.split(" ")
cantidad_palabras = len(palabras)
tiempo = cantidad_palabras/2
tiempo_dalto = tiempo*0.70
if tiempo >= 60:
    print ("Dale broki, tampoco te pedi un testamento.")
else:
    print (f"\nLa cantidad de palabras en el texto es = {cantidad_palabras} y te demorarias diciendola {tiempo} segundos")
    print (f"\nDavid diria {cantidad_palabras} palabras en {tiempo_dalto} segundos")
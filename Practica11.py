#Contraseña aleatoria y con inicio de sesión.
import random
import string
caracteres = string.ascii_letters + string.digits + string.punctuation
try:
    print("Escribe un punto '.' para generar una nueva contraseña.")
    print("Escribe 'salir' para terminar el programa.")
    while True:
        ingresar = input(">>> ")
        if ingresar == ".":
            longitud = random.sample(caracteres, 12)
            password = "".join(longitud)
            print("CONTRASEÑA NUEVA = ", password)
        elif ingresar.lower() == "salir":
            break
        else:
            print("¡¡Solo puedes ingresar un punto o salir NOOB!!.")
    iniciar = input ("¿Quieres iniciar sesión? ")
    if iniciar.lower() == "si":
        def validar_contraseña(contraseña):
            contraseña_correcta = password
            if contraseña == contraseña_correcta:
                print("¡La contraseña es correcta, q pro has iniciado sesión!")
            else:
                print("¡La contraseña es incorrecta, jajajajaja. Intentalo otra vez!")
    else:
        print("No has iniciado sesión, vago!")
    contraseña_ingresada = input("ingrese su contraseña: ")
    validar_contraseña(contraseña_ingresada)
except:
    print("Ups, ha ocurrido un error!") 
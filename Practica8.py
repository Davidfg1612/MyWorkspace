#Programa que determina la jerarquia de 3 números.
print("********************************************************\nPrograma que determina la jerarquia de 3 números\n********************************************************")
try:
    N1= float(input("Ingresa el primer número  =  "))
    N2= float(input("Ingresa el segundo número  =  "))
    N3= float(input("Ingresa el tercer número  =  "))

    if N1 > N2 and N1> N3:
        print(f"El número {N1} es mas grande que {N2} y {N3}")
    elif N2 > N1 and N2 >N3:
        print(f"El número {N2} es mas grande que {N3} Y {N1}")
    elif N3 > N1 and N3 >N2:
        print(f"El número {N3} es mas grande que {N2} Y {N1}")
    elif N1==N2 and N1 > N3:
        print(f"Los números {N1} y {N2} son iguales pero mas grandes que {N3}")
    elif N3==N2 and N3 > N1:
        print(f"Los números {N3} y {N2} son iguales pero mas grandes que {N1}")
    elif N1==N3 and N1 > N2:
        print(f"Los números {N1} y {N3} son iguales pero mas grandes que {N2}")
    elif N1==N2==N3:
        print(f"Los números {N1}, {N2} y {N3} son iguales")
    else:
        print("Esta posibilidad no esta registrada aún")
except ValueError:
    print("¡Escribe un número, NOOB!")
except:
    print("ERROR DESCONOCIDO, PORFAVOR REPORTAR!")
print("¡Gracias por usar este programa!")
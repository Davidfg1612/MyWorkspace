#Conversor de palabras a números y viceversa.
a = "=========="
b = "CONVERSOR"
print(f"{a}")
print(f"{b}")
print(f"{a}")
print("Menú de opciones:")
print("Presiona 1 para convertir un número a palabra.")
print("Presiona 2 para convertir una palabra a número.")
Valor = input("¿Cuál es tu opción deseada? = ")
if Valor == "1":
    numero1 = input("Selecciona el número a convertir (1-5): ")
    if numero1 == "1":
        print("El número 1 en palabras es: UNO")
    elif numero1 == "2":
        print("El número 2 en palabras es: DOS")
    elif numero1 == "3":
        print("El número 3 en palabras es: TRES")
    elif numero1 == "4":
        print("El número 4 en palabras es: CUATRO")
    elif numero1 == "5":
        print("El número 5 en palabras es: CINCO")
    else:
        print("Ese número no está registrado")
elif Valor == "2":
    palabra = input("Selecciona la palabra a convertir (uno-cinco): ")
    if palabra == "uno":
        print("La palabra UNO corresponde al número: 1")
    elif palabra == "dos":
        print("La palabra DOS corresponde al número: 2")
    elif palabra == "tres":
        print("La palabra TRES corresponde al número: 3")
    elif palabra == "cuatro":
        print("La palabra CUATRO corresponde al número: 4")
    elif palabra == "cinco":
        print("La palabra CINCO corresponde al número: 5")
    else:
        print("Esa palabra no está registrada")
else:
    print("Opción no válida. Intenta con 1 o 2.")
    
print("¡Gracias por usar este programa!")



# Pide un número al usuario y muestra su tabla de multiplicar del 1 al 50.
while True:
    try:
        numero = int(input("\nDame un número y te mostraré su tabla de multiplicar hasta el 50. Si quieres salir, pon el número 0: "))
        if numero == 0:
            print("\n¡Has salido del programa!")
            break
        for x in range(1, 51):
            resultado = numero * x
            print(f"{x} * {numero} = {resultado}")
    except ValueError:
        print("\n¡Escribe un número válido!\n")
print("¡Gracias por usar este programa!")

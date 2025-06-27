#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
import time
while True:
    try:
        frutas = {
            "platano": "1.35$",
            "manzana": "0.80$",
            "pera": "0.85$",
            "naranja": "0.70$",
            "mandarina": "1.50$"
        }

        print("\nMenú de opciones =")
        print("\nSi quieres salir del menú solo ingresa -terminar-")
        for fruta, precio in frutas.items():
            print(f"{fruta.title()}: {precio}")
        fruta=input("Ingresa cual fruta quieres llevar (o si quieres salir ya sabes que decir)= ").lower()
        if fruta == "terminar":
            print("Has salido del menú exitosamente!")
            break
        elif fruta not in frutas:
            print("Esa fruta no esta en el menú, intentalo de nuevo")
            continue
    
        kilos=float(input(f"Ingresa cuantos kilos de {fruta} te llevaras = "))
        valor_unitario=float(frutas[fruta].replace("$", ""))
        valor_total=kilos*valor_unitario
        print(f"\nTotal a pagar por {kilos} kg de {fruta}: {valor_total:.2f}$")
        time.sleep(1)
    except Exception as e:
        print (f"Ha ocurrido un error inesperado {e}")
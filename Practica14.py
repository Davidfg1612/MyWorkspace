# Juego de piedra, papel o tijera con la PC:
import random

opciones = ["piedra", "papel", "tijera", "salir"]

print("Posibles opciones:\n")
print(", ".join(opciones))

while True:
        jugador = input("\nIngresa tu opción = ").lower()

        if jugador not in opciones:
            print("¡Elige una opción válida!")
            continue

        if jugador == "salir":
            print("¡Has salido del programa!")
            break

        maquina = random.choice(opciones[:-1])
        print(f"La máquina ha sacado = {maquina}")

        if jugador == maquina:
            print("¡Empate!")
        elif jugador == "piedra" and maquina == "tijera" or \
            jugador == "tijera" and maquina == "papel" or \
            jugador == "papel" and maquina == "piedra":
            print("\n¡Has ganado!\n")
        else:
            print("\n¡Has perdido!\n")



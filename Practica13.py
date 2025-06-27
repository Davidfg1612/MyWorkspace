# Diccionario con acceso a datos personales(Solo pedi ayuda cambiando formato de texto, usando ", ".join y el isinstance)
Personaje = {
    "nombre": "David Alejandro",
    "apellidos": "Fernández Gallego",
    "edad": 14,
    "familia": ["Diana", "Walter", "Brian", "Luna"],
    "deportes": ["Natación", "Baloncesto"],
    "colegio": "I. T. I Pascual Bravo",
    "pais": "Colombia",
    "ciudad": "Medellin",
    "barrio": "Picacho",
    "amigos": ["Sebas", "Yordan", "Esteban", "Farley", "Emmanuel", "Usuga", "Zuleta", "Otalvaro",],
    "lenguaje": "Python"
}

print("\nPuedes preguntar por alguno de estos datos:")
print("\n ".join(Personaje.keys()))

while True:
    try:
        dato = input("\n¿Qué quieres saber sobre mí? (Escribe 'salir' para terminar el programa): ").lower()
        if dato == "salir":
            print("\n¡Has salido del programa!")
            break
        elif dato in Personaje:
            valor = Personaje[dato]
            if isinstance(valor, list):
                print(f"\n{dato.capitalize()}: {', '.join(valor)}")
            else:
                print(f"\n{dato.capitalize()}: {valor}")
        else:
            print("\n¡Dato no encontrado! Escribe exactamente una de estas opciones:")
            print(", ".join(Personaje.keys()))
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

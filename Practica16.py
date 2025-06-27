#Contador de vocales en una frase x.

while True:
    frase = input("\nIngresa la frase para que se cuenten sus vocales, para terminarlo ingresa un punto: ").lower()
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    total_vocales = 0
    if frase == ".":
        print("Has salido del programa!")
        break
    for letra in frase:
        if letra in vocales:
            total_vocales += 1
    print(f"Cantidad total de vocales: {total_vocales}")
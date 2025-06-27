# La pizzería Bella Medalla.
ingredientes_permanentes = ["Queso", "Salsa de tomate", "Masa"]
pizza_carnivora = ["Pepperoni", "Chorizo", "Carne", "Pulpo"]
pizza_vegetariana = ["Cebolla", "Champiñon", "Pimientos", "Maiz dulce"]
pizza_exotica = ["Piña", "Uva asada", "Jabali", "Pato"]
pizza_mixta = pizza_carnivora + pizza_vegetariana + pizza_exotica

def pizzacarnivora():
    print("\nIngredientes disponibles:", ", ".join(pizza_carnivora))
    while True:
        try:
            cantidad_ingredientes = int(input("\n¿Cuántos ingredientes deseas para tu pizza? (0 para regresar): "))
            if cantidad_ingredientes == 0:
                break
            elif cantidad_ingredientes == 1:
                ingrediente = input("\nIngrese el ingrediente deseado: ").capitalize()
                if ingrediente in pizza_carnivora:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes + [ingrediente])}.\n\nFelicidades, has completado tu pedido.")
                    return
            
                else:
                    print("\nEse ingrediente no está en la lista de opciones.")
                    return

            elif cantidad_ingredientes == 2:
                ingrediente1 = input("\nIngrese el primer ingrediente deseado: ").capitalize()
                ingrediente2 = input("\nIngrese el segundo ingrediente deseado: ").capitalize()
                if ingrediente1 == ingrediente2:
                    print("Elige ingredientes diferentes.")
                    return
                elif ingrediente1 in pizza_carnivora and ingrediente2 in pizza_carnivora:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes)} y {ingrediente1} y {ingrediente2}.\n\nFelicidades, has completado tu pedido.")
                    return
                else:
                    print("Uno o ambos ingredientes no están en la lista de opciones.")
                    return

            elif cantidad_ingredientes == 3:
                ingrediente1 = input("\nIngrese el primer ingrediente deseado: ").capitalize()
                ingrediente2 = input("\nIngrese el segundo ingrediente deseado: ").capitalize()
                ingrediente3 = input("\nIngrese el tercer ingrediente deseado: ").capitalize()
                if ingrediente1 == ingrediente2 or ingrediente1 == ingrediente3 or ingrediente2 == ingrediente3:
                    print("Elige ingredientes diferentes.")
                elif ingrediente1 in pizza_carnivora and ingrediente2 in pizza_carnivora and ingrediente3 in pizza_carnivora:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes)}, {ingrediente1}, {ingrediente2} y {ingrediente3}.\n\nFelicidades, has completado tu pedido.")
                    return
                else:
                    print("Alguno de los ingredientes no están en la lista de opciones.")
                    return

            elif cantidad_ingredientes == 4:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes)}, {', '.join(pizza_carnivora)}.\n\nFelicidades, has completado tu pedido.")
                    return

            else:
                print ("Ingresa una cantidad coherente!")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
def pizzavegetariana():
    print("\nIngredientes disponibles:", ", ".join(pizza_vegetariana))
    while True:
        try:
            cantidad_ingredientes = int(input("\n¿Cuántos ingredientes deseas para tu pizza? (0 para regresar): "))
            if cantidad_ingredientes == 0:
                break
            elif cantidad_ingredientes == 1:
                ingrediente = input("\nIngrese el ingrediente deseado: ").capitalize()
                if ingrediente in pizza_vegetariana:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes + [ingrediente])}.\n\nFelicidades, has completado tu pedido.")
                    return
            
                else:
                    print("\nEse ingrediente no está en la lista de opciones.")
                    return

            elif cantidad_ingredientes == 2:
                ingrediente1 = input("\nIngrese el primer ingrediente deseado: ").capitalize()
                ingrediente2 = input("\nIngrese el segundo ingrediente deseado: ").capitalize()
                if ingrediente1 == ingrediente2:
                    print("Elige ingredientes diferentes.")
                    return
                elif ingrediente1 in pizza_vegetariana and ingrediente2 in pizza_vegetariana:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes)} y {ingrediente1} y {ingrediente2}.\n\nFelicidades, has completado tu pedido.")
                    return
                else:
                    print("Uno o ambos ingredientes no están en la lista de opciones.")
                    return

            elif cantidad_ingredientes == 3:
                ingrediente1 = input("\nIngrese el primer ingrediente deseado: ").capitalize()
                ingrediente2 = input("\nIngrese el segundo ingrediente deseado: ").capitalize()
                ingrediente3 = input("\nIngrese el tercer ingrediente deseado: ").capitalize()
                if ingrediente1 == ingrediente2 or ingrediente1 == ingrediente3 or ingrediente2 == ingrediente3:
                    print("Elige ingredientes diferentes.")
                elif ingrediente1 in pizza_vegetariana and ingrediente2 in pizza_vegetariana and ingrediente3 in pizza_vegetariana:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes)}, {ingrediente1}, {ingrediente2} y {ingrediente3}.\n\nFelicidades, has completado tu pedido.")
                    return
                else:
                    print("Alguno de los ingredientes no están en la lista de opciones.")
                    return

            elif cantidad_ingredientes == 4:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes)}, {', '.join(pizza_vegetariana)}.\n\nFelicidades, has completado tu pedido.")
                    return

            else:
                print ("Ingresa una cantidad coherente!")
            
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
def pizzaexotica():
    print("\nIngredientes disponibles:", ", ".join(pizza_exotica))
    while True:
        try:
            cantidad_ingredientes = int(input("\n¿Cuántos ingredientes deseas para tu pizza? (0 para regresar): "))
            if cantidad_ingredientes == 0:
                break
            elif cantidad_ingredientes == 1:
                ingrediente = input("\nIngrese el ingrediente deseado: ").capitalize()
                if ingrediente in pizza_exotica:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes + [ingrediente])}.\n\nFelicidades, has completado tu pedido.")
                    return
            
                else:
                    print("\nEse ingrediente no está en la lista de opciones.")
                    return

            elif cantidad_ingredientes == 2:
                ingrediente1 = input("\nIngrese el primer ingrediente deseado: ").capitalize()
                ingrediente2 = input("\nIngrese el segundo ingrediente deseado: ").capitalize()
                if ingrediente1 == ingrediente2:
                    print("Elige ingredientes diferentes.")
                    return
                elif ingrediente1 in pizza_exotica and ingrediente2 in pizza_exotica:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes)} y {ingrediente1} y {ingrediente2}.\n\nFelicidades, has completado tu pedido.")
                    return
                else:
                    print("Uno o ambos ingredientes no están en la lista de opciones.")
                    return

            elif cantidad_ingredientes == 3:
                ingrediente1 = input("\nIngrese el primer ingrediente deseado: ").capitalize()
                ingrediente2 = input("\nIngrese el segundo ingrediente deseado: ").capitalize()
                ingrediente3 = input("\nIngrese el tercer ingrediente deseado: ").capitalize()
                if ingrediente1 == ingrediente2 or ingrediente1 == ingrediente3 or ingrediente2 == ingrediente3:
                    print("Elige ingredientes diferentes.")
                elif ingrediente1 in pizza_exotica and ingrediente2 in pizza_exotica and ingrediente3 in pizza_exotica:
                    print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes)}, {ingrediente1}, {ingrediente2} y {ingrediente3}.\n\nFelicidades, has completado tu pedido.")
                    return
                else:
                    print("Alguno de los ingredientes no están en la lista de opciones.")
                    return

            elif cantidad_ingredientes == 4:
                print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes)}, {', '.join(pizza_exotica)}.\n\nFelicidades, has completado tu pedido.")
                return
            else:
                print ("Ingresa una cantidad coherente!")

        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
def pizzamixta():
    print("\nIngredientes disponibles:", ", ".join(pizza_mixta))
    while True:
        try:
            cantidad_ingredientes = int(input("\n¿Cuántos ingredientes deseas para tu pizza? (0 para regresar, máximo 5): "))
            if cantidad_ingredientes == 0:
                return
            elif 1 <= cantidad_ingredientes <= 5:
                seleccionados = []
                for i in range(cantidad_ingredientes):
                    ingrediente = input(f"Ingrese el ingrediente número {i + 1}: ").capitalize()
                    if ingrediente in seleccionados:
                        print("Ese ingrediente ya fue elegido. Elige uno diferente.")
                        return
                    if ingrediente in pizza_mixta:
                        seleccionados.append(ingrediente)
                    else:
                        print("Ese ingrediente no está en la lista. Intenta de nuevo.")
                        return
                print(f"\nTu pizza contiene: {', '.join(ingredientes_permanentes + seleccionados)}.\n\nFelicidades, has completado tu pedido.")
                return
            else:
                print("Solo puedes elegir hasta 5 ingredientes.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

pizzas = {
    "pizza_carnivora": pizza_carnivora,
    "pizza_vegetariana": pizza_vegetariana,
    "pizza_exotica": pizza_exotica,
    "pizza_mixta": pizza_mixta
}

print("\n==============================================================================")
print("=                  Bienvenido a la pizzería Bella Medalla                    =")
print("=                                  Menú                                      =")
print("==============================================================================")
print("= Pizza carnivora    ------------", ", ".join(pizza_carnivora), "          =\n")
print("= Pizza vegetariana  ------------", ", ".join(pizza_vegetariana), " =\n")
print("= Pizza exotica      ------------", ", ".join(pizza_exotica), "             =\n")
print("= Pizza mixta        ------------ Estilo Buffet (Los ingredientes que desee) =\n")
print("=================================================================++=============")

while True:
    try:
        pizza_elegida = input("\n¿Cuál pizza deseas escoger? (Ingresa 'salir' para cerrar la pizzeria): ").capitalize()
        if pizza_elegida == "Salir":
            print("\nHas salido de la pizzeria.")
            break
        elif pizza_elegida == "Pizza carnivora":
            print("\nLa pizza elegida ha sido la pizza carnivora.")
            pizzacarnivora()
        elif pizza_elegida == "Pizza vegetariana":
            print("\nLa pizza elegida ha sido la pizza vegetariana.")
            pizzavegetariana()
        elif pizza_elegida == "Pizza exotica":
            print("\nLa pizza elegida ha sido la pizza exotica.")
            pizzaexotica()
        elif pizza_elegida == "Pizza mixta":
            print("\nLa pizza elegida ha sido la pizza mixta.")
            pizzamixta()
        else:
            print("\nEsa pizza aún no está disponible. ¡Cooming Soon!")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
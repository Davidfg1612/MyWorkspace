# La pizzería Bella Medalla.

from Pizzas import pizzacarnivora as PC, pizzaexotica as PE, pizzamixta as PM, pizzavegetariana as PV

ingredientes_permanentes = ["Queso", "Salsa de tomate", "Masa"]
pizza_carnivora = ["Pepperoni", "Chorizo", "Carne", "Pulpo"]
pizza_vegetariana = ["Cebolla", "Champiñon", "Pimientos", "Maiz dulce"]
pizza_exotica = ["Piña", "Uva asada", "Jabali", "Pato"]
pizza_mixta = pizza_carnivora + pizza_vegetariana + pizza_exotica

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
print("================================================================================")

while True:
    try:
        pizza_elegida = input("\n¿Cuál pizza deseas escoger? (Ingresa 'salir' para cerrar la pizzeria): ").capitalize()
        if pizza_elegida == "Salir":
            print("\nHas salido de la pizzeria.")
            break
        elif pizza_elegida == "Pizza carnivora":
            print("\nLa pizza elegida ha sido la pizza carnivora.")
            PC()
        elif pizza_elegida == "Pizza vegetariana":
            print("\nLa pizza elegida ha sido la pizza vegetariana.")
            PV()
        elif pizza_elegida == "Pizza exotica":
            print("\nLa pizza elegida ha sido la pizza exotica.")
            PE()
        elif pizza_elegida == "Pizza mixta":
            print("\nLa pizza elegida ha sido la pizza mixta.")
            PM()
        else:
            print("\nEsa pizza aún no está disponible. ¡Cooming Soon!")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
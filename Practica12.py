#Maquina expendedora con funciones (Me encanto el resultado jjsjsjs).
def maquina(lays, chocolatina, pepsi, cocacola, fanta, redbull, moster, agua, jugohit, chocorramo, oreo): 
    print("=====================================")
    print("=========MAQUINA EXPENDEDORA=========")
    print("=====================================")
    print("=          Opciones:                =")
    print("= A = Lays          B = Chocolatina =")
    print("= C = Pepsi         D = CocaCola    =")
    print("= E = Fanta         F = RedBull     =")
    print("= G = Moster        H = Agua        =")
    print("= I = JugoHit       J = Chocorramo  =")
    print("=           K = Oreo                =")
    print("=====================================")

    while True:
        try:
            resultado = input("¿Qué quieres comprar hoy? Ingresa la letra (o escribe 'Salir' para terminar): ")
            if resultado == "a":
                print(f"\nSe ha entregado: {lays}\n")
            elif resultado == "b":
                print(f"\nSe ha entregado: {chocolatina}\n")
            elif resultado == "c":
                print(f"\nSe ha entregado: {pepsi}\n")
            elif resultado == "d":
                print(f"\nSe ha entregado: {cocacola}\n")
            elif resultado == "e":
                print(f"\nSe ha entregado: {fanta}\n")
            elif resultado == "f":
                print(f"\nSe ha entregado: {redbull}\n")
            elif resultado == "g":
                print(f"\nSe ha entregado: {moster}\n")
            elif resultado == "h":
                print(f"\nSe ha entregado: {agua}\n")
            elif resultado == "i":
                print(f"\nSe ha entregado: {jugohit}\n")
            elif resultado == "j":
                print(f"\nSe ha entregado: {chocorramo}\n")
            elif resultado == "k":
                print(f"\nSe ha entregado: {oreo}\n")
            elif resultado.capitalize() == "Salir":
                print("\nHas salido de la máquina expendedora, vuelve pronto botsin\n")
                break
            else:
                print("\nOpción no registrada, deja de trollear una vez.\n")
        except Exception as e:
            print(f"\nHa ocurrido un error inesperado: {e}\n")

maquina("Lays", "Chocolatina", "Pepsi", "CocaCola", "Fanta", "RedBull", "Moster", "Agua", "JugoHit", "Chocorramo", "Oreo")


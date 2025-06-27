#Perfil estudiante.

class Estudiante:
    def __init__(self, Nombre, Edad, Grado):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Grado = Grado
        self.Estudiando = False

    def Si_Estudiando(self):
        self.Estudiando = True
    def Estado(self):
        if not self.Estudiando:
            print("\nEl estudiante NO esta estudiando!\n")
        else:
            print("\nEl estudiante esta estudiando\n")

nombre = input("Ingresa el nombre de la instancia: ")
edad = int(input("Ingresa la edad de la instancia: "))
grado = int(input("Ingresa el grado de la instancia: "))

Estudiante1 = Estudiante(Nombre=nombre, Edad=edad, Grado=grado)

print (f"\nPrimer estudiante tiene como nombre {Estudiante1.Nombre}, su edad es {Estudiante1.Edad} y su grado es {Estudiante1.Grado}°\n")
estudiando = input(f"¿El estudiante {Estudiante1.Nombre} esta estudiando? (si o no): ").lower()
if estudiando == "si":
    Estudiante1.Si_Estudiando()
    Estudiante1.Estado()
else:
    Estudiante1.Estado()

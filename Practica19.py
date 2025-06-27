#Primer codigo con el paradigma POO.
class Coche:
    #Atributos de clase
    ruedas = 4
    motor = "Motor V8 Biturbo"

    def __init__(self, color, puertas, velocidad, aceleración):
        #Atributos de instancia
        self.color = color
        self.puertas = puertas
        self.velocidad = velocidad
        self.aceleración = aceleración
        self.movimiento = False
        
    def arrancar(self):
        self.movimiento = True

    def estado(self):
        if self.movimiento:
            return "En movimiento"
        else:
            return "Detenido"
#Instancias
FGX = Coche("Rojo", 4, 300, 9.26)
Divad = Coche("Negro", 4, 350, 7.94)
Enchanted = Coche("Azul eléctrico", 2, 400, 13.89)

# Mostramos resultados
FGX.arrancar()
Enchanted.arrancar()

print("\n--- Estado de las instancias ---\n")

print(f"FGX:\n"
    f"Color = {FGX.color}\n"
    f"Puertas = {FGX.puertas}\n"
    f"Velocidad máxima = {FGX.velocidad} Km/h\n"
    f"Aceleración = {FGX.aceleración}\n"
    f"Ruedas = {FGX.ruedas}\n"
    f"Motor = {FGX.motor}\n"
    f"Estado = {FGX.estado()}\n")

print(f"Divad:\n"
    f"Color = {Divad.color}\n"
    f"Puertas = {Divad.puertas}\n"
    f"Velocidad máxima = {Divad.velocidad} Km/h\n"
    f"Aceleración = {Divad.aceleración}\n"
    f"Ruedas = {Divad.ruedas}\n"
    f"Motor = {Divad.motor}\n"
    f"Estado = {Divad.estado()}\n")

print(f"Enchanted:\n"
    f"Color = {Enchanted.color}\n"
    f"Puertas = {Enchanted.puertas}\n"
    f"Velocidad máxima = {Enchanted.velocidad} Km/h\n"
    f"Aceleración = {Enchanted.aceleración}\n"
    f"Ruedas = {Enchanted.ruedas}\n"
    f"Motor = {Enchanted.motor}\n"
    f"Estado = {Enchanted.estado()}\n")
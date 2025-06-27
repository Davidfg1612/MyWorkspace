#Dias de vacaciones según tres claves diferentes.
a = ("Sistema Vacacional Rappi de los venecos para los venecos")
b = ("********************************************************")
print(f"{b}")
print(f"{a}")
print(f"{b}")
Nombre = input("Ingrese tu nombre y apellido = ")
Clave = input("Ingrese tu departamento = ")
Antiguedad = int(input("Ingrese cuantos años has trabajado en tu puesto = "))
if Clave == "Atencion al cliente" and Antiguedad == 1:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 10 dias de vacaciones. ¡Felicidades!")
elif  Clave == "Atencion al cliente" and Antiguedad >=2 and Antiguedad <=6:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 20 dias de vacaciones. ¡Felicidades!")
elif  Clave == "Atencion al cliente" and Antiguedad >=7:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 30 dias de vacaciones. ¡Felicidades!")
elif Clave == "Logística" and Antiguedad == 1:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 12 dias de vacaciones. ¡Felicidades!")
elif  Clave == "Logística" and Antiguedad >=2 and Antiguedad <=6:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 24 dias de vacaciones. ¡Felicidades!")
elif  Clave == "Logística" and Antiguedad >=7:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 34 dias de vacaciones. ¡Felicidades!")
elif Clave == "Gerencia" and Antiguedad == 1:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 15 dias de vacaciones. ¡Felicidades!")
elif  Clave == "Gerencia" and Antiguedad >=2 and Antiguedad <=6:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 25 dias de vacaciones. ¡Felicidades!")
elif  Clave == "Gerencia" and Antiguedad >=7:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 36 dias de vacaciones. ¡Felicidades!")
elif Clave == "Ingenieria" and Antiguedad == 1:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 18 dias de vacaciones. ¡Felicidades!")
elif  Clave == "Ingenieria" and Antiguedad >=2 and Antiguedad <=6:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 28 dias de vacaciones. ¡Felicidades!")
elif  Clave == "Ingenieria" and Antiguedad >=7:
    print(f"Señor {Nombre} del departamento de {Clave} tienes derecho a 40 dias de vacaciones. ¡Felicidades!")
else:
    print("Su departamento no existe o esta mal escrito, escribalo correctamente porfavor")

print("¡Gracias por usar este programa!")
import time
import datetime
import os
import locale
locale.setlocale(locale.LC_TIME, 'Spanish_Spain')
try:
    while True:
        os.system("cls")
        actual = datetime.datetime.now()
        Fecha_Formateada = actual.strftime("%A, %d de %B de %Y, %H:%M:%S").capitalize()
        print("****************************************")
        print("*                Reloj                 *")
        print("****************************************")
        print(f"*{Fecha_Formateada}*")
        print("****************************************")
        print("Presiona Ctrl + C para salir")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nEl reloj se ha detenido.")

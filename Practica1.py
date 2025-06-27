#Calculo de suma de dos numeros
try:
    N1 = float(input("Ingresa el primer número  =  "))
    N2 = float(input("Ingresa el segundo número  =  "))
    Resultado = N1+N2
    print (f"El resultado de {N1} + {N2} es {Resultado}")
except ValueError:
    print("¡Escribe un número valido!")

print("¡Gracias por usar este programa!")
#Número par o impar
a =("***************************************************")
b =("Programa que determina si un número es par o impar")
print(f"{a}")
print(f"{b}")
print(f"{a}")

N = int(input("Ingrese el número ENTERO para ver si es par o impar =  "))

if N%2 == 0:
    print(f"El número {N} es par")
elif N%2 == 1:
    print(f"El número {N} es impar")
else:
    print("Ups, ha ocurrido un error")
    
print("¡Gracias por usar este programa!")
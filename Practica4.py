# calculadora (versión 1.5)
import math

def suma(numero1, numero2):
    return numero1+numero2

def resta(numero1, numero2):
    return numero1-numero2

def multiplicación(numero1, numero2):
    return numero1*numero2

def división(numero1, numero2):
    if numero2 == 0:
        return "No se puede dividir por 0"
    else:
        return numero1 / numero2

def modulo(numero1, numero2):
    if numero2 == 0:
        return "No se puede dividir por 0"
    else:
        return numero1 % numero2

def división_entera(numero1, numero2):
    if numero2 == 0:
        return "No se puede dividir por 0"
    else:
        return numero1 // numero2

def potencia(numero1, numero2):
    return numero1 ** numero2

def raiz_nesima(numero1, numero2):
    if numero2==0:
        raise ValueError("No se puede calcular la raíz con índice cero")
    elif numero1<0 and numero2% 2 == 0:
        raise ValueError("No se puede calcular la raíz par de un numero menor a 0")
    else:
        return numero1**(1/numero2)

def log_base_x(numero1, numero2):
    return math.log(numero1, numero2)

def raiz_cuadrada(numero):
    return math.sqrt(numero)

def raiz_cubica(numero):
    return numero**(1/3)

def valor_absoluto(numero):
    return abs(numero)

def log_base10(numero):
    return math.log10(numero)

def log_base2(numero):
    return math.log2(numero)

def log_base_e(numero):
    return math.log(numero)

def factorial(numero):
    return math.factorial(numero)

def area_triangulo(base, altura):
    return (altura * base) / 2

def area_circulo(radio):
    return math.pi*(radio ** 2)

def area_cuadrado(lado):
    return lado ** 2

def area_elipse(semieje_menor, semieje_mayor):
    return semieje_mayor * semieje_menor*math.pi

def area_rombo(diagonal_menor, diagonal_mayor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_rectangulo(lado1, lado2):
    return lado1*lado2

def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor)*altura) / 2

def area_poligono(apotema, perimetro):
    return (apotema * perimetro)/2

def area_sector_circular(radio, angulo):
    return (math.pi * radio ** 2 * angulo) / 360

def coseno (numero):
    return math.cos(numero)

def seno (numero):
    return math.sin(numero)

def tangente (numero):
    return math.tan(numero)

def deg_grad (numero):
    return math.degrees(numero)

def grad_deg (numero):
    return math.radians(numero)

def log1p_custom (numero):
    return math.log1p(numero)

def around (numero):
    return math.trunc(numero)

def around_menos (numero):
    return math.floor(numero)

def around_mas (numero):
    return math.ceil (numero)

def exp_e (numero):
    return math.exp(numero)

def MCM (numero1, numero2):
    return math.lcm (int(numero1), int(numero2))

def MCD (numero1, numero2):
    return math.gcd (int(numero1), int(numero2))

def hypotenusa (numero1, numero2):
    return math.hypot(numero1, numero2)

def fibonacci(numero):
    if numero < 0:
        raise ValueError("n debe ser un entero no negativo")
    elif numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, int(numero) + 1):
            a, b = b, a + b
        return b
    
def porcentaje(porcentaje, total):
    return (porcentaje / 100) * total

def entero(numero):
    return int(numero)
print("\n=============================================================")
print("======================== CALCULADORA ========================")
print("=============================================================")
print("===================== Menú de opciones ======================")
print("=============================================================")
print("===  1. +         2. -          3. *        4. /          ===")
print("===  5. **        6. √          7. ³√       8. ⁿ√x        ===")
print("===  9. //        10. |x|       11. %       12. log₁₀     ===")
print("=== 13. logₑ      14. log₂      15. logₓ    16. !         ===")
print("=== 17. area      18. sin       19. cos     20. tan       ===")
print("=== 21. deg-grad  22. grad-deg  23. round   24. round+    ===")
print("=== 25. round-    26. MCD       27. MCM     28. int       ===")
print("=== 29. log1p     30. e^x       31. hypot   32. fibo      ===")
print("=== 33. porc                                              ===")
print("=============================================================")
print("=========================  Salir  ===========================")
print("=============================================================\n")
while True:
    operacion = input("\n--- Ingresa operación---: ").strip().lower()

    if operacion not in ["+", "-", "*", "/", "**", "//", "%",
                    "logₓ", "ⁿ√x", "√", "³√", "|x|", "log₁₀",
                    "log₂", "logₑ", "!", "sin", "cos", "tan", 
                    "deg-grad", "grad-deg", "area", "round+", 
                    "round-", "round", "mcd", "mcm", "int",
                    "e^x", "log1p", "fibo", "hypot", "porc"]:
        print("Operación no válida. Intenta de nuevo.")
        continue
    if operacion == "salir":
        print("Adiós.")
        break

    try:
        if operacion in ["+", "-", "*", "/", "**", "//", "%", "logₓ", "ⁿ√x", "mcd", "mcm", "hypot", "porc"]:
            num1 = float(input("Número 1: "))
            num2 = float(input("Número 2: "))

            if operacion == "+": resultado = suma(num1, num2)
            elif operacion == "-": resultado = resta(num1, num2)
            elif operacion == "*": resultado = multiplicación(num1, num2)
            elif operacion == "/": resultado = división(num1, num2)
            elif operacion == "**": resultado = potencia(num1, num2)
            elif operacion == "//": resultado = división_entera(num1, num2)
            elif operacion == "%": resultado = modulo(num1, num2)
            elif operacion == "logₓ": resultado = log_base_x(num1, num2)
            elif operacion == "ⁿ√x": resultado = raiz_nesima(num1, num2)
            elif operacion == "mcd": resultado = MCD(num1, num2)
            elif operacion == "mcm": resultado = MCM(num1, num2)
            elif operacion == "hypot": resultado = hypotenusa(num1, num2)
            elif operacion == "porc": resultado = porcentaje(num1, num2)

            if operacion in ["+", "-", "*", "/", "**", "//", "%"]:
                print(f"📓 {num1} {operacion} {num2} = {resultado}")
            elif operacion == "porc":
                print(f"📓 El {num2}% de {num1} = {resultado}")
            elif operacion == "logₓ":
                print(f"📓 log base {num2} de {num1} = {resultado}")
            elif operacion == "ⁿ√x":
                print(f"📓 raíz {num2}-ésima de {num1} = {resultado}")
            elif operacion == "mcd":
                print(f"📓 mcd({int(num1)}, {int(num2)}) = {resultado}")
            elif operacion == "mcm":
                print(f"📓 mcm({int(num1)}, {int(num2)}) = {resultado}")
            elif operacion == "hypot":
                print(f"📓 hipotenusa de ({num1}, {num2}) = {resultado}")

        elif operacion in ["√", "³√", "|x|", "log₁₀", "log₂", "logₑ", "!", "sin", "cos", "tan", "deg-grad", "grad-deg", "e^x", "log1p", "fibo", "int", "round-", "round+", "round"]:
            num = float(input("Número: "))

            if operacion == "√": resultado = raiz_cuadrada(num)
            elif operacion == "³√": resultado = raiz_cubica(num)
            elif operacion == "|x|": resultado = valor_absoluto(num)
            elif operacion == "log₁₀": resultado = log_base10(num)
            elif operacion == "log₂": resultado = log_base2(num)
            elif operacion == "logₑ": resultado = log_base_e(num)
            elif operacion == "!": resultado = factorial(int(num))
            elif operacion == "sin": resultado = seno(num)
            elif operacion == "cos": resultado = coseno(num)
            elif operacion == "tan": resultado = tangente(num)
            elif operacion == "deg-grad": resultado = deg_grad(num)
            elif operacion == "grad-deg": resultado = grad_deg(num)
            elif operacion == "e^x": resultado = exp_e(num)
            elif operacion == "log1p": resultado = log1p_custom(num)
            elif operacion == "fibo": resultado = fibonacci(int(num))
            elif operacion == "int": resultado = entero(num)
            elif operacion == "round": resultado = around(num)
            elif operacion == "round+": resultado = around_mas(num)
            elif operacion == "round-": resultado = around_menos(num)
            print(f"📘 Resultado: {resultado}")

        elif operacion == "area":
            figura = input("Tipo de figura (triángulo, círculo, elipse, rombo, rectángulo, trapecio, polígono, sector): ").strip().lower()

            if figura == "triángulo":
                b = float(input("Base: "))
                h = float(input("Altura: "))
                resultado = area_triangulo(b, h)
            elif figura == "círculo":
                r = float(input("Radio: "))
                resultado = area_circulo(r)
            elif figura == "elipse":
                a = float(input("Semieje menor: "))
                b = float(input("Semieje mayor: "))
                resultado = area_elipse(a, b)
            elif figura == "rombo":
                d1 = float(input("Diagonal menor: "))
                d2 = float(input("Diagonal mayor: "))
                resultado = area_rombo(d1, d2)
            elif figura == "rectángulo":
                l1 = float(input("Base: "))
                l2 = float(input("Altura: "))
                resultado = area_rectangulo(l1, l2)
            elif figura == "trapecio":
                bm = float(input("Base mayor: "))
                bmn = float(input("Base menor: "))
                h = float(input("Altura: "))
                resultado = area_trapecio(bm, bmn, h)
            elif figura == "polígono":
                ap = float(input("Apotema: "))
                p = float(input("Perímetro: "))
                resultado = area_poligono(ap, p)
            elif figura == "sector":
                r = float(input("Radio: "))
                ang = float(input("Ángulo en grados: "))
                resultado = area_sector_circular(r, ang)
            else:
                resultado = "Figura no reconocida"

            print(f"📘 Área de {figura}: {resultado}")

        else:
            print("Operación no reconocida.")

    except Exception as e:
        print(f"Ha ocurrido un error, vuelve a intentarlo: {e}")

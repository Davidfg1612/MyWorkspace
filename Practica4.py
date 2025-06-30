# calculadora (versión 1.5)
import Operaciones

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

            if operacion == "+": resultado = Operaciones.suma(num1, num2)
            elif operacion == "-": resultado = Operaciones.resta(num1, num2)
            elif operacion == "*": resultado = Operaciones.multiplicación(num1, num2)
            elif operacion == "/": resultado = Operaciones.división(num1, num2)
            elif operacion == "**": resultado = Operaciones.potencia(num1, num2)
            elif operacion == "//": resultado = Operaciones.división_entera(num1, num2)
            elif operacion == "%": resultado = Operaciones.modulo(num1, num2)
            elif operacion == "logₓ": resultado = Operaciones.log_base_x(num1, num2)
            elif operacion == "ⁿ√x": resultado = Operaciones.raiz_nesima(num1, num2)
            elif operacion == "mcd": resultado = Operaciones.MCD(num1, num2)
            elif operacion == "mcm": resultado = Operaciones.MCM(num1, num2)
            elif operacion == "hypot": resultado = Operaciones.hypotenusa(num1, num2)
            elif operacion == "porc": resultado = Operaciones.porcentaje(num1, num2)

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

            if operacion == "√": resultado = Operaciones.raiz_cuadrada(num)
            elif operacion == "³√": resultado = Operaciones.raiz_cubica(num)
            elif operacion == "|x|": resultado = Operaciones.valor_absoluto(num)
            elif operacion == "log₁₀": resultado = Operaciones.log_base10(num)
            elif operacion == "log₂": resultado = Operaciones.log_base2(num)
            elif operacion == "logₑ": resultado = Operaciones.log_base_e(num)
            elif operacion == "!": resultado = Operaciones.factorial(int(num))
            elif operacion == "sin": resultado = Operaciones.seno(num)
            elif operacion == "cos": resultado = Operaciones.coseno(num)
            elif operacion == "tan": resultado = Operaciones.tangente(num)
            elif operacion == "deg-grad": resultado = Operaciones.deg_grad(num)
            elif operacion == "grad-deg": resultado = Operaciones.grad_deg(num)
            elif operacion == "e^x": resultado = Operaciones.exp_e(num)
            elif operacion == "log1p": resultado = Operaciones.log1p_custom(num)
            elif operacion == "fibo": resultado = Operaciones.fibonacci(int(num))
            elif operacion == "int": resultado = Operaciones.entero(num)
            elif operacion == "round": resultado = Operaciones.around(num)
            elif operacion == "round+": resultado = Operaciones.around_mas(num)
            elif operacion == "round-": resultado = Operaciones.around_menos(num)
            print(f"📘 Resultado: {resultado}")

        elif operacion == "area":
            figura = input("Tipo de figura (triángulo, círculo, elipse, rombo, rectángulo, trapecio, polígono, sector): ").strip().lower()

            if figura == "triángulo":
                b = float(input("Base: "))
                h = float(input("Altura: "))
                resultado = Operaciones.area_triangulo(b, h)
            elif figura == "círculo":
                r = float(input("Radio: "))
                resultado = Operaciones.area_circulo(r)
            elif figura == "elipse":
                a = float(input("Semieje menor: "))
                b = float(input("Semieje mayor: "))
                resultado = Operaciones.area_elipse(a, b)
            elif figura == "rombo":
                d1 = float(input("Diagonal menor: "))
                d2 = float(input("Diagonal mayor: "))
                resultado = Operaciones.area_rombo(d1, d2)
            elif figura == "rectángulo":
                l1 = float(input("Base: "))
                l2 = float(input("Altura: "))
                resultado = Operaciones.area_rectangulo(l1, l2)
            elif figura == "trapecio":
                bm = float(input("Base mayor: "))
                bmn = float(input("Base menor: "))
                h = float(input("Altura: "))
                resultado = Operaciones.area_trapecio(bm, bmn, h)
            elif figura == "polígono":
                ap = float(input("Apotema: "))
                p = float(input("Perímetro: "))
                resultado = Operaciones.area_poligono(ap, p)
            elif figura == "sector":
                r = float(input("Radio: "))
                ang = float(input("Ángulo en grados: "))
                resultado = Operaciones.area_sector_circular(r, ang)
            else:
                resultado = "Figura no reconocida"

            print(f"📘 Área de {figura}: {resultado}")

        else:
            print("Operación no reconocida.")

    except Exception as e:
        print(f"Ha ocurrido un error, vuelve a intentarlo: {e}")

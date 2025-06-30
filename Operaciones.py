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
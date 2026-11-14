"""Funciones matemáticas de la calculadora.

Este módulo solo realiza cálculos. No pide datos ni imprime nada:
de eso se encarga calculadora.py.
Cuando una entrada no es válida, las funciones lanzan ValueError
con un mensaje claro.
"""

import math


def suma(a, b):
    """Devuelve a + b."""
    return a + b


def resta(a, b):
    """Devuelve a - b."""
    return a - b


def multiplicacion(a, b):
    """Devuelve a * b."""
    return a * b


def division(a, b):
    """Devuelve a / b. No permite dividir entre cero."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def potencia(base, exponente):
    """Devuelve base elevada a exponente (positivo, negativo o cero)."""
    if base == 0 and exponente < 0:
        raise ValueError("0 elevado a un exponente negativo no está definido.")
    try:
        resultado = base ** exponente
    except OverflowError:
        raise ValueError("El resultado es demasiado grande.")
    if isinstance(resultado, complex):
        raise ValueError(
            "Una base negativa con exponente decimal no tiene resultado real."
        )
    return resultado


def modulo(a, b):
    """Devuelve el residuo de a / b. No permite divisor cero."""
    if b == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero.")
    return a % b


def raiz_cuadrada(numero):
    """Devuelve la raíz cuadrada de un número no negativo."""
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un negativo.")
    return math.sqrt(numero)


def porcentaje(porcentaje_valor, cantidad):
    """Devuelve el porcentaje_valor % de cantidad (15 % de 200 = 30)."""
    return cantidad * porcentaje_valor / 100


def valor_absoluto(numero):
    """Devuelve el valor absoluto de un número."""
    return abs(numero)


def factorial(numero):
    """Devuelve el factorial de un entero no negativo."""
    if numero != int(numero):
        raise ValueError("El factorial solo se define para números enteros.")
    numero = int(numero)
    if numero < 0:
        raise ValueError("El factorial no se define para números negativos.")
    if numero > 1000:
        raise ValueError("El número es demasiado grande (máximo 1000).")
    return math.factorial(numero)


def promedio(numeros):
    """Devuelve el promedio de una lista de números."""
    if len(numeros) == 0:
        raise ValueError("Se necesita al menos un número para el promedio.")
    return sum(numeros) / len(numeros)


def redondear(numero, decimales):
    """Redondea un número a la cantidad de decimales indicada."""
    if decimales != int(decimales):
        raise ValueError("Los decimales deben ser un número entero.")
    if decimales < 0:
        raise ValueError("Los decimales no pueden ser negativos.")
    return round(numero, int(decimales))

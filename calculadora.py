"""Calculadora ampliada: menú e interacción con el usuario.

Las operaciones matemáticas están en operaciones.py.
Ejecutar con:  python calculadora.py
"""

import operaciones

historial = []


# ---------------------------------------------------------------------------
# Entrada de datos con validación
# ---------------------------------------------------------------------------
def leer_numero(mensaje):
    """Pide un número hasta que el usuario escribe uno válido."""
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            numero = float(texto)
        except ValueError:
            print("  Entrada no válida: escribe un número (ejemplo: 12 o 3.5).")
            continue
        if numero != numero or numero in (float("inf"), float("-inf")):
            print("  Entrada no válida: escribe un número finito.")
            continue
        # Si es entero (5.0), se maneja como int para mostrarlo sin ".0"
        return int(numero) if numero.is_integer() else numero


def leer_lista_numeros():
    """Pide varios números separados por espacios."""
    while True:
        texto = input("Números separados por espacios: ").strip().replace(",", ".")
        partes = texto.split()
        if not partes:
            print("  Debes escribir al menos un número.")
            continue
        try:
            numeros = [float(p) for p in partes]
        except ValueError:
            print("  Entrada no válida: todos los valores deben ser números.")
            continue
        if any(n != n or n in (float("inf"), float("-inf")) for n in numeros):
            print("  Entrada no válida: escribe números finitos.")
            continue
        return numeros


def leer_decimales():
    """Pide la cantidad de decimales para redondear (opcional)."""
    while True:
        texto = input("¿Redondear a cuántos decimales? (Enter = sin redondear): ").strip()
        if texto == "":
            return None
        if texto.isdigit():
            return int(texto)
        print("  Escribe un entero mayor o igual a 0, o presiona Enter.")


def formatear(numero):
    """Muestra enteros sin decimales y limita los decimales largos."""
    if isinstance(numero, float):
        if numero.is_integer():
            return str(int(numero))
        return f"{numero:.10g}"
    return str(numero)


# ---------------------------------------------------------------------------
# Acciones del menú: cada una devuelve (descripción, resultado)
# ---------------------------------------------------------------------------
def pedir_dos(texto_a, texto_b):
    return leer_numero(texto_a), leer_numero(texto_b)


def accion_suma():
    a, b = pedir_dos("Primer número: ", "Segundo número: ")
    return f"{formatear(a)} + {formatear(b)}", operaciones.suma(a, b)


def accion_resta():
    a, b = pedir_dos("Primer número: ", "Segundo número: ")
    return f"{formatear(a)} - {formatear(b)}", operaciones.resta(a, b)


def accion_multiplicacion():
    a, b = pedir_dos("Primer número: ", "Segundo número: ")
    return f"{formatear(a)} * {formatear(b)}", operaciones.multiplicacion(a, b)


def accion_division():
    a, b = pedir_dos("Dividendo: ", "Divisor: ")
    return f"{formatear(a)} / {formatear(b)}", operaciones.division(a, b)


def accion_potencia():
    a, b = pedir_dos("Base: ", "Exponente: ")
    return f"{formatear(a)} ^ {formatear(b)}", operaciones.potencia(a, b)


def accion_modulo():
    a, b = pedir_dos("Dividendo: ", "Divisor: ")
    return f"{formatear(a)} mod {formatear(b)}", operaciones.modulo(a, b)


def accion_raiz():
    n = leer_numero("Número: ")
    return f"raíz({formatear(n)})", operaciones.raiz_cuadrada(n)


def accion_porcentaje():
    p = leer_numero("Porcentaje (ejemplo 15): ")
    c = leer_numero("Cantidad (ejemplo 200): ")
    return f"{formatear(p)}% de {formatear(c)}", operaciones.porcentaje(p, c)


def accion_absoluto():
    n = leer_numero("Número: ")
    return f"|{formatear(n)}|", operaciones.valor_absoluto(n)


def accion_factorial():
    n = leer_numero("Entero no negativo: ")
    return f"{formatear(n)}!", operaciones.factorial(n)


def accion_promedio():
    numeros = leer_lista_numeros()
    texto = ", ".join(formatear(n) for n in numeros)
    return f"promedio({texto})", operaciones.promedio(numeros)


def accion_redondeo():
    n = leer_numero("Número a redondear: ")
    d = leer_numero("Cantidad de decimales: ")
    return f"redondeo({formatear(n)}, {formatear(d)} decimales)", operaciones.redondear(n, d)


# Menú: opción -> (nombre, función)
MENU = {
    "1": ("Suma", accion_suma),
    "2": ("Resta", accion_resta),
    "3": ("Multiplicación", accion_multiplicacion),
    "4": ("División", accion_division),
    "5": ("Potencia", accion_potencia),
    "6": ("Módulo (residuo)", accion_modulo),
    "7": ("Raíz cuadrada", accion_raiz),
    "8": ("Porcentaje", accion_porcentaje),
    "9": ("Valor absoluto", accion_absoluto),
    "10": ("Factorial", accion_factorial),
    "11": ("Promedio", accion_promedio),
    "12": ("Redondeo", accion_redondeo),
}


def mostrar_menu():
    print("\n" + "=" * 36)
    print("        CALCULADORA AMPLIADA")
    print("=" * 36)
    print(" Operaciones básicas")
    for clave in ("1", "2", "3", "4"):
        print(f"  {clave:>2}. {MENU[clave][0]}")
    print(" Operaciones avanzadas")
    for clave in ("5", "6", "7", "8", "9", "10", "11", "12"):
        print(f"  {clave:>2}. {MENU[clave][0]}")
    print(" Historial")
    print(" 13. Ver historial")
    print(" 14. Limpiar historial")
    print("  0. Salir")
    print("-" * 36)


# ---------------------------------------------------------------------------
# Historial
# ---------------------------------------------------------------------------
def ver_historial():
    if not historial:
        print("\nEl historial está vacío.")
        return
    print("\n--- Historial de operaciones ---")
    for i, registro in enumerate(historial, start=1):
        print(f"  {i}. {registro}")


def limpiar_historial():
    if not historial:
        print("\nEl historial ya está vacío.")
        return
    historial.clear()
    print("\nHistorial borrado.")


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------
def ejecutar_operacion(opcion):
    nombre, accion = MENU[opcion]
    print(f"\n--- {nombre} ---")
    try:
        descripcion, resultado = accion()
    except ValueError as error:
        print(f"Error: {error}")
        return
    # Redondeo opcional (no aplica a la operación de redondeo en sí)
    if opcion != "12" and not isinstance(resultado, int):
        decimales = leer_decimales()
        if decimales is not None:
            resultado = operaciones.redondear(resultado, decimales)
    texto = f"{descripcion} = {formatear(resultado)}"
    print(f"Resultado: {texto}")
    historial.append(texto)


def preguntar_si_continuar():
    while True:
        respuesta = input("\n¿Realizar otra operación? (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("  Responde 's' para sí o 'n' para no.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            break
        elif opcion in MENU:
            ejecutar_operacion(opcion)
        elif opcion == "13":
            ver_historial()
        elif opcion == "14":
            limpiar_historial()
        else:
            print("Opción no válida. Elige un número del menú.")
            continue

        if not preguntar_si_continuar():
            break

    print("\n¡Hasta pronto!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nPrograma finalizado.")

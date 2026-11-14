# Calculadora 

## Descripción

Calculadora de consola desarrollada en Python como parte de la **Práctica 2 – Ampliación de la calculadora** (Actualización Tecnológica). Permite realizar operaciones básicas y avanzadas desde un menú, valida las entradas del usuario para que el programa no falle, permite repetir operaciones sin reiniciar y guarda un historial de lo calculado durante la ejecución.

## Operaciones y estados

| N.º | Funcionalidad | Estado |
|----|---------------|--------|
| 1 | Potencia |  Completada |
| 2 | Módulo |  Completada |
| 3 | Raíz cuadrada (rechaza negativos) |  Completada |
| 4 | Porcentaje |  Completada |
| 5 | Valor absoluto |  Completada |
| 6 | Factorial |  Completada |
| 7 | Promedio |  Completada |
| 8 | Redondeo |  Completada |
| 9 | Validación de entradas | Completada |
| 10 | División por cero / módulo con divisor cero |  Completada |
| 11 | Menú mejorado |  Completada |
| 12 | Repetir operaciones |  Completada |
| 13 | Historial de operaciones (adicional) |  Completada |
| 14 | Limpiar historial (adicional) |  Completada |
| 15 | Mejorar documentación (adicional) |  Completada |

## Tecnologías

- Python 3
- Git
- GitHub (Issues)
- Markdown

## Estructura del proyecto

```
CALCULADORA/
├── README.md          # Documentación
├── calculadora.py     # Menú, entrada de datos y resultados
└── operaciones.py     # Funciones matemáticas
```

## Instalación y ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/gonzalesstifalejandro-alt/CALCULADORA.git
   cd CALCULADORA
   ```

2. Ejecutar el programa (requiere Python 3.8 o superior, no necesita librerías externas):

   ```bash
   python calculadora.py
   ```

## Ejemplos de uso

**Porcentaje**

```
Elige una opción: 8
Porcentaje (ejemplo 15): 15
Cantidad (ejemplo 200): 200
¿Redondear a cuántos decimales? (Enter = sin redondear):
Resultado: 15% de 200 = 30
```

**Potencia con exponente negativo**

```
Elige una opción: 5
Base: 2
Exponente: -2
Resultado: 2 ^ -2 = 0.25
```

**División por cero**

```
Elige una opción: 4
Dividendo: 10
Divisor: 0
Error: No se puede dividir entre cero.
```

**Entrada no numérica**

```
Primer número: abc
  Entrada no válida: escribe un número (ejemplo: 12 o 3.5).
Primer número:
```

**Historial**

```
Elige una opción: 13

--- Historial de operaciones ---
  1. 15% de 200 = 30
  2. 2 ^ -2 = 0.25
```

## Autor

**Gonzales Stif Alejandro**

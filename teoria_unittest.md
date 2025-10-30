# Pruebas unitarias

## ¿Qué son las pruebas unitarias?

Las pruebas unitarias (unit tests) son un tipo de prueba de software que verifica el correcto funcionamiento de una unidad de código, normalmente una función, método o clase individual, de manera aislada del resto del sistema.

Su objetivo principal es el de detectar errores temprano en el ciclo de desarrollo y asegurar que cada parte del código haga exactamente lo que se espera.

## ¿Cómo usar las pruebas unitarias?

En Python, el módulo estándar unittest se utiliza para escribir y ejecutar pruebas.

Ejemplo básico:

import unittest

from calculadora import sumar

class TestCalculadora(unittest.TestCase):

 def test_sumar(self):
 
   resultado = sumar(2, 3)
        
   self.assertEqual(resultado, 5)

if __name__ == "__main__":

  unittest.main()

Ejecutar las pruebas:

python -m unittest test_calculadora.py

## ¿Por qué usar pruebas unitarias?

- Previenen errores futuros: ayudan detectando problemas rápidamente cuando el código cambia.

- Facilitan el mantenimiento: si algo falla, las pruebas indicaran en dónde.

- Mejoran la calidad del código: promueven un diseño modular y limpio.

- Ahorran tiempo a largo plazo: aunque al principio llevan tiempo, reducen fallos en producción.

- Aumentan la confianza en los cambios: especialmente útil en equipos grandes o proyectos extensos.

## ¿Cuándo usar pruebas unitarias?

- Durante el desarrollo: al crear nuevas funciones o clases.

- Antes de integrar módulos: para asegurar que cada pieza funciona por sí sola.

- Al corregir errores: primero se escribe una prueba que reproduzca el error, luego se corrige el código.

- Al refactorizar: para confirmar que los cambios no rompen el comportamiento previo.

## 1. Buenas prácticas

- Una prueba debe verificarse con solo una cosa.

- Los nombres deben ser claros y descriptivos.

- No depender de otros recursos externos (como bases de datos o red).

- Mantener las pruebas rápidas y repetibles.

- Integrarlas en un sistema de integración continua (CI).

## 2. Ejemplo de estructura de proyecto con pruebas

mi_proyecto/

├── calculadora.py

├── test/

│   ├── __init__.py

│   └── test_calculadora.py

└── teoria_unittest.md




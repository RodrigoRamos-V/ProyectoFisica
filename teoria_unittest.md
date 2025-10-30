1) ¿Qué son las pruebas unitarias?

Las pruebas unitarias (unit tests) son un tipo de prueba de software que verifica el correcto funcionamiento de una unidad de código, normalmente una función, método o clase individual, de manera aislada del resto del sistema.

Su objetivo principal es detectar errores temprano en el ciclo de desarrollo y asegurar que cada parte del código haga exactamente lo que se espera.

2) ¿Cómo usar las pruebas unitarias?

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

3) ¿Por qué usar pruebas unitarias?

- Previenen errores futuros: ayudan a detectar problemas rápidamente cuando el código cambia.

- Facilitan el mantenimiento: si algo falla, las pruebas indican dónde.

- Mejoran la calidad del código: promueven un diseño modular y limpio.

- Ahorran tiempo a largo plazo: aunque al principio llevan tiempo, reducen fallos en producción.

- Aumentan la confianza en los cambios: especialmente útil en equipos grandes o proyectos extensos.








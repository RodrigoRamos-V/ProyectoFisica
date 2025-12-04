import numpy as np
import matplotlib.pyplot as plt
import math
def plot_data_from_file(archivo):
    """
    Carga datos desde un archivo de texto y grafica x(t) y y(t).
    """

    try:
        data = np.loadtxt(archivo)
    except IOError:
        print(f"Error: No se pudo encontrar o leer el archivo '{archivo}'")
        return
    except ValueError:
        print(f"Error: Problema al parsear datos del archivo '{archivo}'")
        return

    t = data[:, 0]
    x = data[:, 1]
    y = data[:, 2]

    plt.figure(figsize=(8, 5))
    plt.plot(t, x, marker="o", label="x(t)")
    plt.plot(t, y, marker="s", label="y(t)")
    plt.xlabel("t")
    plt.ylabel("Valores")
    plt.title("Gráficos de x(t) y y(t)")
    plt.grid(True)
    plt.legend()
    plt.show()


class MMC:
    """
    Clase para el Método de Mínimos Cuadrados (Linear Regression).
    """
    def __init__(self, x_data, y_data):
        self.x = np.array(x_data)
        self.y = np.array(y_data)
        self.n = len(x_data)
        if self.n != len(y_data):
            raise ValueError("Las listas de datos X e Y deben tener la misma longitud.")
        self.A = 0
        self.B = 0
        self.dA = 0
        self.dB = 0

    def calculate_coefficients(self):
       
        sum_x = np.sum(self.x)
        sum_y = np.sum(self.y)
        sum_xy = np.sum(self.x * self.y)
        sum_x2 = np.sum(self.x**2)   
        denominador = self.n * sum_x2 - sum_x**2
        if denominador == 0:
            raise ValueError("No se puede realizar la regresión lineal.")
            
        self.B = (self.n * sum_xy - sum_x * sum_y) / denominador
        self.A = (sum_y / self.n) - self.B * (sum_x / self.n)
        return self.A, self.B

    def calculate_errors(self):

        if self.A == 0 and self.B == 0:
            self.calculate_coefficients()
            
        sum_residuos2 = np.sum((self.y - (self.A + self.B * self.x))**2)
        Sy = math.sqrt(sum_residuos2 / (self.n - 2))

        sum_x2 = np.sum(self.x**2)
        denominador_B = self.n * sum_x2 - np.sum(self.x)**2
        self.dB = Sy * math.sqrt(self.n / denominador_B)

        denominador_A = (self.n - 2) * (self.n * sum_x2 - np.sum(self.x)**2)
        self.dA = Sy * math.sqrt(sum_x2 / denominador_A)
        return self.dA, self.dB

import numpy as np
import matplotlib.pyplot as plt

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

# Puedes ejecutar la función directamente si el archivo existe en la misma carpeta
if __name__ == "__main__":
    archivo_default = "datos_csv.txt"
    plot_data_from_file(archivo_default)

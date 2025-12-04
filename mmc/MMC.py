import numpy as np
import matplotlib.pyplot as plt

def plot_data_from_file(archivo):

    try:
        data = np.loadtxt(archivo)
    except IOError:
        print("Error: No se pudo encontrar o leer el archivo '{archivo}'")
        return
    except ValueError:
        print("Error: Problema al parsear datos del archivo '{archivo}'")
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


if __name__ == "__main__":
    archivo_default = "datos_csv.txt"
    plot_data_from_file(archivo_default)

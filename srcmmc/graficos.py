import os
import numpy as np
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt
from linearizacion import linearizar
from mmc import mmc

def graficar(D, m):
    X, Y = linearizar(D, m)
    A, B, eA, eB = mmc(X, Y)

    X_plot = np.linspace(min(X), max(X), 200)
    Y_plot = A + B * X_plot

    plt.figure(figsize=(7,5))
    plt.scatter(X, Y, label="Datos linearizados")
    plt.plot(X_plot, Y_plot, label=f"Ajuste MMC\nA={A:.3f}±{eA:.3f}\nB={B:.3f}±{eB:.3f}")
    plt.xlabel("ln(D)")
    plt.ylabel("ln(m)")
    plt.title("Linearización y Ajuste MMC")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    os.makedirs("srcmmc", exist_ok=True)
    plt.savefig("srcmmc/linearizado_mmc.png", dpi=150)
    plt.close()

if __name__ == "__main__":
    D = [0.713, 0.998, 1.501, 1.746, 1.905, 2.222]
    m = [1.47, 4.50, 13.75, 21.70, 28.20, 44.75]

    graficar(D, m)

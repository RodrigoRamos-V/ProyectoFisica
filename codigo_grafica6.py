import pandas as pd
import matplotlib.pyplot as plt
import os

data = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [-1.000, -0.809, -0.309, 0.309, 0.809, 1.000],
    "v": [0.000, 1.847, 2.988, 2.988, 1.847, 0.000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,4))
plt.plot(df["t"], df["x"], "o-", label="Posición x(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.title("Movimiento Armónico Simple - Masa m (Tabla 6)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("grafico_posicion_tabla6.png")
plt.close()

plt.figure(figsize=(8,4))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad v(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.title("Velocidad vs Tiempo - Masa m (Tabla 6)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("grafico_velocidad_tabla6.png")
plt.close()

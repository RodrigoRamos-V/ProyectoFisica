import pandas as pd
import matplotlib.pyplot as plt

data = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [2.000, 1.806, 1.261, 0.471, -0.410, -1.211],
    "v": [0.000, -1.910, -3.448, -4.318, -4.349, -3.535]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,4))
plt.plot(df["t"], df["x"], "o-", label="Posición x(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.title("Movimiento Armónico Simple - Masa 2m (Tabla 5)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("grafico_posicion_tabla5.png")
plt.close()

plt.figure(figsize=(8,4))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad v(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.title("Velocidad vs Tiempo - Masa 2m (Tabla 5)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("grafico_velocidad_tabla5.png")
plt.close()

import pandas as pd
import matplotlib.pyplot as plt


data = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [0.707, 0.410, 0.060, -0.298, -0.618, -0.856],
    "v": [-1.283, -1.654, -1.811, -1.731, -1.427, -0.936]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 4))
plt.plot(df["t"], df["x"], "o-", label="Posición x(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.title("Movimiento Armónico Simple - Masa 3m")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad v(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.title("Velocidad vs Tiempo - Masa 3m")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [1.000, 0.951, 0.809, 0.588, 0.309, 0.000],
    "v": [0.000, -0.485, -0.923, -1.271, -1.494, -1.571]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 4))
plt.plot(df["t"], df["x"], "o-", label="Posición x(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.title("Movimiento Armónico Simple - Masa 4m")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad v(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.title("Velocidad vs Tiempo - Masa 4m")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

data = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [0.000, 0.860, 1.552, 1.944, 1.958, 1.591],
    "v": [4.443, 4.012, 2.801, 1.047, -0.910, -2.691]
}


df = pd.DataFrame(data)

plt.figure(figsize=(8,4))
plt.plot(df["t"], df["x"], "o-", label="Posición x(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.title("Movimiento Armónico Simple - Masa 2m (Tabla 4)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("grafico_posicion_tabla4.png")
plt.close()

plt.figure(figsize=(8,4))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad v(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.title("Velocidad vs Tiempo - Masa 2m (Tabla 4)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("grafico_velocidad_tabla4.png")
plt.close()

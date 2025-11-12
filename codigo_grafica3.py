import pandas as pd
import matplotlib.pyplot as plt

data = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [0.000, 0.710, 1.327, 1.772, 1.986, 1.941],
    "v": [3.628, 3.392, 2.714, 1.683, 0.433, -0.873]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 4))
plt.plot(df["t"], df["x"], "o-", label="Posición x(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.title("Movimiento Armónico Simple - Nueva masa")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_posicion_tabla3.png")
plt.close()

plt.figure(figsize=(8, 4))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad v(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.title("Velocidad vs Tiempo - Nueva masa")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_velocidad_tabla3.png")
plt.close()

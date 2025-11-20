import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data = {
    "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
    "x": [-1.000, -0.809, -0.309, 0.309, 0.809, 1.000],
    "v": [0.000, 1.847, 2.988, 2.988, 1.847, 0.000]
}

df = pd.DataFrame(data)

Path("plots6").mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8,5))
plt.plot(df["t"], df["x"], "o-b", label="Posición")
plt.title("Posición - Tabla 6")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots6/posicion6.png", dpi=150)
plt.show()
plt.close()

plt.figure(figsize=(8,5))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad")
plt.title("Velocidad - Tabla 6")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots6/velocidad6.png", dpi=150)
plt.show()
plt.close()

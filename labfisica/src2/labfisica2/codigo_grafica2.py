import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path("src/labfisica/tabla2.csv")
df = pd.read_csv(csv_path)

Path("plots").mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 5))
plt.plot(df["t"], df["x"], "o-b", label="Posición")
plt.title("Posición")
plt.xlabel("Tiempo [s]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("plots/posicion.png", dpi=150)

plt.figure(figsize=(8, 5))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad")
plt.title("Velocidad")
plt.xlabel("Tiempo [s]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("plots/velocidad.png", dpi=150)
savefig("plots/velocidad.png", dpi=150)

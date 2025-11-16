import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path("src4/labfisica4/tabla4.csv")
df = pd.DataFrame(data)

Path("plots").mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8,5))
plt.plot(df["t"], df["x"], "o-", label="Posición")
plt.title("Posición tabla 4")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("plots4/posicion4.png", dpi=150)

plt.figure(figsize=(8,5))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad")
plt.title("Velocidad tabla 4")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("plots4/velocidad4.png", dpi=150)
savefig("plots4/velocidad4.png", dpi=150)

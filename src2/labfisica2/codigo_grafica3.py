import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path("src2/labfisica2/tabla3.csv")
df = pd.DataFrame(data)

Path("plots").mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 5))
plt.plot(df["t"], df["x"], "o-b", label="Posición")
plt.title("Posición tabla 3")
plt.xlabel("Tiempo [s]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots3/posicion3.png", dpi=150)

plt.figure(figsize=(8, 5))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad")
plt.title("Velocidad tabla 3")
plt.xlabel("Tiempo [s]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots3/velocidad3.png", dpi=150)
savefig("plots3/velocidad3.png", dpi=150)

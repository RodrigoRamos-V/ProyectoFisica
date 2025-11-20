import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path("src5/labfisica5/tabla5.csv")
df = pd.DataFrame(data)

Path("plots5").mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8,5))
plt.plot(df["t"], df["x"], "o-", label="Posición")
plt.title("Posicion tabla 4")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("plots5/posicion5.png", dpi=150)
plt.close()

plt.figure(figsize=(8,5))
plt.plot(df["t"], df["v"], "o-r", label="Velocidad")
plt.title("Velocidad tabla 4)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("plots5/velocidad5.png", dpi=150)
plt.close()

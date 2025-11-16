import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data = {
    "H": [1.00, 2.00, 3.00, 4.00, 5.00, 6.00],
    "m": [8.65, 17.30, 25.95, 34.63, 43.31, 51.95]
}

df = pd.DataFrame(data)

Path("plots_cil").mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8,5))
plt.plot(df["H"], df["m"], "o-b", label="Masa")
plt.title("Masa vs Altura – Cilindros")
plt.xlabel("Altura H [cm]")
plt.ylabel("Masa [g]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots_cil/cilindros_masa_vs_altura.png", dpi=150)
plt.show()
plt.close()

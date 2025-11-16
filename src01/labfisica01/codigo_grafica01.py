import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

H = [1.00, 2.00, 3.00, 4.00, 5.00, 6.00]
m = [8.65, 17.30, 25.95, 34.63, 43.31, 51.95]

df = pd.DataFrame({"H": H, "m": m})

Path("plots_cil").mkdir(exist_ok=True)

plt.figure(figsize=(7,5))
plt.plot(df["H"], "o-", label="Altura H")
plt.title("Altura (Cilindros)")
plt.xlabel("Índice")
plt.ylabel("H [cm]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots_cil/h.png", dpi=150)
plt.show()
plt.close()

plt.figure(figsize=(7,5))
plt.plot(df["m"], "o-", label="Masa")
plt.title("Masa (Cilindros)")
plt.xlabel("Índice")
plt.ylabel("Masa [g]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots_cil/m.png", dpi=150)
plt.show()
plt.close()

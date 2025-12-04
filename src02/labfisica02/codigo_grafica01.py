import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

D = [1.00, 2.00, 3.00, 4.00, 5.00, 6.00]
m = [1.22, 4.90, 10.40, 19.52, 30.71, 43.75]

df = pd.DataFrame({"D": D, "m": m})

Path("plots_dis").mkdir(exist_ok=True)

plt.figure(figsize=(7,5))
plt.plot(df["D"], "o-", label="Diámetro D")
plt.title("Diámetro (Discos)")
plt.xlabel("Índice")
plt.ylabel("D [cm]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots_dis/D.png", dpi=150)
plt.show()
plt.close()

plt.figure(figsize=(7,5))
plt.plot(df["m"], "o-", label="Masa")
plt.title("Masa (Discos)")
plt.xlabel("Índice")
plt.ylabel("Masa [g]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots_dis/m.png", dpi=150)
plt.show()
plt.close()

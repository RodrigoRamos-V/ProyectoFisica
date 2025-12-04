import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

D = [0.713, 0.998, 1.501, 1.746, 1.905, 2.222]
m = [1.47, 4.50, 13.75, 21.70, 28.20, 44.75]

df = pd.DataFrame({"D": D, "m": m})

Path("plots_esf").mkdir(exist_ok=True)

plt.figure(figsize=(7,5))
plt.plot(df["D"], "o-", label="Diámetro D")
plt.title("Diámetro (Esferas)")
plt.xlabel("Índice")
plt.ylabel("D [cm]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots_esf/D.png", dpi=150)
plt.show()
plt.close()

plt.figure(figsize=(7,5))
plt.plot(df["m"], "o-", label="Masa")
plt.title("Masa (Esferas)")
plt.xlabel("Índice")
plt.ylabel("Masa [g]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots_esf/m.png", dpi=150)
plt.show()
plt.close()


import matplotlib.pyplot as plt
import numpy as np
from MMC import MMC

os.makedirs("image", exist_ok=True)

t = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
Y = [0.000000, 0.313, 0.627, 0.942, 1.256, 1.571]

mmc = MMC(x=t, y=Y)

x_plot = np.linspace(min(t), max(t), 200)
y_plot = mmc.A + mmc.B * x_plot

plt.figure(figsize=(7,5))
plt.scatter(t, Y, label="Datos linearizados")
plt.plot(x_plot, y_plot, label=f"Ajuste MMC\nA={mmc.A:.4f}±{mmc.A_err:.4f}\nB={mmc.B:.4f}±{mmc.B_err:.4f}")
plt.xlabel("t")
plt.ylabel("Y = acos(x/xmax)")
plt.title("Ajuste por Mínimos Cuadrados (MMC)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("image/linearizado_mmc.png", dpi=150)
plt.close()


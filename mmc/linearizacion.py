import os
import matplotlib.pyplot as plt
import numpy as np
from MMC import MMC

os.makedirs("image", exist_ok=True)

t = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
Y = [0.000000, 0.313, 0.627, 0.942, 1.256, 1.571]

mmc = MMC(x_data=t, y_data=Y)

A, B = mmc.calculate_coefficients()
dA, dB = mmc.calculate_errors()

x_plot = np.linspace(min(t), max(t), 200)
y_plot = A + B * x_plot

plt.figure(figsize=(7, 5))
plt.scatter(t, Y, label="Datos linearizados")
plt.plot(
    x_plot,
    y_plot,
    label=f"Ajuste MMC\nA={A:.4f} ± {dA:.4f}\nB={B:.4f} ± {dB:.4f}"
)

plt.xlabel("t")
plt.ylabel("Y = acos(x/xmax)")
plt.title("Ajuste por Mínimos Cuadrados (MMC)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("image/linearizado_mmc.png", dpi=150)
plt.close()
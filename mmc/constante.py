import numpy as np
import matplotlib.pyplot as plt
from MMC import MMC

# --- Cargar datos y calcular constante elástica k ---
file_path = "MMC/datos_csv.txt"  # Tu archivo CSV
mmc = MMC.from_csv(file_path)

k = mmc.B
k_err = mmc.B_err # Error de la pendiente

print(f"Constante elástica: k = {k:.3f} ± {k_err:.3f} N/m")

# --- Calcular periodo de oscilación para masa 9m ---
m_base = 0.1
m = 9 * m_base # masa 9m

T = 2 * np.pi * np.sqrt(m / k)
T_err = T * (k_err / (2 * k))  # Propagación de error

print(f"Periodo de oscilación para 9m: T = {T:.3f} ± {T_err:.3f} s")

# --- Graficar el movimiento oscilatorio ---
A = 0.05  # Amplitud inicial en metros (ejemplo)
phi = 0   # Fase inicial
omega = np.sqrt(k / m)

t = np.linspace(0, 2*T, 500)  # Dos periodos
x_t = A * np.cos(omega * t + phi)

plt.figure(figsize=(8,4))
plt.plot(t, x_t, label=f"Masa = 9m, T ≈ {T:.2f} s")
plt.xlabel("Tiempo (s)")
plt.ylabel("Desplazamiento (m)")
plt.title("Movimiento Oscilatorio")
plt.grid(True)
plt.legend()
plt.show()

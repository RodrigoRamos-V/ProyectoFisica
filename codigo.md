import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import math

# ----------------------------------------------
# DATOS EXPERIMENTALES (tablas del enunciado)
# ----------------------------------------------
datasets = [
    # factor, t[s], x[m]
    (4, [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
        [1.000, 0.951, 0.809, 0.588, 0.309, 0.000]),
    (3, [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
        [0.707, 0.410, 0.060, -0.298, -0.618, -0.856]),
    (3, [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
        [0.000, 0.710, 1.327, 1.772, 1.986, 1.941]),
    (2, [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
        [0.000, 0.860, 1.552, 1.944, 1.958, 1.591]),
    (2, [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
        [2.000, 1.806, 1.261, 0.471, -0.410, -1.211]),
    (1, [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
        [-1.000, -0.809, -0.309, 0.309, 0.809, 1.000])
]

# Errores
xe = 0.001  # [m]

# ----------------------------------------------
# MODELO TEÓRICO
# ----------------------------------------------
def modelo(t, A, omega, phi):
    """x(t) = A * cos(omega * t + phi)"""
    return A * np.cos(omega * t + phi)

# ----------------------------------------------
# AJUSTE Y CÁLCULOS
# ----------------------------------------------
resultados = []

for i, (factor, t, x) in enumerate(datasets, start=1):
    t = np.array(t)
    x = np.array(x)

    # Estimaciones iniciales
    A0 = np.max(np.abs(x))
    omega0 = 2 * math.pi
    phi0 = 0.0

    popt, pcov = curve_fit(modelo, t, x, p0=[A0, omega0, phi0], sigma=np.full_like(x, xe), absolute_sigma=True)
    perr = np.sqrt(np.diag(pcov))

    A, omega, phi = popt
    sigma_A, sigma_omega, sigma_phi = perr

    # Calcular k/m
    k_m = factor * omega**2
    sigma_k_m = factor * 2 * omega * sigma_omega

    resultados.append({
        "Masa (factor m)": factor,
        "A [m]": A,
        "ω [rad/s]": omega,
        "σ_ω": sigma_omega,
        "k/m [s⁻²]": k_m,
        "σ_(k/m)": sigma_k_m
    })

    # Graficar
    plt.figure()
    plt.errorbar(t, x, yerr=xe, fmt='o', label='Datos experimentales')
    plt.plot(t, modelo(t, *popt), '-', label=f"Ajuste: ω={omega:.2f} rad/s")
    plt.title(f"Ajuste del movimiento armónico simple (masa {factor}m)")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Posición x [m]")
    plt.legend()
    plt.grid(True)
    plt.show()

# ----------------------------------------------
# RESULTADOS FINALES
# ----------------------------------------------
df = pd.DataFrame(resultados)

# Promedio ponderado de k/m
weights = 1 / (df["σ_(k/m)"]**2)
k_m_mean = np.sum(df["k/m [s⁻²]"] * weights) / np.sum(weights)
sigma_k_m_mean = np.sqrt(1 / np.sum(weights))

# Período para masa 9m
T_9m = 6 * math.pi / math.sqrt(k_m_mean)
sigma_T_9m = (3 * math.pi / (k_m_mean ** 1.5)) * sigma_k_m_mean

print("\n--- RESULTADOS GLOBALES ---")
print(df)
print(f"\nPromedio (k/m) = {k_m_mean:.4f} ± {sigma_k_m_mean:.4f} s⁻²")
print(f"Período para masa 9m: T = {T_9m:.4f} ± {sigma_T_9m:.4f} s")

# Guardar resultados
df.to_csv("resultados_mas.csv", index=False)
print("\nResultados guardados en 'resultados_mas.csv'")

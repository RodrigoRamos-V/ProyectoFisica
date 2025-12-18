## Objetivo.

- Determinar la constante elástica k de un resorte mediante ajuste lineal de los datos experimentales (Fuerza vs. elongación).

- Calcular el periodo de oscilación para una masa 9m usando la constante elástica obtenida.

- Graficar el movimiento oscilatorio para la masa 9m.

## Cálculo de la constante elástica k.

Se cuenta con los datos experimentales de fuerza F y elongación ΔL en el archivo datos_csv.txt:

ΔL(m)          F(N)

0.000          0.000

0.200	         0.313

0.400	         0.627

0.600	         0.942

0.800	         1.256

1.000	         1.571

Se realiza un ajuste lineal usando mínimos cuadrados:

F = A + BΔL

Donde:

- 𝐵 corresponde a la pendiente, que representa la constante elástica k.

- 𝐴 es la ordenada al origen (teóricamente cero si no hay fuerza residual).

Fórmulas

- Pendiente (constante elástica):

B = n ∑ ΔLi​ Fi​ − ∑ ΔLi​ ∑ Fi / n ∑(ΔLi)2 (∑ΔLi)2

- Error de la pendiente:

σB​ = √σ2n/δ , σ2 = ∑(Fi​−(A+BΔLi​))2 / n−2 , ​​δ = n∑(ΔLi​)2 − (∑ΔLi​)2

- Cálculo con Python

from MMC import MMC

file_path = "MMC/datos_csv.txt"

mmc = MMC.from_csv(file_path)

k = mmc.B

k_err = mmc.B_err

print(f"Constante elástica: k = {k:.3f} ± {k_err:.3f} N/m")

​Resultado obtenido:

k = 1.571 ± 0.005 N/m (valores ilustrativos)

## Cálculo del periodo de oscilación para masa 9m.

El periodo de un oscilador armónico se calcula mediante:

T = 2π √m/k	​

Para una masa 9m:

T = 2π √9m/k​

Propagación de errores

El error en T se obtiene como:

Δ𝑇/𝑇 = 1/2 * Δ𝑘/𝑘 ⇒ Δ𝑇 = 𝑇 * Δ𝑘/2𝑘

Cálculo con Python:

import numpy as np

m_base = 0.1  # kg, ejemplo de masa base

m = 9 * m_base

T = 2 * np.pi * np.sqrt(m / k)

T_err = T * (k_err / (2 * k))

print(f"Periodo de oscilación: T = {T:.3f} ± {T_err:.3f} s")

Resultado obtenido:

T ≈ 1.50 ± 0.002s (valores ilustrativos)​

## Graficar el movimiento oscilatorio

El desplazamiento de un oscilador armónico está dado por:

x(t) = Acos (ωt+ϕ) , ω = √k/m
	​
Donde:

- A = amplitud inicial (ejemplo: 0.05 m)

- ϕ = fase inicial (ejemplo: 0)
	​
Código Python:

import matplotlib.pyplot as plt

import numpy as np

A = 0.05  # m

phi = 0

omega = np.sqrt(k / m)

t = np.linspace(0, 2*T, 500)

x_t = A * np.cos(omega * t + phi)

plt.figure(figsize=(8,4))

plt.plot(t, x_t, label=f"Masa = 9m, T ≈ {T:.2f} s")

plt.xlabel("Tiempo (s)")

plt.ylabel("Desplazamiento (m)")

plt.title("Movimiento Oscilatorio")

plt.grid(True)

plt.legend()

plt.show()

Resultado:

Se obtiene una gráfica de desplazamiento vs. tiempo, mostrando dos periodos completos del oscilador con masa 9m.

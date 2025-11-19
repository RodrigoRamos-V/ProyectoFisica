import math
from ProyectoFisica.MMC import MMC

t = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000]
x = [1.000, 0.951, 0.809, 0.588, 0.309, 0.000]

xmax = max(x)
Y = [math.acos(xi / xmax) for xi in x]

mmc = MMC(x=t, y=Y)

print("A =", mmc.A)
print("B =", mmc.B)
print("sigma² =", mmc.sigma2)
print("A_err =", mmc.A_err)
print("B_err =", mmc.B_err)

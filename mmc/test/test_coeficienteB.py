import math
from MMC import MMC

def test_coeficiente_B():
    t = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000]
    x = [1.000, 0.951, 0.809, 0.588, 0.309, 0.000]

    xmax = max(x)
    Y = [math.acos(xi / xmax) for xi in x]

    mmc = MMC(x=t, y=Y)

    B_esperado = 0.0001267763

    assert abs(mmc.B - B_esperado) < 1e-6

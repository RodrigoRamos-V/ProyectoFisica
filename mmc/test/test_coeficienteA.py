import math
from MMC import MMC

def test_coeficiente_A():
    t = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000]
    x = [1.000, 0.951, 0.809, 0.588, 0.309, 0.000]

    xmax = max(x)
    Y = [math.acos(xi / xmax) for xi in x]

    mmc = MMC(t, Y)
    mmc.calculate_coefficients()

    A_esperado = 1.5706331676940446

    assert abs(mmc.A - A_esperado) < 1e-6
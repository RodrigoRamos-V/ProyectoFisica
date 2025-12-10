import math
from MMC import MMC

def test_coeficiente_A():
    t = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    x = [1.0, 0.951, 0.809, 0.588, 0.309, 0.0]

    Y = [math.acos(xi / max(x)) for xi in x]

    mmc = MMC(t, Y)
    mmc.calculate_coefficients()

    A_esperado = 1.5705827644880892
    assert abs(mmc.A - A_esperado) < 1e-6
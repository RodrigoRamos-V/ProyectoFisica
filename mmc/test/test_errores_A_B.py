import math
from MMC import MMC

def test_errores_A_B():
    t = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    x = [1.0, 0.951, 0.809, 0.588, 0.309, 0.0]

    Y = [math.acos(xi / max(x)) for xi in x]

    mmc = MMC(t, Y)
    mmc.calculate_errors()

    A_err_esperado = 5.604320e-05
    B_err_esperado = 0.00012906577257161536

    assert abs(mmc.dA - A_err_esperado) < 1e-6
    assert abs(mmc.dB - B_err_esperado) < 1e-6
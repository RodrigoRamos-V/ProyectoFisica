import math
from MMC import MMC

def test_errores_A_B():
    
    t = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000]
    x = [1.000, 0.951, 0.809, 0.588, 0.309, 0.000]

    xmax = max(x)
    Y = [math.acos(xi / xmax) for xi in x]

    mmc = MMC(x=t, y=Y)
    A_err_esperado = 1.1209e-4
    B_err_esperado = 1.8511e-4

    # Verificación
    assert abs(mmc.A_err - A_err_esperado) < 1e-6
    assert abs(mmc.B_err - B_err_esperado) < 1e-6

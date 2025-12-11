from mmc import MMC


def test_coeficiente_A():
    file_path = "mmc/datos_csv.txt"
    
    
    mmc = MMC.from_csv(file_path)
    
    
    sum_x = sum(mmc.x)
    sum_y = sum(mmc.y)
    sum_x2 = sum(xi**2 for xi in mmc.x)
    sum_xy = sum(xi*yi for xi, yi in zip(mmc.x, mmc.y))
    n = len(mmc.x)
    delta = n * sum_x2 - sum_x**2
    
    valor_esperado_A = (sum_y * sum_x2 - sum_x * sum_xy) / delta
    
    
    assert abs(mmc.A - valor_esperado_A) < 1e-6, f"A calculado={mmc.A}, A esperado={valor_esperado_A}"



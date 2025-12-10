from labfisica import MMC

def test_coeficiente_B():
    file_path = "tests/data/data.csv"
    
   
    mmc = MMC.from_csv(file_path)
    
    
    sum_x = sum(mmc.x)
    sum_y = sum(mmc.y)
    sum_x2 = sum(xi**2 for xi in mmc.x)
    sum_xy = sum(xi*yi for xi, yi in zip(mmc.x, mmc.y))
    n = len(mmc.x)
    delta = n * sum_x2 - sum_x**2
    
    valor_esperado_B = (n * sum_xy - sum_x * sum_y) / delta
    
   
    assert abs(mmc.B - valor_esperado_B) < 1e-6, f"B calculado={mmc.B}, B esperado={valor_esperado_B}"


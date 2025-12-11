from mmc import MMC


def test_errores_A_B():
    file_path = "tests/data/data.csv"
    
    
    mmc = MMC.from_csv(file_path)
    
   
    x = mmc.x
    y = mmc.y
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi**2 for xi in x)
    sum_xy = sum(xi*yi for xi, yi in zip(x, y))
    delta = n * sum_x2 - sum_x**2
    
    
    A_manual = (sum_y * sum_x2 - sum_x * sum_xy)

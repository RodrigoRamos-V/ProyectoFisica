import numpy as np

def mmc(X, Y):
    """
    Ajuste lineal por mínimos cuadrados:
        Y = A + B X

    Retorna:
        A (intercepto)
        B (pendiente)
        eA (error del intercepto)
        eB (error de la pendiente)
    """

    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)

    n = len(X)

    Sx = np.sum(X)
    Sy = np.sum(Y)
    Sxx = np.sum(X*X)
    Sxy = np.sum(X*Y)

    denom = n * Sxx - Sx**2

    B = (n * Sxy - Sx * Sy) / denom
    A = (Sy * Sxx - Sx * Sxy) / denom

    # Errores
    Y_ajustada = A + B * X
    residuos = Y - Y_ajustada
    sigma2 = np.sum(residuos**2) / (n - 2)

    eA = np.sqrt(sigma2 * Sxx / denom)
    eB = np.sqrt(sigma2 * n / denom)

    return A, B, eA, eB


if __name__ == "__main__":
    import linearizacion as lin

    D = [0.713, 0.998, 1.501, 1.746, 1.905, 2.222]
    m = [1.47, 4.50, 13.75, 21.70, 28.20, 44.75]

    X, Y = lin.linearizar(D, m)
    A, B, eA, eB = mmc(X, Y)

    print("A =", A)
    print("B =", B)
    print("eA =", eA)
    print("eB =", eB)

import numpy as np

def linearizar(D, m):
    """
    Lineariza los datos usando:
        ln(m) = ln(ρπ/6) + 3 ln(D)

    Retorna:
        X = ln(D)
        Y = ln(m)
    """
    D = np.array(D, dtype=float)
    m = np.array(m, dtype=float)

    X = np.log(D)
    Y = np.log(m)

    return X, Y

if __name__ == "__main__":
    D = [0.713, 0.998, 1.501, 1.746, 1.905, 2.222]
    m = [1.47, 4.50, 13.75, 21.70, 28.20, 44.75]
    X, Y = linearizar(D, m)
    print("X =", X)
    print("Y =", Y)

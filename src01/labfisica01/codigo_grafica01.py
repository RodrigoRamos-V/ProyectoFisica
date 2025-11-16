import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    data = {
        "H_cm": [1.00, 2.00, 3.00, 4.00, 5.00, 6.00],
        "m_g":  [8.65, 17.30, 25.95, 34.63, 43.31, 51.95]
    }

    df = pd.DataFrame(data)

    Path("plots_C1").mkdir(exist_ok=True)

    plt.figure(figsize=(8,5))
    plt.scatter(df["H_cm"], df["m_g"], label="Datos", s=60)
    plt.plot(df["H_cm"], df["m_g"])
    plt.title("Tabla C.1 – Cilindros")
    plt.xlabel("H [cm]")
    plt.ylabel("m [g]")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("plots_C1/cilindros.png", dpi=150)
    plt.show()
    plt.close()

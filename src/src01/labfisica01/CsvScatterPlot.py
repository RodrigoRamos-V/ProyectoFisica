from pathlib import Path
from typing import Tuple

import pandas as pd
import matplotlib.pyplot as plt


class CsvData:
    """Clase simple para usar con make_plot"""
    def __init__(self, x, y, xName="x", yName="y", color="b"):
        self.x = x
        self.y = y
        self.xName = xName
        self.yName = yName
        self.color = color


def make_plot(data: CsvData, scatter: bool = True) -> Tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=(8, 6))

    if scatter:
        ax.scatter(data.x, data.y, marker='o', label=data.yName, color=data.color)
    else:
        ax.plot(data.x, data.y, "o-", label=data.yName, color=data.color)

    ax.set_title(data.yName)
    ax.set_xlabel(data.xName)
    ax.set_ylabel(data.yName)
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
    ax.legend()
    fig.tight_layout()
    return fig, ax


def main() -> None:

    data = {
        "H": [1.00, 2.00, 3.00, 4.00, 5.00, 6.00],
        "m": [8.65, 17.30, 25.95, 34.63, 43.31, 51.95]
    }

    df = pd.DataFrame(data)
    Path("plots_cil").mkdir(parents=True, exist_ok=True)

    altura_data = CsvData(
        x=df.index,
        y=df["H"],
        xName="Índice",
        yName="Altura H [cm]",
        color="green"
    )

    fig_h, _ = make_plot(altura_data, scatter=False)
    plt.show()
    fig_h.savefig("plots_cil/cilindros_altura.png", dpi=150)

    masa_data = CsvData(
        x=df.index,
        y=df["m"],
        xName="Índice",
        yName="Masa [g]",
        color="red"
    )

    fig_m, _ = make_plot(masa_data, scatter=False)
    plt.show()
    fig_m.savefig("plots_cil/cilindros_masa.png", dpi=150)

if __name__ == "__main__":
    main()

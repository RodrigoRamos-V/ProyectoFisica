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
        ax.scatter(data.x, data.y, marker='o', color=data.color)
    else:
        ax.plot(data.x, data.y, "o-", color=data.color)

    ax.set_title(data.yName)
    ax.set_xlabel(data.xName)
    ax.set_ylabel("Magnitud")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
    fig.tight_layout()
    return fig, ax


def main() -> None:

    data = {
        "D": [0.713, 0.998, 1.501, 1.746, 1.905, 2.222],
        "m": [1.47, 4.50, 13.75, 21.70, 28.20, 44.75]
    }

    df = pd.DataFrame(data)
    Path("plots_esf").mkdir(parents=True, exist_ok=True)

    diametro_data = CsvData(
        df.index, df["D"],
        xName="Índice",
        yName="Diámetro D [cm]",
        color="blue"
    )

    fig1, _ = make_plot(diametro_data, scatter=False)
    plt.show()
    fig1.savefig("plots_esf/D.png", dpi=150)

    masa_data = CsvData(
        df.index, df["m"],
        xName="Índice",
        yName="Masa [g]",
        color="red"
    )

    fig2, _ = make_plot(masa_data, scatter=False)
    plt.show()
    fig2.savefig("plots_esf/m.png", dpi=150)


if __name__ == "__main__":
    main()

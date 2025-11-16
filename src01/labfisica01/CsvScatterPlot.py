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
    ax.set_ylabel("Magnitud")
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
    ax.legend()
    fig.tight_layout()
    return fig, ax


def show_plot(fig: plt.Figure) -> None:
    plt.show()


def save_plot(fig: plt.Figure, filename: str | Path) -> None:
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(filename, format="png", dpi=150)


def main() -> None:
    data = {
        "H_cm": [1.00, 2.00, 3.00, 4.00, 5.00, 6.00],
        "m_g":  [8.65, 17.30, 25.95, 34.63, 43.31, 51.95]
    }
    df = pd.DataFrame(data)

    cilindros_data = CsvData(df["H_cm"], df["m_g"], xName="H [cm]", yName="m [g]", color="b")

    fig, _ = make_plot(cilindros_data, scatter=True)
    show_plot(fig)
    save_plot(fig, "plots_C1/cilindros.png")


if __name__ == "__main__":
    main()

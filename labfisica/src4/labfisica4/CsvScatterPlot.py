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
        "t": [0.000, 0.200, 0.400, 0.600, 0.800, 1.000],
        "x": [0.000, 0.860, 1.552, 1.944, 1.958, 1.591],
        "v": [4.443, 4.012, 2.801, 1.047, -0.910, -2.691]
    }

    df = pd.DataFrame(data)

    Path("plots4").mkdir(parents=True, exist_ok=True)

    pos_data = CsvData(df["t"], df["x"], xName="Tiempo [s]", yName="Posición tabla 4", color="b")
    fig, _ = make_plot(pos_data, scatter=False)
    show_plot(fig)
    save_plot(fig, "plots4/posicion_tabla4.png")

    vel_data = CsvData(df["t"], df["v"], xName="Tiempo [s]", yName="Velocidad tabla 4", color="r")
    fig, _ = make_plot(vel_data, scatter=False)
    show_plot(fig)
    save_plot(fig, "plots4/velocidad_tabla4.png")


if __name__ == "__main__":
    main()

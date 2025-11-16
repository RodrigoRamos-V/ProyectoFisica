from pathlib import Path
from typing import Tuple

import pandas as pd
import matplotlib.pyplot as plt


class CsvData:
    """Clase simple para usar con make_plot"""
    def __init__(self, x, y, xName="x", yName="y"):
        self.x = x
        self.y = y
        self.xName = xName
        self.yName = yName


def make_plot(data) -> Tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(data.x, data.y, marker='o')
    ax.set_title(f"{data.yName} vs {data.xName}")
    ax.set_xlabel(data.xName)
    ax.set_ylabel(data.yName)
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
    fig.tight_layout()
    return fig, ax


def show_plot(fig: plt.Figure) -> None:
    plt.show()


def save_plot(fig: plt.Figure, filename: str | Path) -> None:
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(filename, format="png", dpi=150)


def main() -> None:
    import sys
    if len(sys.argv) < 2:
        print("Usage: poetry run python src/labfisica/CsvScatterPlot.py <file.csv>")
        sys.exit(2)

    csv_path = Path(sys.argv[1])
    df = pd.read_csv(csv_path)

    # Posición vs Tiempo
    pos_data = CsvData(df["t"], df["x"], xName="Tiempo [s]", yName="Posición [m]")
    fig, _ = make_plot(pos_data)
    show_plot(fig)
    save_plot(fig, "plots/posicion_vs_tiempo.png")

    # Velocidad vs Tiempo
    vel_data = CsvData(df["t"], df["v"], xName="Tiempo [s]", yName="Velocidad [m/s]")
    fig, _ = make_plot(vel_data)
    show_plot(fig)
    save_plot(fig, "plots/velocidad_vs_tiempo.png")


if __name__ == "__main__":
    main()

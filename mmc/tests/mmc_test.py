from __future__ import annotations
from typing import List
from pydantic import BaseModel, model_validator
import csv

class MMC(BaseModel):
    x: List[float] 
    y: List[float]

    n: int = 0
    sum_x: float = 0.0
    sum_y: float = 0.0
    sum_x2: float = 0.0
    sum_xy: float = 0.0
    delta: float = 0.0
    A: float = 0.0
    B: float = 0.0
    sigma2: float = 0.0 
    A_err: float = 0.0 
    B_err: float = 0.0 

    @model_validator(mode="after")
    def _initialize(self) -> "MMC":
        if len(self.x) != len(self.y):
            raise ValueError("x and y must have same length")
        self.n = len(self.x)
        self._sums()
        self._delta()
        self._coeffB()
        self._coeffA()
        self._sigma2()
        self._coeffA_err()
        self._coeffB_err()
        return self

    def _sums(self):
        self.sum_x = sum(self.x)
        self.sum_y = sum(self.y)
        self.sum_x2 = sum(xi**2 for xi in self.x)
        self.sum_xy = sum(xi*yi for xi, yi in zip(self.x, self.y))

    def _delta(self):
        self.delta = self.n * self.sum_x2 - self.sum_x**2

    def _coeffB(self):
        self.B = (self.n * self.sum_xy - self.sum_x * self.sum_y) / self.delta

    def _coeffA(self):
        self.A = (self.sum_y * self.sum_x2 - self.sum_x * self.sum_xy) / self.delta

    def _sigma2(self):
        self.sigma2 = sum((yi - (self.A + self.B*xi))**2 for xi, yi in zip(self.x, self.y)) / (self.n - 2)

    def _coeffA_err(self):
        self.A_err = (self.sigma2 * self.sum_x2 / self.delta)**0.5

    def _coeffB_err(self):
        self.B_err = (self.sigma2 * self.n / self.delta)**0.5

    @classmethod
    def from_csv(cls, file_path: str) -> "MMC":
        
        x_list = []
        y_list = []
        with open(file_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                x_list.append(float(row["x"]))
                y_list.append(float(row["y"]))
        return cls(x=x_list, y=y_list)

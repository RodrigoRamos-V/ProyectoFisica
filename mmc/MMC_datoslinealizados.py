from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field, model_validator
import math

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
        self._coeffA()
        self._coeffB()
        self._sigma2()
        self._coeffA_err()
        self._coeffB_err()
        return self

    def _sums(self):
        self.sum_x = sum(self.x)
        self.sum_y = sum(self.y)
        self.sum_x2 = sum(xi * xi for xi in self.x)
        self.sum_xy = sum(self.x[i] * self.y[i] for i in range(self.n))

    def _delta(self):
        self.delta = self.n * self.sum_x2 - (self.sum_x ** 2)

    def _coeffA(self):
        self.A = (self.sum_x2 * self.sum_y - self.sum_x * self.sum_xy) / self.delta

    def _coeffB(self):
        self.B = (self.n * self.sum_xy - self.sum_x * self.sum_y) / self.delta

    def _sigma2(self):
        residual_sum = sum((self.y[i] - (self.A + self.B * self.x[i])) ** 2 for i in range(self.n))
        self.sigma2 = residual_sum / (self.n - 2)

    def _coeffA_err(self):
        self.A_err = math.sqrt(self.sigma2 * self.sum_x2 / self.delta)

    def _coeffB_err(self):
        self.B_err = math.sqrt(self.sigma2 * self.n / self.delta)

t = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000]
x = [1.000, 0.951, 0.809, 0.588, 0.309, 0.000]

Xmax = max(x)
Y = [math.acos(xi / Xmax) for xi in x]


mmc = MMC(x=t, y=Y)

print("A =", mmc.A)
print("B =", mmc.B)
print("A_err =", mmc.A_err)
print("B_err =", mmc.B_err)
print("sigma^2 =", mmc.sigma2)

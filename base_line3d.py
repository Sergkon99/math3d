from typing import Callable
from math import *
from base_figure3d import *
from figure3d import *
from utils import *


class Line3D(Figure3D):
    def __init__(
            self,
            f: Callable[[float], Tuple],
            s: float,
            e: float,
            r: float = 1
            ):
        super().__init__()

        t_range = list(frange(s, e, .01))
        for i, t in enumerate(t_range):
            val = f(t)
            # Считаем вектор нормали для окружности
            n = tuple(c2 - c1 for c1, c2 in zip(val, f(t + .1)))
            # Создаем точки на окружности
            circle = generate_circle(val, n, r)
            if self.size[0] == 0:  # Первый ряд точек
                self.add_vertexs(circle)
                continue
            self.add_vertexs(circle)
            cnt = len(circle)
            for j in range(cnt):
                face = (j + cnt * i,
                        (j + cnt * i) + 1,
                        j + cnt * (i - 1) + 1,
                        j + cnt * (i - 1))
                self.add_face(face)


if __name__ == "__main__":
    pass
"""
Содержит некоторые стандартные фигуры в пространстве
"""

from typing import List, Tuple
from base_figure3d import *

SQUEEZING_VALUE = 3/4


class BaseFigure:
    def __init__(self):
        self.figure = None

    def get(self):
        return self.figure


class Tetrahedron(BaseFigure):
    def __init__(
            self,
            a: Point3D,
            b: Point3D,
            c: Point3D,
            d: Point3D,
            r: float = 1,
            only_frame: bool = True
            ):
        """
        Тетраедер
        :param a: вершина основания
        :param b: вершина основания
        :param c: вершина основания
        :param d: вершина тетраедра
        :param r: размер тетраедра
        :param only_frame: только секлет(без граней)
        """
        super().__init__()
        self.figure = Ball(a, r) + Ball(b, r) + Ball(c, r) + Ball(d, r)
        r = r * SQUEEZING_VALUE
        self.figure += Cylinder(a, b, r) + Cylinder(a, c, r) + \
            Cylinder(a, d, r) + Cylinder(b, c, r) + \
            Cylinder(b, d, r) + Cylinder(c, d, r)

        if not only_frame:
            self.figure += Edge(a, b, c) + Edge(a, b, d) + \
                Edge(a, c, d) + Edge(b, c, d)


class Cube(BaseFigure):
    def __init__(self, a: Point3D, e: Point3D, r: float = 1, only_frame: bool = True):
        """
        Куб
        :param a: первая вершина куьа
        :param e: противоположная вершина по диагонали
        :param r: размер куба
        """
        super().__init__()
        # Нижнее основание
        b = (e[0], a[1], a[2])
        c = (e[0], e[1], a[2])
        d = (a[0], e[1], a[2])
        # Верхнее основание
        f = (e[0], a[1], e[2])
        g = (a[0], a[1], e[2])
        h = (a[0], e[1], e[2])

        self.figure = Ball(a, r) + Ball(b, r) + Ball(c, r) + Ball(d, r) +\
            Ball(e, r) + Ball(f, r) + Ball(g, r) + Ball(h, r)
        r = r * SQUEEZING_VALUE
        self.figure += Cylinder(a, b, r) + Cylinder(b, c, r) +\
            Cylinder(c, d, r) + Cylinder(d, a, r) + Cylinder(e, f, r) +\
            Cylinder(f, g, r) + Cylinder(g, h, r) + Cylinder(h, e, r) +\
            Cylinder(b, f, r) + Cylinder(c, e, r) + Cylinder(d, h, r) +\
            Cylinder(a, g, r) + Edge(a, b, c, d) + Edge(e, f, g, h)

        if not only_frame:
            self.figure += Edge(a, b, f, g) + Edge(b, c, e, f) +\
                Edge(c, e, h, d) + Edge(d, h, g, a)


if __name__ == "__main__":
    A = (0, 0, 0)
    B = (5, 0, 0)
    C = (5, 5, 0)
    D = (0, 5, 0)
    E = (5, 5, 5)
    # c1 = Cylinder(B, C, 1, (1, 1, 1), (3, 0, 0), hide=True)
    # c2 = Cylinder(D, E, 1)
    # b = Ball(A, 1)
    # c = c1 + c2
    t = Cube(A, E, .51, False).get()
    t.save_ply("cilllll")

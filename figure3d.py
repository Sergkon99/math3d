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
        :param only_frame: только скелет(без граней)
        """
        super().__init__()
        self.figure = Point(a, r) + Point(b, r) + Point(c, r) + Point(d, r)
        r = r * SQUEEZING_VALUE
        self.figure += Edge(a, b, r) + Edge(a, c, r) + \
            Edge(a, d, r) + Edge(b, c, r) + \
            Edge(b, d, r) + Edge(c, d, r)

        if not only_frame:
            self.figure += Face(a, b, c) + Face(a, b, d) + \
                Face(a, c, d) + Face(b, c, d)


class Cube(BaseFigure):
    def __init__(
            self,
            a: Point3D,
            e: Point3D,
            r: float = 1,
            only_frame: bool = True
            ):
        """
        Куб
        :param a: первая вершина куба
        :param e: противоположная вершина по диагонали
        :param r: размер куба
        :param only_frame: только скелет(без граней)
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

        self.figure = Point(a, r) + Point(b, r) + Point(c, r) + Point(d, r) +\
            Point(e, r) + Point(f, r) + Point(g, r) + Point(h, r)
        r = r * SQUEEZING_VALUE
        self.figure += Edge(a, b, r) + Edge(b, c, r) +\
            Edge(c, d, r) + Edge(d, a, r) + Edge(e, f, r) +\
            Edge(f, g, r) + Edge(g, h, r) + Edge(h, e, r) +\
            Edge(b, f, r) + Edge(c, e, r) + Edge(d, h, r) +\
            Edge(a, g, r)

        if not only_frame:
            self.figure += Face(a, b, c, d) + Face(e, f, g, h) +\
                Face(a, b, f, g) + Face(b, c, e, f) + Face(c, e, h, d) +\
                Face(d, h, g, a)


if __name__ == "__main__":
    A = (0, 0, 0)
    B = (5, 0, 0)
    C = (5, 5, 0)
    D = (0, 5, 0)
    E = (5, 5, 5)
    # c1 = Edge(B, C, 1, (1, 1, 1), (3, 0, 0), hide=True)
    # c2 = Edge(D, E, 1)
    # b = Point(A, 1)
    # c = c1 + c2
    t = Cube(A, E, .51, False).get()
    t.save_ply("cilllll")

"""
Содержит базовые фигуры в пространстве
"""
import os
from typing import List, Tuple
from math import sqrt, sin, cos, pi
from utils import *

# Точка в пространстве
Point3D = Tuple[float, float, float]
# Вектор в пространстве
Vector3D = Point3D
# Грань в пространтсве - список номеров вершин
Face3D = Tuple


class Figure3D:
    def __init__(
            self,
            vertexs: List[Point3D] = None,
            faces: List[Face3D] = None,
            hide: bool = False
            ):
        """
        Базовый класс фигуры в пространстве.
        :param vertexs: список вершин
        :param faces: список граней,
                      каждая грань описана порядковыми номерами вершнин
        :param hide: признок скрытой фигуры, такие фигуры игнорируются
                     при сложении и не выводятся в финальный в файл
        """
        self._vertexs = vertexs or []
        self._faces = faces or []
        self.hide = hide

    def add_vertex(self, vertex: Point3D) -> None:
        """
        Добавление вершины к фигуре
        :param vertex: вершина
        """
        if self.hide:
            return
        self._vertexs.append(vertex)

    def add_face(self, face: Face3D) -> None:
        """
        Добавление грани к фигуре
        :param face: грань
        """
        if self.hide:
            return
        self._faces.append(face)

    def add_vertexs(self, vertexs: List[Point3D]) -> None:
        """
        Добавление списка вершин к фигуре
        :param vertexs: список вершин
        """
        for vertex in vertexs:
            self.add_vertex(vertex)

    def add_faces(self, faces: List[Face3D]) -> None:
        """
        Добавление списка граней к фигуре
        :param faces: список граней
        """
        for face in faces:
            self.add_face(face)

    def get_vertexs(self) -> List[Point3D]:
        """
        Получение списка вершин фигуры
        :return: список вершин
        """
        return self._vertexs[:]

    def get_faces(self) -> List[Face3D]:
        """
        Получение списка граней фигуры
        :return: список граней
        """
        return self._faces[:]

    @property
    def size(self) -> Tuple[int, int]:
        """
        Список вершин и граней фигуры
        """
        return len(self._vertexs), len(self._faces)

    def __add__(self, other: "Figure3D") -> "Figure3D":
        """
        Сложение фигур. Добавление вершин и граней к текущей фигуре
        :param other: другая фигура - наследник класса Figure3D
        """
        if not isinstance(other, Figure3D):
            raise ValueError("Нельзя складывать классы отличные от Figure3D")
        f = Figure3D(self.get_vertexs(), self.get_faces())
        sz = f.size
        added_vertexs = other.get_vertexs()
        added_faces = other.get_faces()
        # Перенумермуем вершины для добавления
        added_faces = [
            tuple(
                map(lambda x: x + sz[0], faces)
            )
            for faces in added_faces
        ]
        f.add_faces(added_faces)
        f.add_vertexs(added_vertexs)
        return f

    def generate_ply(self) -> str:
        """
        Генерация строки в ply формате на основе вершин и граней текущей фигуры
        """
        header = "ply\n" \
                 "format ascii 1.0\n" \
                 "element vertex {cnt_vertex}\n" \
                 "property float x\n" \
                 "property float y\n" \
                 "property float z\n" \
                 "element face {cnt_face}\n" \
                 "property list uchar int vertex_index\n" \
                 "end_header\n".format(
                     cnt_vertex=self.size[0],
                     cnt_face=self.size[1]
                 )

        return header + \
            "\n".join(" ".join(map(str, row)) for row in self._vertexs) + \
            "\n" + \
            "\n".join(str(len(row)) + " " +
                      " ".join(map(str, row)) for row in self._faces)

    def save_ply(self, file_name):
        """
        Создание ply-файла фигуры
        :param file_name: название файла
        """
        file_path = os.path.join(os.getcwd(), "ply", file_name + ".ply")
        with open(file_path, "w") as f:
            f.write(self.generate_ply())


class Ball(Figure3D):
    def __init__(self, a, r, hide=False):
        """
        Шар
        :param a: центр шара
        :param r: радиус шара
        :param hide: признак скрытой фигуры
        """
        super().__init__(hide=hide)
        tetha_range = list(frange(0, pi, .1))
        fi_range = list(frange(0, 2*pi, .1))
        cnt = None
        for t in tetha_range:
            x = [a[0] + r * sin(t) * cos(fi) for fi in fi_range]
            y = [a[1] + r * sin(t) * sin(fi) for fi in fi_range]
            z = [a[2] + r * cos(t) for fi in fi_range]
            cnt = len(x)
            self.add_vertexs([(x_, y_, z_) for x_, y_, z_ in zip(x, y, z)])

        # Добавим грани
        for i in range(self.size[0] - cnt):
            face = (i,
                    (i + cnt),
                    (i + cnt + 1) % self.size[0],
                    i + 1)
            self.add_face(face)


class Face(Figure3D):
    def __init__(self, *points, hide=False):
        """
        Грань
        :params: принимает любое кол-во точек Point3D для задание грани
        """
        super().__init__(hide=hide)

        for point in points:
            if type(point) != tuple:
                raise ValueError(
                    f"Тип переданного элемента не соответсвует формату. \
                    {type(point)} != {tuple}")
        self.add_vertexs(points)
        self.add_face(list(range(len(points))))


class Cylinder(Figure3D):
    def __init__(
            self,
            a: Point3D,
            b: Point3D,
            r: float,
            n1: Vector3D = None,
            n2: Vector3D = None,
            hide: bool = False
            ):
        """
        Цилиндр.
        :param a: центр первого основания цилиндра
        :param b: центр второго основания цилиндра
        :param r: радиус оснований цилиндра
        :param n1: вектор нормали к первому основанию
        :param n2: вектор нормали ко аторому основанию
        :param hide: признак скрытой фигуры
        """
        super().__init__(hide=hide)

        n = None
        # Считаем общий вектор нормали, если они не заданы
        if n1 is None and n2 is None:
            n = tuple(c2 - c1 for c1, c2 in zip(a, b))

        l1 = generate_circle(a, n if n is not None else n1, r)
        l2 = generate_circle(b, n if n is not None else n1, r)

        self.add_vertexs(l1)
        self.add_vertexs(l2)

        # Схема грани
        # i+cnt----i+cnt+1
        #   |         |
        #   |         |
        #   |         |
        #   |         |
        #   i--------i+1
        cnt = len(l1)
        for i in range(cnt):
            face = (i,
                    (i + cnt),
                    (i + cnt + 1) % (2 * cnt),
                    i + 1)
            self.add_face(face)
        self.add_face(tuple(range(cnt)) + (0,))
        self.add_face(tuple(map(lambda x: x + cnt, range(cnt))) + (0,))


Point = Ball
Edge = Cylinder

if __name__ == "__main__":
    pass

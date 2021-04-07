from typing import List, Tuple
from functools import partial
from operator import add


class Figure3D:
    def __init__(self, vertexs: List[Tuple] = None, faces: List[Tuple] = None):
        # Список вершин
        # Каждая вершина - кортеж из 3-х элементов (x, y, z)
        self._vertexs = vertexs or []
        # Список граней
        # Каждая грань содержит порядковый номер вершин на которох построена
        self._faces = faces or []

    def add_vertex(self, vertex: Tuple):
        self._vertexs.append(vertex)

    def add_face(self, face: Tuple):
        self._faces.append(face)

    def add_vertexs(self, vertexs: List[Tuple]):
        for vertex in vertexs:
            self.add_vertex(vertex)

    def add_faces(self, faces: List[Tuple]):
        for face in faces:
            self.add_face(face)

    def get_vertexs(self):
        return self._vertexs[:]

    def get_faces(self):
        return self._faces[:]

    @property
    def size(self):
        # Врнет размер - кол-во веришин и граней
        return len(self._vertexs), len(self._faces)

    def __add__(self, other):
        f = Figure3D(self.get_vertexs(), self.get_faces())
        sz = f.size
        added_vertexs = other.get_vertexs()
        added_faces = other.get_faces()
        added_faces = [
            tuple(
                map(lambda x: x + sz[0], faces)
            )
            for faces in added_faces
        ]
        f.add_faces(added_faces)
        f.add_vertexs(added_vertexs)
        return f

    def generate_ply(self):
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
        with open(file_name + ".ply", "w") as f:
            f.write(self.generate_ply())


class Tetrahedron(Figure3D):
    def __init__(self, a, b, c, d):
        super().__init__()
        # задайм вершины
        self.add_vertex(a)
        self.add_vertex(b)
        self.add_vertex(c)
        self.add_vertex(d)
        # задаем ребра
        self.add_face((0, 1, 2))
        self.add_face((0, 2, 3))
        self.add_face((0, 1, 3))
        self.add_face((1, 2, 3))


class Cube(Figure3D):
    def __init__(self, a, b, c, d, e, f, g, h):
        super().__init__()
        # задайм вершины
        self.add_vertex(a)
        self.add_vertex(b)
        self.add_vertex(c)
        self.add_vertex(d)
        self.add_vertex(e)
        self.add_vertex(f)
        self.add_vertex(g)
        self.add_vertex(h)
        # задаем ребра
        self.add_face((0, 1, 2, 3))
        self.add_face((7, 6, 5, 4))
        self.add_face((0, 4, 5, 1))
        self.add_face((1, 5, 6, 2))
        self.add_face((2, 6, 7, 3))
        self.add_face((3, 7, 4, 0))

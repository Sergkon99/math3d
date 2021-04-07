class Figure3D:
    def __init__(self):
        self._vertexs = []
        self._faces = []

    def _faces_offset(self, n):
        for i, face in enumerate(self._faces):
            self._faces[i] = (face[j] + n for j in range(1, len(face)))

    def add_vertex(self, *args):
        self._vertexs.append(tuple(args))

    def add_vertexs(self, vertexs):
        for vertex in vertexs:
            self.add_vertex(*vertex)

    def add_face(self, *args):
        self._faces.append((len(args), *args))

    def add_faces(self, faces):
        raise RuntimeError("Fix this")
        for face in faces:
            self.add_face(*face)

    def __add__(self, other):
        f = Figure3D()
        f._vertexs.extend(self._vertexs)
        f._vertexs.extend(other._vertexs)
        f._faces.extend(self._faces)
        # смещение для правильного отображения граней
        n = len(self._vertexs)
        new_other_faces = []
        for i, face in enumerate(other._faces[:]):
            new_other_faces.append(
                (face[0], *(face[j] + n for j in range(1, len(face))))
            )
        f._faces.extend(new_other_faces)
        return f

    def generate_ply(self):
        return f"""
            ply
            format ascii 1.0
            element vertex {len(self._vertexs)}
            property float x
            property float y
            property float z
            element face {len(self._faces)}
            property list uchar int vertex_index
            end_header
        """ + \
            "\n".join(" ".join(map(str, row)) for row in self._vertexs) + \
            "\n" + \
            "\n".join(" ".join(map(str, row)) for row in self._faces)

    def save_ply(self, file_name):
        with open(file_name + ".ply", "w") as f:
            f.write(self.generate_ply())


class Tetrahedron(Figure3D):
    def __init__(self, a, b, c, d):
        super().__init__()
        # задайм вершины
        self.add_vertex(*a)
        self.add_vertex(*b)
        self.add_vertex(*c)
        self.add_vertex(*d)
        # задаем ребра
        self.add_face(0, 1, 2)
        self.add_face(0, 2, 3)
        self.add_face(0, 1, 3)
        self.add_face(1, 2, 3)


class Cube(Figure3D):
    def __init__(self, a, b, c, d, e, f, g, h):
        super().__init__()
        # задайм вершины
        self.add_vertex(*a)
        self.add_vertex(*b)
        self.add_vertex(*c)
        self.add_vertex(*d)
        self.add_vertex(*e)
        self.add_vertex(*f)
        self.add_vertex(*g)
        self.add_vertex(*h)
        # задаем ребра
        self.add_face(0, 1, 2, 3)
        self.add_face(7, 6, 5, 4)
        self.add_face(0, 4, 5, 1)
        self.add_face(1, 5, 6, 2)
        self.add_face(2, 6, 7, 3)
        self.add_face(3, 7, 4, 0)


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


def generate_ply():
    t = Tetrahedron(
        (1, 1, 0),
        (2, 0, 0),
        (1, 0, 0),
        (1, 0, 1)
    )
    c = Cube(
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (0, 1, 0),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 1),
        (1, 1, 0)
    )
    f = c + t
    t.save_ply("Tetrahedron")
    c.save_ply("Cube")
    f.save_ply("Figure")


generate_ply()

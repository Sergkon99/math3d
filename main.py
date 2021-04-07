from figure3d import *


if __name__ == "__main__":
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

from figure3d import *


if __name__ == "__main__":
    # t = Tetrahedron(
    #     (1, 1, 0),
    #     (2, 0, 0),
    #     (1, 0, 0),
    #     (1, 0, 1)
    # )
    # c = Cube(
    #     (0, 0, 0),
    #     (0, 0, 1),
    #     (0, 1, 1),
    #     (0, 1, 0),
    #     (1, 0, 0),
    #     (1, 0, 1),
    #     (1, 1, 1),
    #     (1, 1, 0)
    # )
    # f = c + t
    # t.save_ply("Tetrahedron")
    # # c.save_ply("Cube")
    # f.save_ply("Figure")

    c1 = Cylinder((0, 0, 0), (3, 9, 2), 1)
    c2 = Cylinder((3, 9, 2), (9, 9, 2), 1)
    c3 = Cylinder((9, 9, 2), (10, 9, 0), 1)
    c = c1 + c2 + c3
    c.save_ply("Cylinder2")

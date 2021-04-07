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

    c1 = Cylinder((0, 0, 0), (5, 0, 0), .1)
    c2 = Cylinder((0, 0, 0), (1, 5, 0), .1)
    c3 = Cylinder((1, 5, 0), (6, 5, 0), .1)
    c4 = Cylinder((5, 0, 0), (6, 5, 0), .1)
    c5 = Cylinder((5, 0, 0), (0, 0, 5), .1)
    c6 = Cylinder((6, 5, 0), (0, 0, 5), .1)
    c7 = Cylinder((1, 5, 0), (0, 0, 5), .1)
    c8 = Cylinder((0, 0, 0), (0, 0, 5), .1)
    b1 = Ball((0, 0, 5), .2)
    b2 = Ball((0, 0, 0), .2)
    b3 = Ball((5, 0, 0), .2)
    b4 = Ball((6, 5, 0), .2)
    b5 = Ball((1, 5, 0), .2)
    e1 = Edge((0, 0, 0), (0, 0, 5), (1, 5, 0))
    e2 = Edge((0, 0, 0), (1, 5, 0), (6, 5, 0), (5, 0, 0))
    c = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + b1 + b2 + b5 + b3 + b4 + e1 + e2
    c.save_ply("Figgg")

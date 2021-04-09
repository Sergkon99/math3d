from figure3d import *
from base_figure3d import *


if __name__ == "__main__":
    A = (0, 0, 0)
    B = (5, 0, 0)
    C = (5, 5, 0)
    D = (0, 5, 0)
    E = (0, 0, 5)
    F = (5, 5, 5)

    t = Tetrahedron(A, B, C, E, .2, only_frame=False).get()
    t.save_ply("Tetrahedron")

    c = Cube(A, F).get()
    c.save_ply("Cube")

    c1 = Cylinder(A, B, .1)
    c2 = Cylinder(A, D, .1)
    c3 = Cylinder(D, C, .1)
    c4 = Cylinder(B, C, .1)
    c5 = Cylinder(B, E, .1)
    c6 = Cylinder(C, E, .1)
    c7 = Cylinder(D, E, .1)
    c8 = Cylinder(A, E, .1)
    b1 = Ball(E, .2)
    b2 = Ball(A, .2)
    b3 = Ball(B, .2)
    b4 = Ball(C, .2)
    b5 = Ball(D, .2)
    e1 = Face(A, E, D)
    e2 = Face(A, B, E)
    e3 = Face(B, E, C, hide=True)
    e4 = Face(C, E, D)
    e5 = Face(A, D, C, B)
    c = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 +\
        b1 + b2 + b5 + b3 + b4 +\
        e1 + e2 + e3 + e4 + e5
    c.save_ply("Figure")

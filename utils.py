from math import *


def frange(x, y, jump):
    while x < y:
        yield x
        x += jump
    yield y


def generate_circle(
        p,
        n,
        r
        ):
    """
    Генерация точек на окружности
    :param p: центр окружности
    :param n: нормаль к плоскости в которой лежит окружность
    :param r: радиус окружности
    """
    # Коэфиценты ур-ия прямой
    A, B, C = n

    t_range = list(frange(0, 2 * pi, .1))
    if A**2 + C**2 < 0.001:
        x = [p[0] + r * cos(t) for t in t_range]
        y = [p[1] for t in t_range]
        z = [p[2] + r * sin(t) for t in t_range]
        return [(x_, y_, z_) for x_, y_, z_ in zip(x, y, z)]
    x = [
        p[0] + r / sqrt(A**2 + C**2) * (C * cos(t) - A * B * sin(t) / sqrt(A**2 + B**2 + C**2))
        for t in t_range
    ]
    y = [
        p[1] + r * sqrt(A**2 + C**2) / sqrt(A**2 + B**2 + C**2) * sin(t)
        for t in t_range
    ]
    z = [
        p[2] - r / sqrt(A**2 + C**2) * (A * cos(t) + B * C * sin(t) / sqrt(A**2 + B**2 + C**2))
        for t in t_range
    ]
    return [(x_, y_, z_) for x_, y_, z_ in zip(x, y, z)]
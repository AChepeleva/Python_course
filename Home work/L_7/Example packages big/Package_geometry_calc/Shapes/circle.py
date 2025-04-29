# Функции для вычисления площади и периметра круга.

import math

def cir_perimeter(r):
    """Вычисление длины окружности."""
    P_cir = 2 * math.pi * r
    return round(P_cir, 2)


def cir_area(r):
    """Вычисление площади круга."""
    S_cir =  math.pi * r ** 2
    return round(S_cir, 2)

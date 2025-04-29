# Функции с  различными действиями на введенными числами.

def sum_values(value1, value2):
    return value1 + value2


def quotient_values(value1, value2):
    if value2 == 0:
        return "Ошибка - деление на ноль!"
    return value1 / value2


def max_value(value1, value2):
    return max(value1, value2)


def min_value(value1, value2):
    return min(value1, value2)

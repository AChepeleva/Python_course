# Функции для ввода данных.

def input_positive_float(promt):
    """Функция для проверки ввода положительного числа."""
    while True:
        try:
            value = float(input(promt))
            if value <= 0:
                print("Ошибка: значение должно быть больше нуля!")
                continue
            return value
        except ValueError:
            print("Ошибка: введите числовое значение!")

def input_triangle():
    """Функция для ввода сторон треугольника.
    В результате возвращается кортеж."""
    a = input_positive_float("Длина стороны a (см) = ")
    b = input_positive_float("Длина стороны b (см) = ")
    c = input_positive_float("Длина стороны c (см) = ")

    # Дополнительная проверка на существование такого треугольника.
    if a + b <= c or a + c <= b or b + c <= a:
        print("Ошибка: такого треугольника не существует!")
        return input_triangle()

    return a, b, c


def input_square():
    """Функция для ввода стороны квадрата.
    В результате возвращается число."""
    a = input_positive_float("Длина стороны (см) = ")
    return a


def input_rectangle():
    """Функция для ввода сторон прямоугольникаю
     В результате возвращается кортеж."""
    a = input_positive_float("Длина стороны a (см) = ")
    b = input_positive_float("Длина стороны b (см) = ")
    return a, b


def input_circle():
    """Функция для ввода радиуса круга.
     В результате возвращается число."""
    r = input_positive_float("Радиус (см) = ")
    return r

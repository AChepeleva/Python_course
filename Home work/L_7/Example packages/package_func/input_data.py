# Модуль с функциями для 

def get_input_data():
    """Функция для ввода целлого числа и проверки ввода."""
    while True:
        try:
            value1 = int(input("Введите целое число1: "))
            value2 = int(input("Введите целое число2: "))
            return value1, value2
        except ValueError:
            print("Ошибка ввода! Ввведите целые числа.")

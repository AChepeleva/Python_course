# Проверка выбора площади или периметра.

def chose_operation():
    """Функция для выбора операции"""
    operation = input("1 - Периметр, 2 -Площадь --> ")
    return operation

def validate_operation_input():
    """Функция проверяет ввод операции (1 - периметр, 2 - площадь)."""
    while True:
        operation = chose_operation().strip()
        if operation in ('1', '2'):
            return operation
        print("Ошибка: введите 1 или 2!")

def print_result(shape, operation, result):
    """Функция выводит результат вычислений."""
    units = "см" if "Периметр" in operation or "Длина" in operation else "см^2"
    print("--------------------------------")
    print(f"{operation} {shape.lower()}: {result} {units}")
    print("--------------------------------")


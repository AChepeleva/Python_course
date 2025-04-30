
from package_func.input_data import get_input_data
from package_func.operations import sum_values, quotient_values, max_value, min_value
from package_func.stat import add_data, show_data


def main():
    msg = """1 - сумма
    2 - частное
    3 - найти максимум
    4 - найти минимум
    5 - спиок
    -1 - закончить """

    operation = input(msg)

    while operation != "-1":
        match operation:
            case "1":
                value1, value2 = get_input_data()
                result = sum_values(value1, value2)
                print(f"Сумма: {result}")
                add_data(f"{value1} + {value2}", result)
            case "2":
                value1, value2 = get_input_data()
                result = quotient_values(value1, value2)
                print(f"Частное: {result}")
                add_data(f"{value1} / {value2}", result)
            case "3":
                value1, value2 = get_input_data()
                result = max_value(value1, value2)
                print(f"Максимум: {result}")
                add_data(f"max({value1}, {value2})", result)
            case "4":
                value1, value2 = get_input_data()
                result = min_value(value1, value2)
                print(f"Минимум: {result}")
                add_data(f"min({value1}, {value2})", result)
            case "5":
                print("Сделанные вычисления:5")
                show_data()
            case _:
                print("Извини, не понял.")
        operation = input(msg)

main()

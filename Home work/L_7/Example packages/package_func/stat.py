# Сохранение вычислений в словарь.

data_list = []

def add_data(operation, result):
    data_list.append({"Выражение": operation, "Результат": result})


def show_data():
    if not data_list:
        print("Вычислений еще не было.")
    else:
        for entry in data_list:
            print(f"Выражение: {entry['Выражение']}, Результат: {entry['Результат']}")

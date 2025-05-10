# Журнал запросов.

my_journal = []

def add_to_journal(shape, operation, result):
    """Функция добавления запроса в журнал."""
    units = "см" if "Периметр" in operation or "Длина" in operation else "см^2"
    my_journal.append({"shape": shape, "operation": operation, "result": result, "units": units})


def clear_journal():
    """Функция очищает весь журнал запросов."""
    del my_journal[:]
    return "Журнал успешно очищен."


def get_my_journal():
    """Возвращает журнал запросов."""
    return my_journal

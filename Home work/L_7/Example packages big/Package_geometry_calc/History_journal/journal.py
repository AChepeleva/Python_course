# Журнал запросов.

my_journal = []

def add_to_journal(shape, operation, result):
    """Функция добавления запроса в журнал."""
    my_journal.append({"shape": shape, "operation": operation, "result": result})


def get_my_journal():
    """Возвращает журнал запросов."""
    return my_journal
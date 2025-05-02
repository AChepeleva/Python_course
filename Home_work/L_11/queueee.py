
class EmptyQueError(Exception):
    """очередь пуста"""
    pass


class Que:
    def __init__(self):
        self.__que = []
        print("очередь создана")
    def put(self, num):
        self.__que.append(num)
        print("успешно добавдено")
        print("текущее значение оцереди", self.__que)
        print()
    def get(self):
        if len(self.__que) < 1:
            raise EmptyQueError
        del self.__que[0]
        print("успешно удалено")
        print("текущее значение оцереди", self.__que)
        print()


q1 = Que()

for i in range(5):
    q1.put(i)


for i in range(6):
    q1.get()



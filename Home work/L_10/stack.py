
class Stack:
    def __init__(self):
        self.__stack = []
        print("stack OK")
    def push(self, value):
        self.__stack.append(value)
        print(value,"OK")
    def pop(self):
        try:
            print(self.__stack.pop(),"del Ok")
        except:
            print("pusto")
    def stat(self):
        print("tekushee sostoanie:")
        print(self.__stack)

        
class AddstackVal(Stack):
    def __init__(self):
        super().__init__()
        self.__summa = 0
    def push(self, value):
        super().push(value)
        self.__summa += value
    def get_sum(self):
        print(self.__summa)


        
# s2 = AddstackVal()
# s2.get_sum()
# s2.stat()
# s2.push(33)
# s2.push(2)
# s2.stat

from package_classes.task_class import Task
from package_classes.exceptions import BadIdError, BadNameError, BadPriorityError


class TodoList:
    __auto_id = 1

    def __init__(self):
        self.__task_storage: dict[Task] = {}

    @classmethod
    def incrId(cls):
        cls.__auto_id +=1

    @classmethod
    def getId(cls):
        return cls.__auto_id
    
    def create(self, name, priority):
        """Метод для добавленя задачи в хранилище."""
        if len(name) < 7:
            raise BadNameError(name, "Имя должно быть более 7 символов!")
        
        if priority < 1 or priority > 100:
            raise BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100!")
        
        self.__task_storage.update({TodoList.getId(): Task(name, priority)})
        TodoList.incrId()
        return True
    

    def read(self, tid) -> Task:
        """Метод для чтения задачи по id."""
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")
        
        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи не содержится!")


    def read_all(self):
        """Метод для чтения всех задачь."""
        res_str = "номер задачи: значение\n"
        
        for k, v in self.__task_storage.items():
            res_str += f"{k} | {v}\n"

        return res_str
    

    def update(self, tid, name, priority):
        """Метод для обновления задачи в хранилище."""
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")
        
        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи не содержится!")
        
        if len(name) < 7:
            raise BadNameError(name, "Имя должно быть более 7 символов!")
        
        if priority < 1 or priority > 100:
            raise BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100!")
        
        self.__task_storage.update({tid: Task(name, priority)})

        return True
    

    def delete(self, tid):
        """Метод для удаления задачи по id"""
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")
        
        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи не содержится!")
        
        self.__task_storage.pop(tid)

        return True
    

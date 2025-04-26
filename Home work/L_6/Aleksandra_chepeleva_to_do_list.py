def create_task():
    """Функция для создания задания."""
    global task_auto_id
    t_name = input("Дай имя задачи:")
    t_status = False
    task_list[task_auto_id] = {"task_name":t_name,"status":False}
    task_auto_id += 1
    return True


def show_tasks():
    """Функция для отображения всех заданий"""
    print("show tasks")
    for task_id, desc in task_list.items():
        print("______________")
        print(f"Task id: {task_id}")
        for key, value in desc.items():
            print("\t",key, value)
        print("______________")


def change_status():
    """Функция для изменения сатуса задания"""
    task_id = int(input("Give me programm number:"))
    if task_id not in task_list:
        return False
    inside = task_list.get(task_id)
    inside["status"] = True
    task_list.update({task_id:inside})


def main():
    msg = """1 - new tasks
    2 - show tasks
    3 - change task status
    quit - exit from programm
    """
    oper = input(msg)

    while oper != "quit":
        match oper:
            case "1":
                create_task()
            case "2":
                show_tasks()
            case "3":
                change_status()
            case _:
                print("Sorry, ne ponial")
        oper = input(msg)


task_list = {}
task_auto_id = 1
main()



# добавить 
#документацию
#улучшить вывод
#структурировать код
Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#class work continue


# to do list


task_list = {}
#task_list[task_id] = {task_name:task_name, status:status}
#task_list[task_id] = {"task_name":"task_name", "status":status - bool}
di = {}
di[1] = {"task_name":"go to schoo", "status":False}
di
{1: {'task_name': 'go to schoo', 'status': False}}
di[1]
{'task_name': 'go to schoo', 'status': False}

task_auto_id = 1
def create_task():
    t_name = input("Дай имя задачи:")
    t_status = False
    task_list[task_auto_id] = {"task_name":t_name,"status":False}

    
task_list
{}
create_task()
Дай имя задачи:wsdfg
def create_task():
    t_name = input("Дай имя задачи:")
    t_status = False
    task_list[task_auto_id] = {"task_name":t_name,"status":False}
    return True

create_task()
Дай имя задачи:sdf
True


task_uato_id
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    task_uato_id
NameError: name 'task_uato_id' is not defined. Did you mean: 'task_auto_id'?
task_auto_id
1
def create_task():
    t_name = input("Дай имя задачи:")
    t_status = False
    task_list[task_auto_id] = {"task_name":t_name,"status":False}
    task_auto_id += 1
    return True

def create_task():
    global task_auto_id
    t_name = input("Дай имя задачи:")
    t_status = False
    task_list[task_auto_id] = {"task_name":t_name,"status":False}
    task_auto_id += 1
    return True

create_task()
Дай имя задачи:asdf
True
create_task()
Дай имя задачи:asdfghjk4567
True
task_auto_id
3




task-list
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    task-list
NameError: name 'task' is not defined
task_list
{1: {'task_name': 'asdf', 'status': False}, 2: {'task_name': 'asdfghjk4567', 'status': False}}
def show_tasks:
    
SyntaxError: expected '('
def show_tasks():
    print("show tasks")
    for tusk_id, desc in task_list.item()
    
SyntaxError: expected ':'
def show_tasks():
    print("show tasks")
    for tusk_id, desc in task_list.items():
        print("______________")
        print("Task id: {task_id}")
        for key, value in desc.items():
            print("\t",key, value)
        print("______________")

        
show_tasks()
show tasks
______________
Task id: {task_id}
	 task_name asdf
	 status False
______________
______________
Task id: {task_id}
	 task_name asdfghjk4567
	 status False
______________


def show_tasks():
    print("show tasks")
    for task_id, desc in task_list.items():
        print("______________")
        print("Task id: {task_id}")
        for key, value in desc.items():
            print("\t",key, value)
        print("______________")

        

show_tasks()
show tasks
______________
Task id: {task_id}
	 task_name asdf
	 status False
______________
______________
Task id: {task_id}
	 task_name asdfghjk4567
	 status False
______________
def show_tasks():
    print("show tasks")
    for task_id, desc in task_list.items():
        print("______________")
        print(f"Task id: {task_id}")
        for key, value in desc.items():
            print("\t",key, value)
        print("______________")

        
show_tasks()
show tasks
______________
Task id: 1
	 task_name asdf
	 status False
______________
______________
Task id: 2
	 task_name asdfghjk4567
	 status False
______________

def change_status(:
                  
SyntaxError: invalid syntax
def change_status():
    task_id = int(input("Give me programm number:"))
    if task_id not in task_list:
        return False
    inside = task_list.get(task_id)
    inside["status"] = True
    task_list.update({task_id:inside})

    
show_tasks()
show tasks
______________
Task id: 1
	 task_name asdf
	 status False
______________
______________
Task id: 2
	 task_name asdfghjk4567
	 status False
______________
change_status()
Give me programm number:2
change_status()
Give me programm number:6
False
change_status()
Give me programm number:2
task_list
{1: {'task_name': 'asdf', 'status': False}, 2: {'task_name': 'asdfghjk4567', 'status': True}}






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


main()
1 - new tasks
    2 - show tasks
    3 - change task status
    quit - exit from programm
    2
show tasks
______________
Task id: 1
	 task_name asdf
	 status False
______________
______________
Task id: 2
	 task_name asdfghjk4567
	 status True
______________
1 - new tasks
    2 - show tasks
    3 - change task status
    quit - exit from programm
    1
Дай имя задачи:asdfg
1 - new tasks
    2 - show tasks
    3 - change task status
    quit - exit from programm
    2
show tasks
______________
Task id: 1
	 task_name asdf
	 status False
______________
______________
Task id: 2
	 task_name asdfghjk4567
	 status True
______________
______________
Task id: 3
	 task_name asdfg
	 status False
______________
1 - new tasks
    2 - show tasks
    3 - change task status
    quit - exit from programm
    3
Give me programm number:1
1 - new tasks
    2 - show tasks
    3 - change task status
    quit - exit from programm
    2
show tasks
______________
Task id: 1
	 task_name asdf
	 status True
______________
______________
Task id: 2
	 task_name asdfghjk4567
	 status True
______________
______________
Task id: 3
	 task_name asdfg
	 status False
______________
1 - new tasks
    2 - show tasks
    3 - change task status
    quit - exit from programm
    quite
Sorry, ne ponial
1 - new tasks
    2 - show tasks
    3 - change task status
    quit - exit from programm
    quit



>>> import calendar as c
>>> c.isleap(2000)
True
>>> c.isleap(2020)
True
>>> import random as r
>>> r.randin(1,5)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    r.randin(1,5)
AttributeError: module 'random' has no attribute 'randin'. Did you mean: 'randint'?
>>> r.randint(1,5)
5
>>> r.randint(1,500)
441
>>> 
>>> 

>>> secret = r.randint(1,5)
>>> my_number = int(input("give number 1-5"))
give number 1-52
>>> my_number == secret
False
>>> secret = r.randint(1,3)
>>> my_number = 2
>>> my_number == secret
... 
False
>>> secret = r.randint(1,3)
... 
>>> my_number = 1
>>> my_number == secret
... 
False
>>> 
>>> 
>>> 

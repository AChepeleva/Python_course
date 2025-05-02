Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.



from abc import ABC, abstractmethod




# MRO

class A:
    a = 1
    def __init__(self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B(A):
    b = 2
    def __init__(self):
        self.bb = 22
    def fun_b(self):
        return "fun_b"

    
class C:
    c = 3
    def __init__(self):
        self.cc = 33
    def fun_c(self):
        return "fun_c"

    
c_inst = C()
c_inst.cc
33
c_inst.c
3
c_inst.fun_c()
'fun_c'
c_inst.b
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c_inst.b
AttributeError: 'C' object has no attribute 'b'
class C(B):
    c = 3
    def __init__(self):
        self.cc = 33
    def fun_c(self):
        return "fun_c"

    
c_inst = C()
c_inst.cc
33
c_inst.c
3
c_inst.fun_c()
'fun_c'
c_inst.b
2
c_inst.a
1
c_inst.bb
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    c_inst.bb
AttributeError: 'C' object has no attribute 'bb'. Did you mean: 'b'?
c_inst.fun_b
<bound method B.fun_b of <__main__.C object at 0x000001B192946900>>
c_inst.a
1
c_inst.aa
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c_inst.aa
AttributeError: 'C' object has no attribute 'aa'. Did you mean: 'a'?
c_inst.fun_a
<bound method A.fun_a of <__main__.C object at 0x000001B192946900>>
class A:
    a = 1
    def __init__(self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B(A):
    b = 2
    def __init__(self):
        super().__init()
        self.bb = 22
    def fun_b(self):
        return "fun_b"

    
class C(B):
    c = 3
    def __init__(self):
        super().__init()
        self.cc = 33
    def fun_c(self):
        return "fun_c"

    
c_inst.C()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c_inst.C()
AttributeError: 'C' object has no attribute 'C'. Did you mean: 'c'?
c_inst.C
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    c_inst.C
AttributeError: 'C' object has no attribute 'C'. Did you mean: 'c'?
c_inst.c
3
c_inst.aa
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c_inst.aa
AttributeError: 'C' object has no attribute 'aa'. Did you mean: 'a'?
class B(A):
    b = 2
    def __init__(self):
        super().__init__()
        self.bb = 22
    def fun_b(self):
        return "fun_b"

    
class C(B):
    c = 3
    def __init__(self):
        super().__init__()
        self.cc = 33
    def fun_c(self):
        return "fun_c"

    
c_inst = C()
c_inst.c
3
c_inst.aa
11
c_inst.bb
22

C.mro()
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
B.mro()
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
A.mro()
[<class '__main__.A'>, <class 'object'>]



# множественное наследование

class A:
    a = 1
    var = 100
    def __init__(self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B:
    B = 1
    var = 333
    def __init__(self):
        self.bb = 11
    def fun_b(self):
        return "fun_b"

    
class C(A, B):
    pass

c_inst = C()
c_inst.a
1
c_inst.B
1
c_inst.var
100

class D(B,A):
    pass
d_inst = D()
SyntaxError: invalid syntax
class D(B,A):
    pass


d_inst = D()
d_inst.var
333





C.mro()
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
class A:
    def start(self):
        print("A-start")
    def job(self):
        self.start()

        
class B:
    def start(self):
        print("B-start")

        

class B(A):
    def start(self):
        print("B-start")

        
B.mro
<built-in method mro of type object at 0x000001B19262DEB0>
B.mro()
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
a_in =A()
b_in =B()

a_in.start()
A-start
a_in.job()
A-start
b_in.start()
B-start
b_in.job()
B-start




class A:
    def __str__(self):
        print("A-str")

        
class B(A):
    def __str__(self):
        print("B-str")


class A:
    def __str__(self):
        return "A-str"

    
class B(A):
    def __str__(self):
        return "B-str"

    
bb = B()
print(bb)
B-str




екнЖ
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    екнЖ
NameError: name 'екнЖ' is not defined
try:
    1/0
except:
    print(0)
else:
    print('ok')
finally:
    print("bum!")

    
0
bum!
try:
    print()
except:
    print(0)
else:
    print('ok')
finally:
    print("bum!")

    

ok
bum!
try:
    print()
except:
    print(0)
else:
    print('ok')

    

ok

try:
    1/0
except:
    print(0)
else:
    print('ok')

    
0

try:
    print()
finally:
    print("bum!")

    

bum!
try:
    1/0
else:
    print('ok')
    
SyntaxError: expected 'except' or 'finally' block
try:
    1/0
except:
    print(0)
finally:
    print("bum!")

    
0
bum!
try:
    1/0
finally:
    print("bum!")

    
bum!
Traceback (most recent call last):
  File "<pyshell#149>", line 2, in <module>
    1/0
ZeroDivisionError: division by zero



class User:
    def ___init__(self,n,a):
        self.name=n
        self.age=a
    def __rrepr__(self):
        return f"user({self.name},{self.age})"

    
def user_input():
    n,a = input("name"), int(input("age"))
    if len(n) < 2:
        pass ## вызвать исключение
    if a < 0:
        pass ## возраст отрицательный
    return User(n,a)

def user_input():
    n,a = input("name"), int(input("age"))
    if len(n) < 2:
        pass ## вызвать исключение ОшибкаДлина имени
    if a < 0:
        pass ## вызвать исключение Ошибкавозраст отрицателеьный
    return User(n,a)


class UserNameError(Exception):
    def __init__(self, u_name, msg="name < 2 simbols"):
        self.u_name-u_name
        self.msg = msg

        
raise UserNameError("A")
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    raise UserNameError("A")
  File "<pyshell#174>", line 3, in __init__
    self.u_name-u_name
AttributeError: 'UserNameError' object has no attribute 'u_name'
class UserNameError(Exception):
    def __init__(self, u_name, msg="name < 2 simbols"):
        self.u_name=u_name
        self.msg = msg

        
raise UserNameError("A")
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    raise UserNameError("A")
UserNameError: A
class UserNameError(Exception):
    def __init__(self, u_name, msg="name < 2 simbols"):
        self.u_name=u_name
        self.msg = msg
    def __repr__(self):
        return self.msg +"-->"+self.msg

    
class UserAgeError(Exception):
    def __init__(self, u_age, msg="age < 0 nelsia"):
        self.u_age=u_age
        self.msg = msg
    def __repr__(self):
        return f"{self.u_age} --> {self.msg}"

    
raise UserAgeError(-1)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    raise UserAgeError(-1)
UserAgeError: -1


def user_input():
    n,a = input("name"), int(input("age"))
    if len(n) < 2:
        raise UserNameError(n)## вызвать исключение ОшибкаДлина имени
    if a < 0:
        raise UserAgeError(a)## вызвать исключение Ошибкавозраст отрицателеьный
    return User(n,a)

user_input()
nameasdfg
age333
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    user_input()
  File "<pyshell#189>", line 7, in user_input
    return User(n,a)
TypeError: User() takes no arguments
user_input()
name s
age2
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    user_input()
  File "<pyshell#189>", line 7, in user_input
    return User(n,a)
TypeError: User() takes no arguments

try:
    user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("something wrong")

    
nameS
age11
S
class User:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __repr__(self):
        return f"User({self.name}, {self.age})"

    
class UserNameError(Exception):
    def __init__(self, u_name, message="имя пользователя меньше 2-ух симоволов запрещено!"):
        self.u_name = u_name
        self.message = message
    def __str__(self):
        return self.u_name + "-->" + self.message

    
class UserAgeError(Exception):
    def __init__(self, u_age, message="возраст пользователя не может быть меньше нуля!"):
        self.u_age = u_age
        self.message = message
    def __str__(self):
        return f"{self.u_age} --> {self.message}"

    
def user_input():
    n, a = input("name "), int(input("age "))
    if len(n) < 2:
        raise UserNameError(n)
    if a < 0:
        raise UserAgeError(a)
    return User(n, a)

try:
    user = user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("Чтото не так...")

    
name A
age 1
A-->имя пользователя меньше 2-ух симоволов запрещено!
try:
    user = user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("Чтото не так...")

    
name ss
age -2
-2 --> возраст пользователя не может быть меньше нуля!

try:
    user = user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("Чтото не так...")

    
name a
age -1
a-->имя пользователя меньше 2-ух симоволов запрещено!





>>> 
>>> 
>>> 
>>> # lab
>>> # Que - put, get, __que = []
>>> # exception - QueEmptyError
>>> 
>>> class Que:
...     def __init__(self):
...         self.__que = []
...         print("очередь создана")
...     def put(self, num):
...         self.__que.append(num)
...         print("успешно добавдено")
...     def get(self):
...         if len(self.__que) < 1:
...             raise EmptyQueError
...         del self.__que[0]
...         print("успешно удалено")
... 
...         
>>> 
>>> class EmptyQueError(Exception):
...     """очередь пуста"""
...     pass
... 
>>> q1 = Que()
очередь создана
>>> for i in range(5):
...     q1.put(i)
... 
...     
успешно добавдено
успешно добавдено
успешно добавдено
успешно добавдено
успешно добавдено
q1.__dict__
{'_Que__que': [0, 1, 2, 3, 4]}
q1.get()
успешно удалено
q1.get()
успешно удалено
q1.get()
успешно удалено
q1.get()
успешно удалено
q1.get()
успешно удалено
q1.get()
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    q1.get()
  File "<pyshell#239>", line 10, in get
    raise EmptyQueError
EmptyQueError
for i in range(5):
    q1.put(i)

    
успешно добавдено
успешно добавдено
успешно добавдено
успешно добавдено
успешно добавдено
q1.__dict__
{'_Que__que': [0, 1, 2, 3, 4]}
q1.get()
успешно удалено
q1.__dict__
{'_Que__que': [1, 2, 3, 4]}
q1.get()
успешно удалено
q1.__dict__
{'_Que__que': [2, 3, 4]}
q1.get()
успешно удалено
q1.get()
успешно удалено
q1.get()
успешно удалено
q1.get()
Traceback (most recent call last):
  File "<pyshell#266>", line 1, in <module>
    q1.get()
  File "<pyshell#239>", line 10, in get
    raise EmptyQueError
EmptyQueError


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

        
for i in range(5):
    q1.put(i)

    
успешно добавдено
успешно добавдено
успешно добавдено
успешно добавдено
успешно добавдено
for i in range(6):
    q1.get(i)

    
Traceback (most recent call last):
  File "<pyshell#275>", line 2, in <module>
    q1.get(i)
TypeError: Que.get() takes 1 positional argument but 2 were given

q1 = Que()
очередь создана
for i in range(5):
    q1.put(i)

    
успешно добавдено
текущее значение оцереди [0]

успешно добавдено
текущее значение оцереди [0, 1]

успешно добавдено
текущее значение оцереди [0, 1, 2]

успешно добавдено
текущее значение оцереди [0, 1, 2, 3]

успешно добавдено
текущее значение оцереди [0, 1, 2, 3, 4]

for i in range(5):
    q1.put(i)

успешно добавдено
текущее значение оцереди [0, 1, 2, 3, 4, 0]

успешно добавдено
текущее значение оцереди [0, 1, 2, 3, 4, 0, 1]

успешно добавдено
текущее значение оцереди [0, 1, 2, 3, 4, 0, 1, 2]

успешно добавдено
текущее значение оцереди [0, 1, 2, 3, 4, 0, 1, 2, 3]

успешно добавдено
текущее значение оцереди [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

for i in range(5):
    q1.get(i)

    
Traceback (most recent call last):
  File "<pyshell#282>", line 2, in <module>
    q1.get(i)
TypeError: Que.get() takes 1 positional argument but 2 were given
del q1
q1 = Que()
очередь создана
for i in range(5):
    q1.put(i)

    
успешно добавдено
текущее значение оцереди [0]

успешно добавдено
текущее значение оцереди [0, 1]

успешно добавдено
текущее значение оцереди [0, 1, 2]

успешно добавдено
текущее значение оцереди [0, 1, 2, 3]

успешно добавдено
текущее значение оцереди [0, 1, 2, 3, 4]

for i in range(6):
    q1.get()

    
успешно удалено
текущее значение оцереди [1, 2, 3, 4]

успешно удалено
текущее значение оцереди [2, 3, 4]

успешно удалено
текущее значение оцереди [3, 4]

успешно удалено
текущее значение оцереди [4]

успешно удалено
текущее значение оцереди []

Traceback (most recent call last):
  File "<pyshell#288>", line 2, in <module>
    q1.get()
  File "<pyshell#271>", line 12, in get
    raise EmptyQueError
EmptyQueError

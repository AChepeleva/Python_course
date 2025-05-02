Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

13+13
26
li = [1,2,3,4]
li
[1, 2, 3, 4]
li[1]
2
di = {1:2222,2:333}
di
{1: 2222, 2: 333}
del di
di
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    di
NameError: name 'di' is not defined. Did you mean: 'li'?
try:
    print(di)
except NameError:
    print("dcfvgbhnjmk")
    raise

dcfvgbhnjmk
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    print(di)
NameError: name 'di' is not defined. Did you mean: 'li'?
try:
    vgbhnj
except NameError:
    prunt(123)
except:
    print(wsdf)

    
Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    vgbhnj
NameError: name 'vgbhnj' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#21>", line 4, in <module>
    prunt(123)
NameError: name 'prunt' is not defined. Did you mean: 'print'?







# car
# vin volume bbody_type

class Car:
    def __init__(self, vin, volume, bbody_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f"Car({self.vin}, {self.volume}, {self.body_type})"

    
lada1 = Car()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    lada1 = Car()
TypeError: Car.__init__() missing 3 required positional arguments: 'vin', 'volume', and 'bbody_type'
lada1 = Car("1234", 2.34,"fghjk")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    lada1 = Car("1234", 2.34,"fghjk")
  File "<pyshell#39>", line 5, in __init__
    self.body_type = body_type
NameError: name 'body_type' is not defined. Did you mean: 'bbody_type'?
lada1.__dict__
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    lada1.__dict__
NameError: name 'lada1' is not defined
lada1 = Car("123123123", 2.34,"fghjdcck")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    lada1 = Car("123123123", 2.34,"fghjdcck")
  File "<pyshell#39>", line 5, in __init__
    self.body_type = body_type
NameError: name 'body_type' is not defined. Did you mean: 'bbody_type'?
class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f"Car({self.vin}, {self.volume}, {self.body_type})"

    
lada1 = Car("1234", 2.34,"fghjk")
lada1
Car(1234, 2.34, fghjk)
lada2 = Car ("22222", 3.3, "qwerf")
lada2
Car(22222, 3.3, qwerf)
lada1.__dict__
{'vin': '1234', 'volume': 2.34, 'body_type': 'fghjk'}
li = [lada1,lada2]
for car_i in li:
    print(car_i.vin)
    print(car_i.volume)
    print(car_i.body_type)

    
1234
2.34
fghjk
22222
3.3
qwerf
for car_i in li:
    for k,  v in car_i.__dict__.items():
        print(k,":",v)

        
vin : 1234
volume : 2.34
body_type : fghjk
vin : 22222
volume : 3.3
body_type : qwerf


class Car:
    def __init__(bla, vin, volume, body_type):
        bla.vin = vin
        bla.volume = volume
        bla.body_type = body_type
    def __repr__(bla):
        return f"Car({bla.vin}, {bla.volume}, {bla.body_type})"

    
lada1 = Car("1234", 2.34,"fghjk")
lada1
Car(1234, 2.34, fghjk)
lada2 = Car ("22222", 3.3, "qwerf")
lada2
Car(22222, 3.3, qwerf)


class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f"Car({self.vin}, {self.volume}, {self.body_type})"

    
lada2 = Car ("22222", 3.3, "qwerf")
lada2
Car(22222, 3.3, qwerf)
lada2.body_type = "coupe"

lada2
Car(22222, 3.3, coupe)
lada2.new_var = 12345678
lada2
Car(22222, 3.3, coupe)
lada2.__dict__
{'vin': '22222', 'volume': 3.3, 'body_type': 'coupe', 'new_var': 12345678}
Car.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '__init__': <function Car.__init__ at 0x0000021BE2578D60>, '__repr__': <function Car.__repr__ at 0x0000021BE2578E00>, '__static_attributes__': ('body_type', 'vin', 'volume'), '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
Car.__format__
<method '__format__' of 'object' objects>
Car.__bases__
(<class 'object'>,)
class S:
    pass
fg = S()
SyntaxError: invalid syntax
class S:
    pass

fg = S()
fg
<__main__.S object at 0x0000021BE2456BA0>





class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f"Car({self.vin}, {self.volume}, {self.body_type})"
    def move(self):
        print("move")
    def turn(self, direct):
        print("turn", direct)
    def stop(self):
        print("stop")

        
class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270,max_speed=300):
        super().__init__(self, vin, volume, body_type)
        self.speed_limit =  max_speed
    def __repr__(self):
        super().__repr__()
        return f"SportCar({self.speed_limit}, {self.max_speed})"
    def race(self):
        print(f"race with {self.max_speed} km\h")

        
renault = SportCar("1111111", 2.3.5,"coupe")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
renault = SportCar("1111111", 2.5,"coupe")
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    renault = SportCar("1111111", 2.5,"coupe")
  File "<pyshell#108>", line 3, in __init__
    super().__init__(self, vin, volume, body_type)
TypeError: Car.__init__() takes 4 positional arguments but 5 were given
class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270,max_speed=300):
        super().__init__(vin, volume, body_type)
        self.speed_limit =  max_speed
    def __repr__(self):
        return super().__repr___() + "\n" +"f"SportCar({self.speed_limit}, {self.max_speed})"
    def race(self):
        print(f"race with {self.max_speed} km\h")
        
SyntaxError: unterminated string literal (detected at line 6)

class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270,max_speed=300):
        super().__init__(vin, volume, body_type)
        self.speed_limit =  max_speed
    def __repr__(self):
        return super().__repr___() + "\n" +f"SportCar({self.speed_limit}, {self.max_speed})"
    def race(self):
        print(f"race with {self.max_speed} km\h")

        
renault = SportCar("1111111", 2.5,"coupe")
renault
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    renault
  File "C:\Users\Sasha_Ch\AppData\Local\Programs\Python\Python313\Lib\idlelib\rpc.py", line 620, in displayhook
    text = repr(value)
  File "<pyshell#114>", line 6, in __repr__
    return super().__repr___() + "\n" +f"SportCar({self.speed_limit}, {self.max_speed})"
AttributeError: 'super' object has no attribute '__repr___'. Did you mean: '__repr__'?
class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270,max_speed=300):
        super().__init__(vin, volume, body_type)
        self.speed_limit =  max_speed
    def __repr__(self):
        return super().__repr__() + "\n" +f"SportCar({self.speed_limit}, {self.max_speed})"
    def race(self):
        print(f"race with {self.max_speed} km\h")

        
renault = SportCar("1111111", 2.5,"coupe")
renault
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    renault
  File "C:\Users\Sasha_Ch\AppData\Local\Programs\Python\Python313\Lib\idlelib\rpc.py", line 620, in displayhook
    text = repr(value)
  File "<pyshell#118>", line 6, in __repr__
    return super().__repr__() + "\n" +f"SportCar({self.speed_limit}, {self.max_speed})"
AttributeError: 'SportCar' object has no attribute 'max_speed'
class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270,max_speed=300):
        super().__init__(vin, volume, body_type)
        self.max_speed =  max_speed
    def __repr__(self):
        return super().__repr__() + "\n" +f"SportCar({self.speed_limit}, {self.max_speed})"
    def race(self):
        print(f"race with {self.max_speed} km\h")

        
renault = SportCar("1111111", 2.5,"coupe")
renault
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    renault
  File "C:\Users\Sasha_Ch\AppData\Local\Programs\Python\Python313\Lib\idlelib\rpc.py", line 620, in displayhook
    text = repr(value)
  File "<pyshell#122>", line 6, in __repr__
    return super().__repr__() + "\n" +f"SportCar({self.speed_limit}, {self.max_speed})"
AttributeError: 'SportCar' object has no attribute 'speed_limit'
class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270,max_speed=300):
        super().__init__(vin, volume, body_type)
        self.speed_limit =  speed_limit
        self.max_speed =  max_speed
    def __repr__(self):
        return super().__repr__() + "\n" +f"SportCar({self.speed_limit}, {self.max_speed})"
    def race(self):
        print(f"race with {self.max_speed} km\h")

        
renault = SportCar("1111111", 2.5,"coupe")
renault
Car(1111111, 2.5, coupe)
SportCar(270, 300)
renault.___repr___
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    renault.___repr___
AttributeError: 'SportCar' object has no attribute '___repr___'. Did you mean: '__repr__'?
renault.__repr__
<bound method SportCar.__repr__ of Car(1111111, 2.5, coupe)
SportCar(270, 300)>
renault.move
<bound method Car.move of Car(1111111, 2.5, coupe)
SportCar(270, 300)>
renault.race
<bound method SportCar.race of Car(1111111, 2.5, coupe)
SportCar(270, 300)>








class Dog:
    say(self, msg):
        
SyntaxError: invalid syntax
print()



class Dog:
    say(self, msg):
        
SyntaxError: invalid syntax
class Dog:
    def say(self, msg):
        print(msg)

        
class Bird:
    def say(self, msg):
        print(msg)

        
class Cat:
    def say(self, msg):
        print(msg)

        
d,c,b = Dog(),Bird(),cat()
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    d,c,b = Dog(),Bird(),cat()
NameError: name 'cat' is not defined. Did you mean: 'Cat'?
d,c,b = Dog(),Bird(),Cat()
d.say('dog'),c.say("kria"), b.say("mcat")
dog
kria
mcat
(None, None, None)
i,f,s = 12,3.4,"wsdcf"
i
12
f
3.4
s
'wsdcf'
i*3
36
f*3
10.2
s*3
'wsdcfwsdcfwsdcf'





#Stack

stack = []




class Stack:
    def __init__(self):
        self.__stack = []
        print("stack OK")
    def push(self, value):
        self.__stack.append(value)
        print(value,"OK")
    def pop(self):
        print(self.__stack.pop(),"del Ok")

        

s1 = Stack()
stack OK
s1.push(4)
4 OK
s1.push(22)
22 OK
s1.push(3)
3 OK
s1.__dict__
{'_Stack__stack': [4, 22, 3]}
s1.push(10)
10 OK
si.pop()
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    si.pop()
NameError: name 'si' is not defined. Did you mean: 'li'?
s1.pop()(
    
KeyboardInterrupt
s1.pop()
10 del Ok
s1.pop()
3 del Ok
s1.pop()
22 del Ok
s1.pop()
4 del Ok
s1.pop()
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    s1.pop()
  File "<pyshell#183>", line 9, in pop
    print(self.__stack.pop(),"del Ok")
IndexError: pop from empty list
s1.__dict__
{'_Stack__stack': []}



class Stack:
    def __init__(self):
        self.__stack = []
        print("stack OK")
    def push(self, value):
        self.__stack.append(value)
        print(value,"OK")
    def pop(self):
        print(self.__stack.pop(),"del Ok")
    def stat(self):
        print("tekushee sostoanie:")
        print(self.__stack)

        
s1  =Stack()
stack OK
s1.push(22)
22 OK
s1.push(99)
99 OK
s1.push(2)
2 OK
s1.stat()
tekushee sostoanie:
[22, 99, 2]
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

        
s1  =Stack()
stack OK
s1.stat()
tekushee sostoanie:
[]
s1.pop()
pusto


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
        supper().__init__()
        self.__summa = 0
    def push(self, value):
        supper().push(self, value)
        self.__summa += value
    def get_sum(self):
        print(self.__summa)

        

s2 = AddstackVal()
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    s2 = AddstackVal()
  File "<pyshell#229>", line 3, in __init__
    supper().__init__()
NameError: name 'supper' is not defined. Did you mean: 'super'?
class AddstackVal(Stack):
    def __init__(self):
        super().__init__()
        self.__summa = 0
    def push(self, value):
        super().push(self, value)
        self.__summa += value
    def get_sum(self):
        print(self.__summa)

        
s2 = AddstackVal()
stack OK
s2.get_summa()
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    s2.get_summa()
AttributeError: 'AddstackVal' object has no attribute 'get_summa'. Did you mean: 'get_sum'?
s2.get_sum()
0
s2.stat()
tekushee sostoanie:
[]
s2.push(33)
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    s2.push(33)
  File "<pyshell#233>", line 6, in push
    super().push(self, value)
TypeError: Stack.push() takes 2 positional arguments but 3 were given
class AddstackVal(Stack):
    def __init__(self):
        super().__init__()
        self.__summa = 0
    def push(self, value):
        super().push(value)
        self.__summa += value
    def get_sum(self):
        print(self.__summa)

        
s2 = AddstackVal()
stack OK
s2.get_summa()
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    s2.get_summa()
AttributeError: 'AddstackVal' object has no attribute 'get_summa'. Did you mean: 'get_sum'?
s2.get_sum()
0
s2.push(33)
33 OK
s2.push(2)
2 OK
s2.stat
<bound method Stack.stat of <__main__.AddstackVal object at 0x0000021BE24570E0>>





a = 10
b = 15
a + b
25
help(int)





a = 10
b = 15
a + b
25
a.__add__(b)
25
c,d = 3.13,5.7
c.__add__(d)
8.83
help(float)



class Dog:
    def __init__(self,num):
        self.num = num
    def __add__(self,dog_inst):
        return self.num + dog_inst.number

    
d1,d2 = Dog(4),Dog(6)

d1.__add__(d2)
Traceback (most recent call last):
  File "<pyshell#276>", line 1, in <module>
    d1.__add__(d2)
  File "<pyshell#273>", line 5, in __add__
    return self.num + dog_inst.number
AttributeError: 'Dog' object has no attribute 'number'
class Dog:
    def __init__(self,num):
        self.num = num
    def __add__(self,dog_inst):
        return self.num + dog_inst.num

    
d1,d2 = Dog(4),Dog(6)
d1.__add__(d2)
10
d1+d2
10
class Dog:
    def __init__(self,name,age,color,salary):
        self.name= name
        self.age= age
        self.color= color
        self.salare= salary


d1,d2 = Dog("Jo",4,"red",100), Dog("Jojo",1,"blue",1001)
d1+d2
Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    d1+d2
TypeError: unsupported operand type(s) for +: 'Dog' and 'Dog'
class Dog:
    def __init__(self,name,age,color,salary):
        self.name= name
        self.age= age
        self.color= color
        self.salare= salary
    def __add__(self,next_dog):
        return self.salary +next_dog.salary

    
d1,d2 = Dog("Jo",4,"red",100), Dog("Jojo",1,"blue",1001)
d1+d2
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    d1+d2
  File "<pyshell#287>", line 8, in __add__
    return self.salary +next_dog.salary
AttributeError: 'Dog' object has no attribute 'salary'. Did you mean: 'salare'?
class Dog:
    def __init__(self,name,age,color,salary):
        self.name= name
        self.age= age
        self.color= color
        self.salary= salary
    def __add__(self,next_dog):
        return self.salary +next_dog.salary

    
d1,d2 = Dog("Jo",4,"red",100), Dog("Jojo",1,"blue",1001)

d1+d2
1101
class Dog:
    def __init__(self,name,age,color,salary):
        self.name= name
        self.age= age
        self.color= color
        self.salary= salary
    def __add__(self,next_dog):
        return self.salary +next_dog.salary
    def __len__(self):
        return self.age

    
d1,d2 = Dog("Jo",4,"red",100), Dog("Jojo",1,"blue",1001)

d1+d2
1101
len(d1)
4
len(d2)
1
class Dog:
    def __init__(self,name,age,color,salary):
        self.name= name
        self.age= age
        self.color= color
        self.salary= salary
    def __add__(self,next_dog):
        return self.salary +next_dog.salary
    def __len__(self):
        return self.age
    def __sub__(self,next_dog):
        return self.salary - next_dog.salary

    
d1,d2 = Dog("Jo",4,"red",100), Dog("Jojo",1,"blue",1001)

d1+d2
1101
d1-d2
-901
len(d1)
4
len(d2)
1
class Dog:
    def __init__(self,name,age,color,salary):
        self.name= name
        self.age= age
        self.color= color
        self.salary= salary
    def __add__(self,next_dog):
        return self.salary +next_dog.salary
    def __len__(self):
        return self.age
    def __sub__(self,next_dog):
        return self.salary - next_dog.salary
    def __eq__(self,next_dog):
        return self.name == next_dog
    def __ne__(self,next_dog):
        return self.name != next_dog

    
d1,d2 = Dog("Jo",4,"red",100), Dog("Jojo",1,"blue",1001)

d1+d2
1101
d1-d2
-901
d1==d2
False
d1!=d2
True
class Dog:
    def __init__(self,name,age,color,salary):
...         self.name= name
...         self.age = age
...         self.color= color
...         self.salary= salary
...     def __add__(self,next_dog):
...         return self.salary +next_dog.salary
...     def __len__(self):
...         return self.age
...     def __sub__(self,next_dog):
...         return self.salary - next_dog.salary
...     def __eq__(self,next_dog):
...         return self.name == next_dog.name
...     def __ne__(self,next_dog):
...         return self.name != next_dog.name
...     def __pow__(self,value):
...         return self.age ** value
...     def __mul__(self, next_dog):
...         return self.age * next_dog.age
... 
...     
>>> d1,d2 = Dog("Jo",4,"red",100), Dog("Jojo",1,"blue",1001)
... 
>>> d1+d2
1101
>>> d1-d2
-901
>>> d1!=d2
True
>>> d1**2
16
>>> d2**3
1
>>> d1*d2
4
>>> len(d1)
4
>>> 

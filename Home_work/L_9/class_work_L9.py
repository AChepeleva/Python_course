Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.



# CRM

client1 = ["Dima", 37529123456,"dima@d.mail"]
slient1 [0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    slient1 [0]
NameError: name 'slient1' is not defined. Did you mean: 'client1'?
client1[0]
'Dima'
'Dima'
'Dima'







client2 = [ 37529123456,"sdcds","dima@d.mail"]



class Wallet:
    pass

a = 10
b='asd'
wal = Wallet()

type(a)
<class 'int'>
type(wal)
<class '__main__.Wallet'>
type(b)
<class 'str'>
class Dog:
    pass

class Car:
    pass

lada = Car()
type(lada)
<class '__main__.Car'>
bob = Dog()
type(bob)
<class '__main__.Dog'>





class Wallet:
    def __init__(self, w_id, amount, owner):
        pass

    
w1 = Wallet(2,100,'vasia')

w1
<__main__.Wallet object at 0x0000013890E26E40>
w1.w_id
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    w1.w_id
AttributeError: 'Wallet' object has no attribute 'w_id'

class Wallet:
    def __init__(self, wid, amount, owner):
        self.wid = wid
        self.amount = amoutn
        self.owner = owner

        
w1 = Wallet()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    w1 = Wallet()
TypeError: Wallet.__init__() missing 3 required positional arguments: 'wid', 'amount', and 'owner'
w1 = Wallet(2,100,'vasia')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    w1 = Wallet(2,100,'vasia')
  File "<pyshell#57>", line 4, in __init__
    self.amount = amoutn
NameError: name 'amoutn' is not defined. Did you mean: 'amount'?
class Wallet:
    def __init__(self, wid, amount, owner):
        self.wid = wid
        self.amount = amount
        self.owner = owner

        
w1 = Wallet(2,100,'vasia')
w1
<__main__.Wallet object at 0x0000013890E26F90>
w1.wid
2
w1.amount
100
w1.owner
'vasia'
w2 = Wallet(11,10000,'wwwww')
w2.wid
11
w1.wid
2

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
bobik = Dog("Bobok", 1)

bobik
<__main__.Dog object at 0x0000013890E26E40>
bobik.age
1
drug = Dog("Drug", 2)
drug.age
2



class Client:
    def __init__(self, name, phone, email = None):
        self.name = name
        self.phone = phone
        sel.email = email

        

c1 = Client("Dima", 234567)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    c1 = Client("Dima", 234567)
  File "<pyshell#89>", line 5, in __init__
    sel.email = email
NameError: name 'sel' is not defined. Did you mean: 'self'?
class Client:
    def __init__(self, name, phone, email = None):
        self.name = name
        self.phone = phone
        self.email = email

        

c1 = Client("Dima", 234567)

c1
<__main__.Client object at 0x0000013890E27230>
c2 = Client("Vasia", 66666666, "dddd@mail.com")

c1.email
print(c1.email )
None
c2.name
'Vasia'
c2.email
'dddd@mail.com'
type(c1)
<class '__main__.Client'>
type(c2)
<class '__main__.Client'>




st = []
n = 4
for i in range(4):
    print('client number: ', i)
    name = input('name:')
    phone = input('phone:')
    email = input('email:')
    cl = Client(name, phone, email)
    st.append(cl)

    
client number:  0
name:Cima
phone:12345678
email:sdf@m.com
client number:  1
name:Sasha
phone:123456
email:sasha@m.com
client number:  2
name:Vasia
phone:11111111
email:sdf@c.m
client number:  3
name:zac
phone:23456
email:swdc@mai;.com

st
[<__main__.Client object at 0x0000013890F30190>, <__main__.Client object at 0x0000013890F302D0>, <__main__.Client object at 0x0000013890F30410>, <__main__.Client object at 0x0000013890F30550>]
def show_cl(clients):
    for cl in clients:
        print("name: ", cl.name)
        print("phone: ", cl.phone)
        print("email: ", cl.email)
        print()
    print()

    
show_cl(st)
name:  Cima
phone:  12345678
email:  sdf@m.com

name:  Sasha
phone:  123456
email:  sasha@m.com

name:  Vasia
phone:  11111111
email:  sdf@c.m

name:  zac
phone:  23456
email:  swdc@mai;.com




class Dog:
    class_v = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
Dog.class_v
0
Dog.name
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    Dog.name
AttributeError: type object 'Dog' has no attribute 'name'
d1 = Dog("dog",1)

d1.name
'dog'
d1.class_v
0
d1.name ="bobik"

d1.name
'bobik'
d1.age =10000
d1.age
10000
Dog.class_a=1111
Dpg.class_v
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    Dpg.class_v
NameError: name 'Dpg' is not defined. Did you mean: 'Dog'?
Dog.class_v
0
Dog.class_v = 111
Dog.class_v
111



class Task:
    count = 1
    def __init__(self, name):
        self.task_i = Task.count
        Task.count += 1
        self.name=name
        self.task_status = False

        
t1= Task("go")
t2 = task("run")
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    t2 = task("run")
NameError: name 'task' is not defined. Did you mean: 'Task'?
t2 = Task("run")
t3 = Task("sleep")
print(t1.task_i,t1.name,t1.task_status)
1 go False
print(t2.task_i,t2.name,t2.task_status)
2 run False
print(t3.task_i,t3.name,t3.task_status)
3 sleep False



class F:
    a = 9
    def __init__(self):
        pass

    
s = F()
s
<__main__.F object at 0x0000013890E27620>
s.__dict__
{}
F.a
9
F.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, 'a': 9, '__init__': <function F.__init__ at 0x0000013890F41BC0>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'F' objects>, '__weakref__': <attribute '__weakref__' of 'F' objects>, '__doc__': None})


class F:
    """python3dll."""
    a = 9
    def __init__(self):
        pass

    

F.__doc__
'python3dll.'
help(F)
Help on class F in module __main__:

class F(builtins.object)
 |  python3dll.
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  a = 9



class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.name}, an i am {self.age}')

        
bob = Cat("barsic", 3)
bob.hello()
hello!my name is barsic, an i am 3


class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.name}, an i am {self.age}')
    def say(self, msg):
        print(f'{self.name} says: {self.msg}')

        
bob
<__main__.Cat object at 0x0000013890E27770>
bob = Cat('Bob', 3)
bob.name
'Bob'
bob.age
3
bob.hello
<bound method Cat.hello of <__main__.Cat object at 0x0000013890E26CF0>>
bob.hello()
hello!my name is Bob, an i am 3
bob.say("Meow!")
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    bob.say("Meow!")
  File "<pyshell#203>", line 8, in say
    print(f'{self.name} says: {self.msg}')
AttributeError: 'Cat' object has no attribute 'msg'

class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.name}, an i am {self.age}')
    def say(self, msg):
        print(f'{self.name} says: {msg}')

        
bob = Cat('Bob', 3)
bob.name
'Bob'
bob.say("Meow!")
Bob says: Meow!



class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.name}, an i am {self.age}')
    def say(self, msg):
        print(f'{self.name} says: {msg}')
    def grow(self):
        self.age +=1

    

bob = Cat('Bob', 3)


bob.hello()
hello!my name is Bob, an i am 3
bob.grow()
bob.hello()
hello!my name is Bob, an i am 4





a=1
li=[1,2,3]
print(a,li)
1 [1, 2, 3]
bob
<__main__.Cat object at 0x0000013890E278C0>
print(bob)
<__main__.Cat object at 0x0000013890E278C0>


a
1
class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.name}, an i am {self.age}')
    def say(self, msg):
        print(f'{self.name} says: {msg}')
    def grow(self):
        self.age +=1
    def __repr__(self):
        return f"Cat info. \n {self.name}, {self.age}"

    

bob = Cat('Bob', 3)
bob.__repr__
<bound method Cat.__repr__ of Cat info. 
 Bob, 3>
print(bob)
Cat info. 
 Bob, 3
bob
Cat info. 
 Bob, 3
class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.name}, an i am {self.age}')
    def say(self, msg):
        print(f'{self.name} says: {msg}')
    def grow(self):
        self.age +=1
    def __repr__(self):
        return f"Cat info. \n {self.name}, {self.age}"
    def __str__(self):
        return f"{sself.name}, {self.age}"

    

bob = Cat('Bob', 3)
bob
Cat info. 
 Bob, 3
print(bob)
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    print(bob)
  File "<pyshell#257>", line 14, in __str__
    return f"{sself.name}, {self.age}"
NameError: name 'sself' is not defined. Did you mean: 'self'?
class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.name}, an i am {self.age}')
    def say(self, msg):
        print(f'{self.name} says: {msg}')
    def grow(self):
        self.age +=1
    def __repr__(self):
        return f"Cat info. \n {self.name}, {self.age}"
    def __str__(self):
        return f"{self.name}, {self.age}"

    

bob = Cat('Bob', 3)
bob
Cat info. 
 Bob, 3
print(bob)
Bob, 3



help(Cat)
Help on class Cat in module __main__:

class Cat(builtins.object)
 |  Cat(name, age)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, age)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  __str__(self)
 |      Return str(self).
 |
 |  grow(self)
 |
 |  hello(self)
 |
 |  say(self, msg)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

help(int)
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating-point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Built-in subclasses:
 |      bool
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(self, /)
 |      Ceiling of an Integral returns itself.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floor__(self, /)
 |      Flooring an Integral returns itself.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Convert to a string according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __invert__(self, /)
 |      ~self
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __neg__(self, /)
 |      -self
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __rand__(self, value, /)
 |      Return value&self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __round__(self, ndigits=<unrepresentable>, /)
 |      Rounding an Integral returns itself.
 |
 |      Rounding with an ndigits argument also returns an integer.
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __rxor__(self, value, /)
 |      Return value^self.
 |
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(self, /)
 |      Truncating an Integral returns itself.
 |
 |  __xor__(self, value, /)
 |      Return self^value.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is equal to the original int.
 |
 |      The ratio is in lowest terms and has a positive denominator.
 |
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |
 |      Also known as the population count.
 |
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |
 |  conjugate(self, /)
 |      Returns self, the complex conjugate of any int.
 |
 |  is_integer(self, /)
 |      Returns True. Exists for duck type compatibility with float.is_integer.
 |
 |  to_bytes(self, /, length=1, byteorder='big', *, signed=False)
 |      Return an array of bytes representing an integer.
 |
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.  Default
 |        is length 1.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        sys.byteorder as the byte order value.  Default is to use 'big'.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  from_bytes(bytes, byteorder='big', *, signed=False)
 |      Return the integer represented by the given array of bytes.
 |
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        sys.byteorder as the byte order value.  Default is to use 'big'.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  denominator
 |      the denominator of a rational number in lowest terms
 |
 |  imag
 |      the imaginary part of a complex number
 |
 |  numerator
 |      the numerator of a rational number in lowest terms
 |
 |  real
 |      the real part of a complex number








class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.name}, an i am {self.age}')
    def say(self, msg):
        print(f'{self.name} says: {msg}')
    def grow(self):
        self.age +=1
    def __repr__(self):
        return f"Cat info. \n {self.name}, {self.age}"
    def __str__(self):
        return f"{self.name}, {self.age}"

        

class Dog:
    pass

d = Dog()
Dog.__bases__
(<class 'object'>,)

class Swim_cat(Cat):
    def swim (self):
        print("I can swim!")

        

sad = Swim_cat("Sadic", 2)
sad
Cat info. 
 Sadic, 2
sadic.name
Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    sadic.name
NameError: name 'sadic' is not defined
sad.name
'Sadic'
print(sad)
Sadic, 2


sad.age
2
sad.hello()
hello!my name is Sadic, an i am 2
sad.grow()

sad.hello()
hello!my name is Sadic, an i am 3

class Swim_cat(Cat):
    def swim (self):
        print("I can swim!")
    def __str__(self):
        return f"Swim_cat: {self.name}, {self.age}"

    
sad = Swim_cat
sad
<class '__main__.Swim_cat'>
print(sad)
<class '__main__.Swim_cat'>
sad = Swim_cat()
Traceback (most recent call last):
  File "<pyshell#312>", line 1, in <module>
    sad = Swim_cat()
TypeError: Cat.__init__() missing 2 required positional arguments: 'name' and 'age'
sad = Swim_cat("Sadic", 2)
sad
Cat info. 
 Sadic, 2
print(sad)
Swim_cat: Sadic, 2
Swim_cat: Sadic, 2
SyntaxError: invalid syntax




class Swim_cat(Cat):
    def __init__(self, name, age,color):
        super().__init__(name,age)
        self.color= color
    def swim (self):
        print("I can swim!")
    def __str__(self):
        return f"Swim_cat: {self.name}, {self.age}"

    
sad = Swim_cat("Sadic", 2, "red")

sad.__dict__
{'name': 'Sadic', 'age': 2, 'color': 'red'}
class Swim_cat(Cat):
    def __init__(self, name, age,color):
        super().__init__(name,age)
        self.color= color
    def swim (self):
        print("I can swim!")
    def swim(self):
        super().hello()
        print(f"my color: {self.color}")
    def __str__(self):
        return f"Swim_cat: {self.name}, {self.age}"

    

sad = Swim_cat("Sadic", 2, "red")
sad.swim()
hello!my name is Sadic, an i am 2
my color: red




class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.name}, an i am {self.age}')
    def __str__(self):
        return f"{self.name}, {self.age}"



c= Cat('Sad', 1)

c.hello()
hello!my name is Sad, an i am 1
c.name = "Noname"
c.hello()
hello!my name is Noname, an i am 1
class Cat:
    def __init__(self, name, age):
        self.__name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.name}, an i am {self.age}')
    def __str__(self):
        return f"{self.name}, {self.age}"

    
c= Cat('Sad', 1)
c.hello()
Traceback (most recent call last):
  File "<pyshell#346>", line 1, in <module>
    c.hello()
  File "<pyshell#344>", line 6, in hello
    print(f'hello!my name is {self.name}, an i am {self.age}')
AttributeError: 'Cat' object has no attribute 'name'
class Cat:
    def __init__(self, name, age):
        self.__name= name
        self.age = age
    def hello(self):
        print(f'hello!my name is {self.__name}, an i am {self.age}')
    def __str__(self):
        return f"{self.__name}, {self.age}"

    
c= Cat('Sad', 1)
c.hello()
hello!my name is Sad, an i am 1
c.name
Traceback (most recent call last):
  File "<pyshell#351>", line 1, in <module>
    c.name
AttributeError: 'Cat' object has no attribute 'name'
c.__dict__
{'_Cat__name': 'Sad', 'age': 1}
c._Cat__name
'Sad'
class Cat:
    def __init__(self, name, age):
        self.__name= name
        self.age = age
    def hello(self):
...         print(f'hello!my name is {self.__name}, an i am {self.age}')
...     def __str__(self):
...         return f"{self.__name}, {self.age}"
...     def change(self, name)
...     
SyntaxError: expected ':'
>>> class Cat:
...     def __init__(self, name, age):
...         self.__name= name
...         self.age = age
...     def hello(self):
...         print(f'hello!my name is {self.__name}, an i am {self.age}')
...     def __str__(self):
...         return f"{self.__name}, {self.age}"
...     def change(self, name):
...         self.__name= name
... 
...         
>>> c= Cat('Sad', 1)
>>> c.hello
<bound method Cat.hello of <__main__.Cat object at 0x0000013890E27B60>>
>>> c.hello()
hello!my name is Sad, an i am 1
>>> c.__name
Traceback (most recent call last):
  File "<pyshell#362>", line 1, in <module>
    c.__name
AttributeError: 'Cat' object has no attribute '__name'
>>> c.change("sadd")
>>> c.hello()
hello!my name is sadd, an i am 1
>>> c.change("Sadd")
>>> c.hello()
hello!my name is Sadd, an i am 1
>>> 
>>> 
>>> 

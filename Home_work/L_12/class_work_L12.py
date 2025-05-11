Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


def a(v=100):
    returnv

    
a()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a()
  File "<pyshell#4>", line 2, in a
    returnv
NameError: name 'returnv' is not defined
def a(v=100):
    return v


a()
100



class Wallet():
    def __init__(self,amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self.amount
    def set_amount(self,value):
        if value < 0:
            pass
        self._amount = value

        

class NegAmount(Exception):
    """Negative balance"""
    pass

raise NegAmount
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    raise NegAmount
NegAmount
class Wallet():
    def __init__(self,amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self.amount
    def set_amount(self,value):
        if value < 0:
            raise NegAmount
        self._amount = value

        

u1 = Wallet()

u1.__dict__
{'_amount': 0}
u2 = Wallet(100)
u2.__dict__
{'_amount': 100}
u2.get_amount()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    u2.get_amount()
  File "<pyshell#30>", line 5, in get_amount
    return self.amount
AttributeError: 'Wallet' object has no attribute 'amount'. Did you mean: '_amount'?
class Wallet():
    def __init__(self,amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self._amount
    def set_amount(self,value):
        if value < 0:
            raise NegAmount
        self._amount = value

        
u2 = Wallet(100)
u1 = Wallet()
u2.get_amount()
100
u1.get_amount()
0
u2.set_amount(1000)
u2.get_amount()
1000
u1.set_amount(-1)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    u1.set_amount(-1)
  File "<pyshell#38>", line 8, in set_amount
    raise NegAmount
NegAmount



class Wallet():
    def __init__(self,amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self._amount
    def set_amount(self,value):
        if value < 0:
            raise NegAmount
        self._amount = value
    amount = property(get_amount,set_amount)

    
u1=Wallet()
u2=Wallet(100)
u2.amount
100
u2.amount = 10000
u2
<__main__.Wallet object at 0x000001AABE12FD90>
u2.amount
10000
u2.__dict__
{'_amount': 10000}




 def summ(a,b):
     
SyntaxError: unexpected indent
def summ(a,b):
    return a+b

summ(2,4)
6
summ(2,4,1)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    summ(2,4,1)
TypeError: summ() takes 2 positional arguments but 3 were given
def Myprint(a,b,c):
    print(a,b,c)

    
Myprint(1,2,3)
1 2 3
Myprint(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    Myprint(1,2,3,4,5)
TypeError: Myprint() takes 3 positional arguments but 5 were given
print()

help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

def Myprint(args):
    print(type(args))
    for val in args:
        print(val, end=" ")

        
Myprint(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    Myprint(1,2,3,4)
TypeError: Myprint() takes 1 positional argument but 4 were given
Myprint([1,2,3,4])
<class 'list'>
1 2 3 4 
Myprint((1,2,3,4))
<class 'tuple'>
1 2 3 4 
def Myprint(*args):
    print(type(args))
    for val in args:
        print(val, end=" ")

        


Myprint(1,2,3,4)
<class 'tuple'>
1 2 3 4 
Myprint([1,2,3,4])
<class 'tuple'>
[1, 2, 3, 4] 
Myprint([1,2,3,4],1,2,3,True)
<class 'tuple'>
[1, 2, 3, 4] 1 2 3 True 
def Myprint(*args):
    print(type(args))
    print(args)
    for val in args:
        print(val, end=" ")

        
Myprint([1,2,3,4])
<class 'tuple'>
([1, 2, 3, 4],)
[1, 2, 3, 4] 
Myprint(1,2,3,4)
<class 'tuple'>
(1, 2, 3, 4)
1 2 3 4 
Myprint([1,2,3,4],1,2,3,True)
<class 'tuple'>
([1, 2, 3, 4], 1, 2, 3, True)
[1, 2, 3, 4] 1 2 3 True 


def myprint (*args, mysep=' ', myend='\n'):
    for val in args:
        print(val,end=mysep)
    print(end=myend)

    
myprint()

myprint("sdf")
sdf 
myprint(1,2,3)
1 2 3 


def summ(*args):
    return sum(args)

def summ(*args):
    res=0
    for i in args:
        res+=i
    return res

summ(1,2,3,4,5)
15



def cost_count(*money):
    res=0
    days = len(money)
    for i in money:
        res += i
    return f"total cost for {days} days is: {res}\n"

cost_counter(15,44,100,4,9)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    cost_counter(15,44,100,4,9)
NameError: name 'cost_counter' is not defined. Did you mean: 'cost_count'?
cost_count(15,44,100,4,9)
'total cost for 5 days is: 172\n'

 


li = [1,2,3]
a,*b = li
b
[2, 3]


def family(**kwargs):
    print(kwargs)
    print(type(kwargs))

    

family(Nik="dad", Maria="mom")
{'Nik': 'dad', 'Maria': 'mom'}
<class 'dict'>

family(Nik="dad", Maria="mom",1=11)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
family(Nik="dad", Maria="mom",Sis=11)
{'Nik': 'dad', 'Maria': 'mom', 'Sis': 11}
<class 'dict'>

 







def func(a,b,*args):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    

func(1,2,3,4,5)
1 <class 'int'>
2 <class 'int'>
(3, 4, 5) <class 'tuple'>
def func(*args,a=100,b=50):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    
func(1,2,3,4,5)
100 <class 'int'>
50 <class 'int'>
(1, 2, 3, 4, 5) <class 'tuple'>
def func(*args):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
KeyboardInterrupt


def func(a=100,b=50,*args):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    
func(1,2,3,4,5,5)
1 <class 'int'>
2 <class 'int'>
(3, 4, 5, 5) <class 'tuple'>
def func(a=100,b=50,*args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))

    
func(1,2,3,4,5)
1 <class 'int'>
2 <class 'int'>
(3, 4, 5) <class 'tuple'>
{} <class 'dict'>
func(1,2)
1 <class 'int'>
2 <class 'int'>
() <class 'tuple'>
{} <class 'dict'>
func(1,2,3,4,5,dad="qqqqq", mom="dcc")
1 <class 'int'>
2 <class 'int'>
(3, 4, 5) <class 'tuple'>
{'dad': 'qqqqq', 'mom': 'dcc'} <class 'dict'>




li1=[1,2,3,4]
li2=[3,4,5,6,7,8]
liu3 = [li1,li2]
liu3
[[1, 2, 3, 4], [3, 4, 5, 6, 7, 8]]
liu3 = [*li1,*li2]
liu3
[1, 2, 3, 4, 3, 4, 5, 6, 7, 8]


di1={1:11,2:22}
di1
{1: 11, 2: 22}
di2={4:11,5:22}
di2
{4: 11, 5: 22}
di3={**di1,**di2}
di3
{1: 11, 2: 22, 4: 11, 5: 22}
di3={di1,di2}
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    di3={di1,di2}
TypeError: unhashable type: 'dict'




def con(bit):
    return bit/3.5

con
<function con at 0x000001AABE2800E0>
b1=95000
con(b1)
27142.85714285714
def con(bit):
    return bit*3.5


con(b1)
332500.0

lambda bit: bit*3.5
<function <lambda> at 0x000001AABE2771A0>
(lambda bit: bit*3.5)(b1)
332500.0


1+99+1234*3+(lambda bit: bit*3.5)(b1)
336302.0



li=[1,2,3,4,5,6,7]
iterator = iter(li)
next(iterator)
1
next(iterator)
2
next(iterator)
3
next(iterator)
4
next(iterator)
5
next(iterator)
6
next(iterator)
7
next(iterator)
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    next(iterator)
StopIteration
for i in li:
    next(iterator)

    
Traceback (most recent call last):
  File "<pyshell#218>", line 2, in <module>
    next(iterator)
StopIteration
for i in li:
    print(i)

    
1
2
3
4
5
6
7





class Feb():
    def __init__(self,fn):
        self.fn=fn
        self.i=0
        self.f1=self.f2=1
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.fn:
            raise StopIteration
        if self.i == 1 or self.i == 2
        
SyntaxError: expected ':'
class Feb():
    def __init__(self,fn):
        self.fn=fn
        self.i=0
        self.f1=self.f2=1
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.fn:
            raise StopIteration
        if self.i == 1 or self.i == 2:
            return 1
        fret = self.f1 +self.f2
        self.f1, self.f2 = self.f2,fret

        
class Feb():
    def __init__(self,fn):
        self.fn=fn
        self.i=0
        self.f1=self.f2=1
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.fn:
            raise StopIteration
        if self.i == 1 or self.i == 2:
            return 1
        fret = self.f1 +self.f2
        self.f1, self.f2 = self.f2,fret
        return fret

    
febx = Feb(10)
for f in febx:
    print(f, end=" ")

    
1 1 2 3 5 8 13 21 34 55 





li =  [i** for i in range(100)]
SyntaxError: invalid syntax
li =  [i**2 for i in range(10)]
li
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



gen =  (i**2 for i in range(100))
gen
<generator object <genexpr> at 0x000001AABE1F2B50>
next(gen)
0
next(gen)
1
next(gen)
4
next(gen)
9
next(gen)
16
next(gen)
25



# func gen

def func(n):
    start = 0
    for i in range(n):
        start += 1
        return start

    

func(10)
1

func_gen=func(10)
func_gen
1
def func(n):
    start = 0
    for i in range(n):
        start += 1
        yield start

        
func_gen=func(10)

func_gen
<generator object func at 0x000001AABE1F3100>
next(func_gen)
1
next(func_gen)
2
next(func_gen)
3
next(func_gen)
4
for i in func(10):
    pfrint(i)

    
Traceback (most recent call last):
  File "<pyshell#293>", line 2, in <module>
    pfrint(i)
NameError: name 'pfrint' is not defined. Did you mean: 'print'?
for i in func(10):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
gen =  (i**2 for i in range(10))
for i in gen:
    print(i)

    
0
1
4
9
16
25
36
49
64
81




#map filter zip

li = [1,2,3]
li2 = ["one","two","three"]
res = list(zip(li2,li1))
res
[('one', 1), ('two', 2), ('three', 3)]


li=[1,2,3,4,5]
li
[1, 2, 3, 4, 5]
m = map(lambd x: x**2/2,li)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
m = map(lambda x: x**2/2,li)
m
<map object at 0x000001AABE265810>
li = list(m)
li
[0.5, 2.0, 4.5, 8.0, 12.5]
m
<map object at 0x000001AABE265810>
for i in m:
    print(m)

    
m = map(lambda x: x**2/2,li)
for i in m:
    print(m)

    
<map object at 0x000001AABE264940>
<map object at 0x000001AABE264940>
<map object at 0x000001AABE264940>
<map object at 0x000001AABE264940>
<map object at 0x000001AABE264940>
m = map(lambda x: x**2/2,li)
for i in m:
    print(i)

    
0.125
2.0
10.125
32.0
78.125


li = [1,2,3,4,5,6,7,8]
for i in filter(lambda x: x%2 != 0, li):
    print(i)

    
1
3
5
7


def func():
    number = 10
    return number

func()
10
def func():
    number = 10
    def inner():
        val = 5 + number
        return val
    return inner

func()
<function func.<locals>.inner at 0x000001AABE274040>
number
Traceback (most recent call last):
  File "<pyshell#343>", line 1, in <module>
    number
NameError: name 'number' is not defined
res = func()
res
<function func.<locals>.inner at 0x000001AABE26B060>
res()
15
res
<function func.<locals>.inner at 0x000001AABE26B060>
res.__closer__
Traceback (most recent call last):
  File "<pyshell#348>", line 1, in <module>
    res.__closer__
AttributeError: 'function' object has no attribute '__closer__'. Did you mean: '__closure__'?
res.__closure__
(<cell at 0x000001AABE264760: int object at 0x00007FFA2E5224C8>,)



issubclass(float,object)
True
issubclass(list,type)
False
isinstance(float,object)
True
isinstance(float,type)
True
class D:
    pass

issubclass(D,object)
True
issubclass(D,list)
False
isinstance(D,float)
False
isinstance(D,type)
True


dog = type("Dog", (object,),{"count":1})
dog
<class '__main__.Dog'>
dog.__name__
'Dog'
dog.__bases__
(<class 'object'>,)
dog.__dict_
Traceback (most recent call last):
  File "<pyshell#369>", line 1, in <module>
    dog.__dict_
AttributeError: type object 'Dog' has no attribute '__dict_'. Did you mean: '__dict__'?
>>> dog.__dict__
mappingproxy({'count': 1, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None})
>>> class Dog:
...     counter=1
... 
...     
>>> d1 = dog()
>>> di
Traceback (most recent call last):
  File "<pyshell#375>", line 1, in <module>
    di
NameError: name 'di' is not defined. Did you mean: 'li'?
>>> d1
<__main__.Dog object at 0x000001AABE126CF0>
>>> d2 = Dog1()
Traceback (most recent call last):
  File "<pyshell#377>", line 1, in <module>
    d2 = Dog1()
NameError: name 'Dog1' is not defined. Did you mean: 'Dog'?
>>> d2
Traceback (most recent call last):
  File "<pyshell#378>", line 1, in <module>
    d2
NameError: name 'd2' is not defined. Did you mean: 'u2'?
>>> d2 = Dog()
>>> d2
<__main__.Dog object at 0x000001AABE126E40>

Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.




enumerate()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    enumerate()
TypeError: enumerate() missing required argument 'iterable'
li = [1,2,3,4]
li
[1, 2, 3, 4]
enumerate(li)
<enumerate object at 0x000002313B3F5440>
li
[1, 2, 3, 4]
for i, v in enumerate(li,5):
    print(i,v)

    
5 1
6 2
7 3
8 4
bool(1)
True
bool()
False
bool("")
False
bool(" ")
True
ind = [1,2,3,4,5,6,]
ind = [1,2,3,4,5,6]
ind = [1,0,1,1,0,1]
bool(ind[0])
True
if bool(ind[0]) and bool(ind[1]) and bool(ind[2]) and bool(ind[3]):
    print("OK")
    else:
        
SyntaxError: invalid syntax
if bool(ind[0]) and bool(ind[1]) and bool(ind[2]) and bool(ind[3]):
    print("OK")
else:
    print("ploxo")

    
ploxo
ind = [1,1,1,1,1]
if bool(ind[0]) and bool(ind[1]) and bool(ind[2]) and bool(ind[3]):
    print("OK")
else:
    print("ploxo")

    
OK
#all any
if all(ind):
    print("OK")
else:
    print("ploxo")

    
OK
ind = [1,0,1,1]
if all(ind):
    print("OK")
else:
    print("ploxo")

ploxo


if any(ind):
    print("OK")
else:
    print("ploxo")

OK
ind = [1,1,1,1]
if any(ind):
    print("OK")
else:
    print("ploxo")

    
OK
>>> 
>>> 
>>> ind = [0,0,0]
>>> if any(ind):
...     print("OK")
... else:
...     print("ploxo")
... 
ploxo
>>> 
>>> 

>>> def my_all(iterable):
...     flag = None
...     for val in iterable:
...         if not bool(val):
...             return False
...         flag = True
...     return flag
... 
>>> li
[1, 2, 3, 4]
>>> my_all(li)
True
>>> li = [1,2,3,4,5,0]
>>> my_all(li)
False
>>> my_all([1,2,0,44])
False
>>> 
>>> 


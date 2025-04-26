Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print(123)
123
2+3
5
li = [1,2,3]
li
[1, 2, 3]
len(li)
3


f = ("name", "phone", 1233)
type(f)
<class 'tuple'>

print (f)
('name', 'phone', 1233)

#empty tupels
tp = ()
type (tp)
<class 'tuple'>
tp
()
tp1 = tuple()
tp1
()
type(tp1)
<class 'tuple'>
isinstance(tp, tuple)
True


li = []
li
[]
li = [1]
li
[1]
se = {1}
se
{1}
tp = (1)
tp
1
type(tp)
<class 'int'>
tp = (1,)
tp
(1,)
type(tp)
<class 'tuple'>
tp
(1,)
tp = 1,
tp
(1,)
type(tp)
<class 'tuple'>
li = [1,2,3]
se = {1,2,3}
st = "123e"
i = 1
f = 4.3
tp = (2,)
tp
(2,)
se
{1, 2, 3}
li
[1, 2, 3]
st
'123e'
i
1
f
4.3

tp = 1,2,3,4
tp
(1, 2, 3, 4)
tp = (1,2,3)
tp[0]
1
tp[1]
2
tp[2]
3
tp[3]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    tp[3]
IndexError: tuple index out of range
li
[1, 2, 3]
li[3]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    li[3]
IndexError: list index out of range
len(tp)
3




tp
(1, 2, 3)
tp[-1]
3
tp[::-1]
(3, 2, 1)
tp
(1, 2, 3)


tp = (1., 2., 3., .4,)
tp
(1.0, 2.0, 3.0, 0.4)

li
[1, 2, 3]
li.append(1111)
li
[1, 2, 3, 1111]
tp.append(111)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    tp.append(111)
AttributeError: 'tuple' object has no attribute 'append'
tp[1] = 33
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    tp[1] = 33
TypeError: 'tuple' object does not support item assignment
li
[1, 2, 3, 1111]
tp
(1.0, 2.0, 3.0, 0.4)
tp = (1.0, 2.0, 3.0, 0.4, li)
tp
(1.0, 2.0, 3.0, 0.4, [1, 2, 3, 1111])
li.pop()
1111
tp
(1.0, 2.0, 3.0, 0.4, [1, 2, 3])





#unpack

li = [1,2,3]
tp = (1,2,3)


a,b,c,d = tp
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a,b,c,d = tp
ValueError: not enough values to unpack (expected 4, got 3)
a,b,c = tp
a
1
b
2
c
3
st
'123e'
a,b,c,d = st
a
'1'
s
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s
NameError: name 's' is not defined. Did you mean: 'se'?
d
'e'
tp
(1, 2, 3)
n, *fil = tp
n
1
fil
[2, 3]


def ret():
    return(1,2,3,4,5)

ret()
(1, 2, 3, 4, 5)
res = ret()
re
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    re
NameError: name 're' is not defined. Did you mean: 'se'? Or did you forget to import 're'?
res
(1, 2, 3, 4, 5)
g, *h = ret
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    g, *h = ret
TypeError: cannot unpack non-iterable function object
g, *h = ret()
g
1
h
[2, 3, 4, 5]
h.append(9999)
h
[2, 3, 4, 5, 9999]


def ret():
    return(1,2,3,4,5)

a, *b,c= ret()
a
1
b
[2, 3, 4]
c
5
a, *b,c,d= ret()
a
1
b
[2, 3]
c
4
d
5
a, *b,c,d,e= ret()
a
1
b
[2]
c
3
d
4
e
5
ret
<function ret at 0x0000014FFE701760>
ret()
(1, 2, 3, 4, 5)
*a = ret()
SyntaxError: starred assignment target must be in a list or tuple

*a,b = ret()
a
[1, 2, 3, 4]
b
5


tp = 1,
tp
(1,)
tp = 3.,
tp
(3.0,)


tp = (1,2,3,4,5,6)
tp
(1, 2, 3, 4, 5, 6)
tp[:3]
(1, 2, 3)
tp[::2]
(1, 3, 5)
tp[-1]
6
tp[:-1]
(1, 2, 3, 4, 5)
tp2 = (2,3,4,5,6)
tp + tp2
(1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6)
tp
(1, 2, 3, 4, 5, 6)
tp*3
(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)


tp
(1, 2, 3, 4, 5, 6)
6 in tp
True
44 in tp
False

3in tp
True
3 in tp
True
tp
(1, 2, 3, 4, 5, 6)
tp2
(2, 3, 4, 5, 6)
tp, tp2 = tp2, tp
tp
(2, 3, 4, 5, 6)
tp2
(1, 2, 3, 4, 5, 6)
len(tp)
5

tp
(2, 3, 4, 5, 6)
tp[::3]
(2, 5)
tp[:3]
(2, 3, 4)
tp[-1]
6
(22,33,44)
(22, 33, 44)
1 + (22,3)
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    1 + (22,3)
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
res = tp[:3] + (22,33,44) +tp[4:]
res
(2, 3, 4, 22, 33, 44, 6)


del res
res
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    res
NameError: name 'res' is not defined. Did you mean: 'ret'?
tp
(2, 3, 4, 5, 6)
tp.count(3)
1
tp.count(22)
0
tp.index(2)
0


n = int(input())
5
if n in tp:
    print('index:', tp.index(n))
    print("value:", tp[tp.index(n)])

    
index: 3
value: 5
tp
(2, 3, 4, 5, 6)
tp = tp[:3]
tp
(2, 3, 4)
tp = (list(tp).pop().pop())
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    tp = (list(tp).pop().pop())
AttributeError: 'int' object has no attribute 'pop'
tp = list(tp)
tp
[2, 3, 4]
tp.pop()
4
tp
[2, 3]
tp = tuple(tp)
tp
(2, 3)



for i in tp:
    print(i**2)

    
4
9
for i in range(len(tp)):
    print(i,tp[i])

    
0 2
1 3
tp = (1,2,3,4,5,6)
tp
(1, 2, 3, 4, 5, 6)




#dict
di = {}
type(di)
<class 'dict'>
di = dict()
di
{}


di = {1:"one", 2:"two"}
di
{1: 'one', 2: 'two'}
di = {1:"one", 2:"two", 3: 2234, 4: (1,2,3,4)}
di
{1: 'one', 2: 'two', 3: 2234, 4: (1, 2, 3, 4)}



di[3]
2234
di[]4
SyntaxError: invalid syntax
di[4]
(1, 2, 3, 4)
di[6]
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    di[6]
KeyError: 6
di = {1:"one", 2:"two", 3: 2234, (1,2):"tuple"}
di[(1,2)]
'tuple'
di["two"]
Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    di["two"]
KeyError: 'two'
di = {{1,2,3}:10,}
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    di = {{1,2,3}:10,}
TypeError: unhashable type: 'set'
di = {[1,2,3]:10,}
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    di = {[1,2,3]:10,}
TypeError: unhashable type: 'list'



hash
<built-in function hash>
help(hash)
Help on built-in function hash in module builtins:

hash(obj, /)
    Return the hash value for the given object.

    Two objects that compare equal must also have the same hash value, but the
    reverse is not necessarily true.

hash(2)
2
hash("23432")
2189920593023178000
hash(3)
3
di = {2:2345 , 2:1111111111}
di
{2: 1111111111}
hash(1)
1
hash(0)
0
hash("")
0
hash(False)
0
hash(True)
1




di {1:111}
SyntaxError: invalid syntax
di = {1:111}
di[1]
111
di[True]
111
di {1:111,0:1234567}
SyntaxError: invalid syntax
di = {1:111,0:1234567}
di[0]
1234567
di[False]
1234567
di[""]
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    di[""]
KeyError: ''


di
{1: 111, 0: 1234567}
di = {1:111,0:1234567, "":""em}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
di = {1:111,0:1234567, "":"em"}
di[0]
1234567
di[]
SyntaxError: invalid syntax
di[""]
'em'
di[False]
1234567

di
{1: 111, 0: 1234567, '': 'em'}
di.egt("")
Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    di.egt("")
AttributeError: 'dict' object has no attribute 'egt'
di.get("")
'em'
di.get()1234567
SyntaxError: invalid syntax
di.get(1234567)
di.keys()
dict_keys([1, 0, ''])
di.values()
dict_values([111, 1234567, 'em'])
di.popitem()
('', 'em')
di
{1: 111, 0: 1234567}
di.pop(0)
1234567
di
{1: 111}
di.update({22:'wer'})
di
{1: 111, 22: 'wer'}
di.update({1:-1})
di
{1: -1, 22: 'wer'}

1 in di
True
33 in di
False
for k in di.keys():
    print(k)

    
1
22
for k, v in di.item():
    print(k, v)

    
Traceback (most recent call last):
  File "<pyshell#314>", line 1, in <module>
    for k, v in di.item():
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
for k, v in di.items():
    print(k, v)

    
1 -1
22 wer


di = {s(i):i**3for i in range(10)}
Traceback (most recent call last):
  File "<pyshell#318>", line 1, in <module>
    di = {s(i):i**3for i in range(10)}
NameError: name 's' is not defined. Did you mean: 'se'?
di = {s(i):i**3 for i in range(10)}
Traceback (most recent call last):
  File "<pyshell#319>", line 1, in <module>
    di = {s(i):i**3 for i in range(10)}
NameError: name 's' is not defined. Did you mean: 'se'?
di = {str(i):i**3 for i in range(10)}
di
{'0': 0, '1': 1, '2': 8, '3': 27, '4': 64, '5': 125, '6': 216, '7': 343, '8': 512, '9': 729}





#Lab


()
()
sc =  ()
sc
()
6
6
sc += (6,)
sc += (9,)
sc += (10,)
sc
(6, 9, 10)
sum(sc)
25
len(sc)
3
sum(sc)/len(sc)
8.333333333333334
round((sum(sc)/len(sc)),2)
8.33


dedf avg(sc):
    
SyntaxError: invalid syntax
def av(sc):
    return round((sum(sc)/len(sc)),2)


sc
(6, 9, 10)
av(sc)
8.33


stud = {}
stud
{}
def new(name, grade):
    if len(stud) < 2:
        return False
    name = name.title()
    if name in stud:
        stud.update(stud.get(name) + (grade,))
    else:
        stud.update({name:(grade, )})
    return True

stud
{}
new("petya petrov", 7)
False
def new(name, grade):
    if len(name) < 2:
        return False
    name = name.title()
    if name in stud:
        stud.update(stud.get(name) + (grade,))
    else:
        stud.update({name:(grade, )})
    return True

new("petya petrov", 7)
True
stud
{'Petya Petrov': (7,)}
new("petya petrov", 10)
Traceback (most recent call last):
  File "<pyshell#371>", line 1, in <module>
    new("petya petrov", 10)
  File "<pyshell#368>", line 6, in new
    stud.update(stud.get(name) + (grade,))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
def new(name, grade):
    if len(name) < 2:
        return False
    name = name.title()
    if name in stud:
        stud.update({stud.get(name) + (grade,)})
    else:
        stud.update({name:(grade, )})
    return True

new("petya petrov", 10)
True
stud
{'Petya Petrov': (7,), 7: 10}
def new(name, grade):
    if len(name) < 2:
        return False
    name = name.title()
    if name in stud:
        stud.update({name: stud.get(name) + (grade,)})
    else:
        stud.update({name:(grade, )})
    return True

new("petya petrov", 10)
True
stud = {}
KeyboardInterrupt
new("petya petrov", 7)
True
stud
{'Petya Petrov': (7,)}
new("petya petrov", 10)
True
stud
{'Petya Petrov': (7, 10)}
new("petya petrov", 6)
True
stud
{'Petya Petrov': (7, 10, 6)}
av(stud.get("Petya Petrov"))
7.67
def av(sc):
    return round((sum(sc)/len(sc)),2)

oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')
1 - new grade, 2 - show avg, 3 - show grades, guit - exit

while oper != "guit":
    match oper:
        case"1":



KeyboardInterrupt
def show_g():
    for k, v in stud.item():
        print("name", k)
        print("grades", v)

        
show_g
<function show_g at 0x0000014FFE727060>
show_g()
Traceback (most recent call last):
  File "<pyshell#403>", line 1, in <module>
    show_g()
  File "<pyshell#401>", line 2, in show_g
    for k, v in stud.item():
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
def show_g():
    print("show_d")
    for k, v in stud.item():
        print("name", k)
        print("grades", v)

        
show_g()
show_d
Traceback (most recent call last):
  File "<pyshell#406>", line 1, in <module>
    show_g()
  File "<pyshell#405>", line 3, in show_g
    for k, v in stud.item():
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
stud
{'Petya Petrov': (7, 10, 6)}
def show_g():
    print("show_d")
    for k, v in stud.items():
        print("name", k)
        print("grades", v)

        

show_g
<function show_g at 0x0000014FFE702F20>
show_g()
show_d
name Petya Petrov
grades (7, 10, 6)
def show_avg():
    print("show avg")
    for k, v in stud.items():
        print("name", k)
        print("avg", av(v))

        
show_avg()
show avg
name Petya Petrov
avg 7.67

while oper != "guit":
    match oper:
        case"1":
            name = input("Put full name:")
            grad = int(input("Put grade:"))
            new(name, grade)
        case "2":
            show_avg()
        case "3":
            show_g()
        case _:
            print("ne ponial")
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')

    
ne ponial
1 - new grade, 2 - show avg, 3 - show grades, guit - exit
ne ponial
1 - new grade, 2 - show avg, 3 - show grades, guit - exit1
Put full name:vasia petRov
Put grade:9
Traceback (most recent call last):
  File "<pyshell#428>", line 6, in <module>
    new(name, grade)
NameError: name 'grade' is not defined. Did you mean: 'grad'?
while oper != "guit":
    match oper:
        case"1":
            name = input("Put full name:")
            grad = int(input("Put grade:"))
            new(name, stud)
        case "2":
            show_avg()
        case "3":
            show_g()
        case _:
            print("ne ponial")
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')

    
Put full name:vasSia petrOv
Put grade:9
True
1 - new grade, 2 - show avg, 3 - show grades, guit - exit3
show_d
name Petya Petrov
grades (7, 10, 6)
name Vassia Petrov
grades ({'Petya Petrov': (7, 10, 6), 'Vassia Petrov': (...)},)
1 - new grade, 2 - show avg, 3 - show grades, guit - exit1
Put full name:Vassia Petrov
Put grade:7
True
1 - new grade, 2 - show avg, 3 - show grades, guit - exit2
show avg
name Petya Petrov
avg 7.67
name Vassia Petrov
Traceback (most recent call last):
  File "<pyshell#430>", line 8, in <module>
    show_avg()
  File "<pyshell#416>", line 5, in show_avg
    print("avg", av(v))
  File "<pyshell#388>", line 2, in av
    return round((sum(sc)/len(sc)),2)
TypeError: unsupported operand type(s) for +: 'int' and 'dict'
while oper != "guit":
    match oper:
        case"1":
            name = input("Put full name:")
            grad = int(input("Put grade:"))
            new(name, stud)
        case "2":
            show_avg()
        case "3":
            show_g()
        case _:
            print("ne ponial")
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')

    
show avg
name Petya Petrov
avg 7.67
name Vassia Petrov
Traceback (most recent call last):
  File "<pyshell#432>", line 8, in <module>
    show_avg()
  File "<pyshell#416>", line 5, in show_avg
    print("avg", av(v))
  File "<pyshell#388>", line 2, in av
    return round((sum(sc)/len(sc)),2)
TypeError: unsupported operand type(s) for +: 'int' and 'dict'
while oper != "guit":
    match oper:
        case"1":
            name = input("Put full name:")
            grad = int(input("Put grade:"))
            new(name, stud)
        case "2":
            show_avg()
        case "3":
            show_g()
        case _:
            print("ne ponial")
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')

    
show avg
name Petya Petrov
avg 7.67
name Vassia Petrov
Traceback (most recent call last):
  File "<pyshell#434>", line 8, in <module>
    show_avg()
  File "<pyshell#416>", line 5, in show_avg
    print("avg", av(v))
  File "<pyshell#388>", line 2, in av
    return round((sum(sc)/len(sc)),2)
TypeError: unsupported operand type(s) for +: 'int' and 'dict'
oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')
1 - new grade, 2 - show avg, 3 - show grades, guit - exit1
while oper != "guit":
    match oper:
        case"1":
            name = input("Put full name:")
            grad = int(input("Put grade:"))
            new(name, stud)
        case "2":
            show_avg()
        case "3":
            show_g()
        case _:
            print("ne ponial")
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')

    
Put full name:Vassia Petrov
Put grade:2
True
1 - new grade, 2 - show avg, 3 - show grades, guit - exit3
show_d
name Petya Petrov
grades (7, 10, 6)
name Vassia Petrov
grades ({'Petya Petrov': (7, 10, 6), 'Vassia Petrov': (...)}, {'Petya Petrov': (7, 10, 6), 'Vassia Petrov': (...)}, {'Petya Petrov': (7, 10, 6), 'Vassia Petrov': (...)})
1 - new grade, 2 - show avg, 3 - show grades, guit - exit2
show avg
name Petya Petrov
avg 7.67
name Vassia Petrov
Traceback (most recent call last):
  File "<pyshell#437>", line 8, in <module>
    show_avg()
  File "<pyshell#416>", line 5, in show_avg
    print("avg", av(v))
  File "<pyshell#388>", line 2, in av
    return round((sum(sc)/len(sc)),2)
TypeError: unsupported operand type(s) for +: 'int' and 'dict'
show_avg()
show avg
name Petya Petrov
avg 7.67
name Vassia Petrov
Traceback (most recent call last):
  File "<pyshell#438>", line 1, in <module>
    show_avg()
  File "<pyshell#416>", line 5, in show_avg
    print("avg", av(v))
  File "<pyshell#388>", line 2, in av
    return round((sum(sc)/len(sc)),2)
TypeError: unsupported operand type(s) for +: 'int' and 'dict'
stud
{'Petya Petrov': (7, 10, 6), 'Vassia Petrov': ({...}, {...}, {...})}
stud.pop()
Traceback (most recent call last):
  File "<pyshell#440>", line 1, in <module>
    stud.pop()
TypeError: pop expected at least 1 argument, got 0
stud.pop('Vassia Petrov')
({'Petya Petrov': (7, 10, 6)}, {'Petya Petrov': (7, 10, 6)}, {'Petya Petrov': (7, 10, 6)})
stud
{'Petya Petrov': (7, 10, 6)}
def main():
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')
    while oper != "guit":
        match oper:
            case"1":
                name = input("Put full name:")
                grad = int(input("Put grade:"))
                new(name, grade)
            case "2":
                show_avg()
            case "3":
                show_g()
            case _:
                print("ne ponial")
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')

    
main()
1 - new grade, 2 - show avg, 3 - show grades, guit - exitguit
1 - new grade, 2 - show avg, 3 - show grades, guit - exitguit
main()
1 - new grade, 2 - show avg, 3 - show grades, guit - exit3
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
show_d
name Petya Petrov
grades (7, 10, 6)
Traceback (most recent call last):
  File "<pyshell#447>", line 1, in <module>
    main()
  File "<pyshell#445>", line 12, in main
    show_g()
  File "<pyshell#409>", line 5, in show_g
    print("grades", v)
KeyboardInterrupt
stud
{'Petya Petrov': (7, 10, 6)}

def av(sc):
    return round((sum(sc)/len(sc)),2)

av(sc)
8.33
def show_g():
    for k, v in stud.item():
        print("name", k)
        print("grades", v)

show_g
<function show_g at 0x0000014FFE6FAFC0>
show_g()
Traceback (most recent call last):
  File "<pyshell#454>", line 1, in <module>
    show_g()
  File "<pyshell#452>", line 2, in show_g
    for k, v in stud.item():
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
def show_g():
    for k, v in stud.items():
        print("name", k)
        print("grades", v)

        
shoe_g()
Traceback (most recent call last):
  File "<pyshell#457>", line 1, in <module>
    shoe_g()
NameError: name 'shoe_g' is not defined. Did you mean: 'show_g'?
show_g()
name Petya Petrov
grades (7, 10, 6)
def show_avg():
    print("show avg")
    for k, v in stud.items():
        print("name", k)
        print("avg", av(v))

        
show_avg()
show avg
name Petya Petrov
avg 7.67

def new(name, grade):
    if len(name) < 2:
        return False
    name = name.title()
    if name in stud:
        stud.update({name: stud.get(name) + (grade,)})
    else:
        stud.update({name:(grade, )})
    return True

new("Petya Petrov", 10)
True
stud
{'Petya Petrov': (7, 10, 6, 10)}

def main():
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')
    while oper != "guit":
        match oper:
            case "1":
                name = input("Put full name:")
                grad = int(input("Put grade:"))
                new(name, grade)
            case "2":
                show_avg()
            case "3":
                show_g()
            case _:
                print("ne ponial")
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')

    
main()
1 - new grade, 2 - show avg, 3 - show grades, guit - exitguit
1 - new grade, 2 - show avg, 3 - show grades, guit - exit
main
<function main at 0x0000014FFE725DA0>
main()
1 - new grade, 2 - show avg, 3 - show grades, guit - exit1
Put full name:SSs vcdsa
Put grade:5
Traceback (most recent call last):
  File "<pyshell#471>", line 1, in <module>
    main()
  File "<pyshell#468>", line 8, in main
    new(name, grade)
NameError: name 'grade' is not defined. Did you mean: 'grad'?
def main():
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')
    while oper != "guit":
        match oper:
            case "1":
                name = input("Put full name:")
                grade = int(input("Put grade:"))
                new(name, grade)
            case "2":
                show_avg()
            case "3":
                show_g()
            case _:
                print("ne ponial")
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')

    
main()
1 - new grade, 2 - show avg, 3 - show grades, guit - exit1
Put full name:sade hjklo
Put grade:4
Put full name:
Put grade:
Traceback (most recent call last):
  File "<pyshell#474>", line 1, in <module>
    main()
  File "<pyshell#473>", line 7, in main
    grade = int(input("Put grade:"))
ValueError: invalid literal for int() with base 10: ''
main()
1 - new grade, 2 - show avg, 3 - show grades, guit - exit2
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklodef main():
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')
    while oper != "guit":
        match oper:
            case "1":
                name = input("Put full name:")
                grad = int(input("Put grade:"))
                new(name, grade)
            case "2":
                show_avg()
            case "3":
                show_g()
            case _:
                print("ne ponial")
    oper = input('1 - new grade, 2 - show avg, 3 - show grades, guit - exit')
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0
show avg
name Petya Petrov
avg 8.25
name Sade Hjklo
avg 4.0Traceback (most recent call last):
  File "<pyshell#475>", line 1, in <module>
    main()
  File "<pyshell#473>", line 10, in main
    show_avg()
  File "<pyshell#460>", line 5, in show_avg
    print("avg", av(v))
KeyboardInterrupt
main()
1 - new grade, 2 - show avg, 3 - show grades, guit - exit3
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
grades (4,)
name Petya Petrov
grades (7, 10, 6, 10)
name Sade Hjklo
Traceback (most recent call last):
  File "<pyshell#476>", line 1, in <module>
    main()
  File "<pyshell#473>", line 12, in main
    show_g()
  File "<pyshell#456>", line 3, in show_g
    print("name", k)
KeyboardInterrupt































def avg(score):
    """ Функция для вычисления среднего бала студента.
    Arguments:
    score - tuple - набор оценок.
    Returns:
    float - средний бал, 2 знака послсе запятой.
    """
    return round((sum(score)/len(score)),2)

avg(10)
Traceback (most recent call last):
  File "<pyshell#495>", line 1, in <module>
    avg(10)
  File "<pyshell#494>", line 8, in avg
    return round((sum(score)/len(score)),2)
TypeError: 'int' object is not iterable
avg({1,2,3})
2.0


def new_grade(student_name, grade):
    """Функция для добавления новой оценки студенту.
    Arguments:
    student_name - str - имя, не менее 2-х символов.
    grade - int - оценка.
    Returns:
    True - если оценка добавлен ауспешно.
    False - если имя меньше 2 символов.
    """
    if len(student_name) < 2:
        return False
    
    student_name = student_name.title()

    if student_name in student_grades:
        student_grades.update({student_name: student_grades.get(student_name) + (grade,)})
    else:
        student_grades.update({student_name:(grade, )})

    return True

student_grades = {10,8,5,9}
student_name = "vasia petrov"
new_grade("vasia petrov", 2)
True
student_name
'vasia petrov'
student_name = student_name.title()
student_name
'Vasia Petrov'
student_grades
{'Vasia Petrov', 5, 8, 9, 10}


def show_grades():
    print("show_grades")
    for key, value in student_grades.items():
        print("name:", key)
        print("grades:", value)


show_gradess()
Traceback (most recent call last):
  File "<pyshell#512>", line 1, in <module>
    show_gradess()
NameError: name 'show_gradess' is not defined. Did you mean: 'show_grades'?
show_grades()
show_grades
Traceback (most recent call last):
  File "<pyshell#513>", line 1, in <module>
    show_grades()
  File "<pyshell#510>", line 3, in show_grades
    for key, value in student_grades.items():
AttributeError: 'set' object has no attribute 'items'
student_grades
{'Vasia Petrov', 5, 8, 9, 10}
show_grades()
show_grades
Traceback (most recent call last):
  File "<pyshell#515>", line 1, in <module>
    show_grades()
  File "<pyshell#510>", line 3, in show_grades
    for key, value in student_grades.items():
AttributeError: 'set' object has no attribute 'items'
def show_grades():
    print("show_grades")
    for key, value in student_grades.items():
        print("name:", key)
        print("grades:", value)

        
show_grades()
show_grades
Traceback (most recent call last):
  File "<pyshell#518>", line 1, in <module>
    show_grades()
  File "<pyshell#517>", line 3, in show_grades
    for key, value in student_grades.items():
AttributeError: 'set' object has no attribute 'items'
student_grades = {1,2,3,4}
show_grades()
show_grades
Traceback (most recent call last):
  File "<pyshell#520>", line 1, in <module>
    show_grades()
  File "<pyshell#517>", line 3, in show_grades
    for key, value in student_grades.items():
AttributeError: 'set' object has no attribute 'items'
def new_grade(student_name, grade):
    """Функция для добавления новой оценки студенту.
    Arguments:
    student_name - str - имя, не менее 2-х символов.
    grade - int - оценка.
...     Returns:
...     True - если оценка добавлен ауспешно.
...     False - если имя меньше 2 символов.
...     """
...     if len(student_name) < 2:
...         return False
...     
...     student_name = student_name.title()
... 
...     if student_name in student_grades:
...         student_grades.update({student_name: student_grades.get(student_name) + (grade,)})
...     else:
...         student_grades.update({student_name:(grade, )})
... 
...     return True
... 
>>> 
>>> new_grade()
Traceback (most recent call last):
  File "<pyshell#523>", line 1, in <module>
    new_grade()
TypeError: new_grade() missing 2 required positional arguments: 'student_name' and 'grade'
>>> new_grade('qwerzxd tyhujkil',6)
True
>>> show_grades()
show_grades
Traceback (most recent call last):
  File "<pyshell#525>", line 1, in <module>
    show_grades()
  File "<pyshell#517>", line 3, in show_grades
    for key, value in student_grades.items():
AttributeError: 'set' object has no attribute 'items'
>>> student_grades
{'Qwerzxd Tyhujkil', 1, 2, 3, 4}

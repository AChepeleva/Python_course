Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

1+1
2
print(23)
23
3 < 9
True
inpyt('->')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    inpyt('->')
NameError: name 'inpyt' is not defined. Did you mean: 'input'?
inpet()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    inpet()
NameError: name 'inpet' is not defined. Did you mean: 'input'?
input()
fghj
'fghj'
li = [1,2,3]
li
[1, 2, 3]
li.append(3456789)
li
[1, 2, 3, 3456789]
li.pop(3456789)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    li.pop(3456789)
IndexError: pop index out of range
li.pop()
3456789
li
[1, 2, 3]




#sign up
# name, phone, username

name = input("Name:")
Name:Sasha
tel = input("Tel:")
Tel:4567895677
username = input("Username:")
Username:Sss


def sign_up():
    name = input("Name:")
    tel = input("Tel:")
    username = input("Username:")
    user = [name, tel, username]
    print("User:", user, "was created.")

    

sing_up
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    sing_up
NameError: name 'sing_up' is not defined. Did you mean: 'sign_up'?
sign_up
<function sign_up at 0x000002CBC889CF40>
sing_up
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    sing_up
NameError: name 'sing_up' is not defined. Did you mean: 'sign_up'?
sign_up
<function sign_up at 0x000002CBC889CF40>
print
<built-in function print>

sign_up()
Name:Sasha
Tel:2345678
Username:sss
User: ['Sasha', '2345678', 'sss'] was created.


de fe():
    
SyntaxError: invalid syntax
def hel lo():
    
SyntaxError: expected '('
def hello:
    
SyntaxError: expected '('
def hello()
SyntaxError: expected ':'
def hellol ():
    print('hello')

    
def bye():
    print('bye!')

    
hello()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    hello()
NameError: name 'hello' is not defined. Did you mean: 'hellol'?
hellol()
hello
bye()
bye!
for i in range(5):
    hellol()
    bye()

    
hello
bye!
hello
bye!
hello
bye!
hello
bye!
hello
bye!

del bye
bye()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    bye()
NameError: name 'bye' is not defined

def sign_up():
    name = input("Name:")
    tel = input("Tel:")
    username = input("Username:")
    user = [name, tel, username]
    print("User:", user, "was created.")

    

print('Privet user')
Privet user
1+2
3
2+2
4
if 1 == 1:
    sign_up()

    
Name:sasha
Tel:123456
Username:sss
User: ['sasha', '123456', 'sss'] was created.

type(hellol)
<class 'function'>
hellol = 10
type(hellol)
<class 'int'>
hellol()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    hellol()
TypeError: 'int' object is not callable
print = 100
print
100

================================================ RESTART: Shell ================================================
print(1)
1


print(1,2,3, end="*")
1 2 3*
def convert():
    pass

def hel(name):
    print("welcome, {name}")

    
hel()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    hel()
TypeError: hel() missing 1 required positional argument: 'name'
hel("sasha')
    
SyntaxError: unterminated string literal (detected at line 1)
hel("ss")
    
welcome, {name}
def hel(name):
    print(f"welcome, {name}")

    
hel("ss")
welcome, ss
hel("ss","d")
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    hel("ss","d")
TypeError: hel() takes 1 positional argument but 2 were given

def convert(cm):
    cmm = cm%100
    mm = cm //100
    print(mm, cmm, sep=".")

    
convert(178)
1.78
convert(160)
1.60

mm
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    mm
NameError: name 'mm' is not defined
cmm
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    cmm
NameError: name 'cmm' is not defined
cm
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    cm
NameError: name 'cm' is not defined



if True:
    a = 1000

    
a
1000

def fun(num1, st1,li1):
    print(num1, st1,li1)
    dd = 10000
    print(dd)

    

num1
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    num1
NameError: name 'num1' is not defined
bb
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    bb
NameError: name 'bb' is not defined
fun(1,22,33)
1 22 33
10000
fun(1,"st",[2,3,4])
1 st [2, 3, 4]
10000

fun("st",[2,3,4])
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    fun("st",[2,3,4])
TypeError: fun() missing 1 required positional argument: 'li1'




def hel(name,ph):
    print("Name:",name)
    print("tel:", ph)

    
hel(1123,"ddd")
Name: 1123
tel: ddd
hel("fds",2433)
Name: fds
tel: 2433



def sign_up(name, phone, username):
    user = [name, phone, username]
    print("User:", user, "was created.")

    
sign_up("fghj",23)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    sign_up("fghj",23)
TypeError: sign_up() missing 1 required positional argument: 'username'

def sign_up(phone, username,name="wer"):
    user = [name, phone, username]
    print("User:", user, "was created.")

    

sign_up
<function sign_up at 0x000001B76A439620>
sign_up(12,"vvv")
User: ['wer', 12, 'vvv'] was created.
sign_up(12,"vvv","fd")
User: ['fd', 12, 'vvv'] was created.

def feed(name, ph, com="")
SyntaxError: expected ':'
def feed(name, ph, com=""):
    print(name, ph)

    
feed("sasha",1234)
sasha 1234
feed("sasha",1234,"dfvgbhnjmk")
sasha 1234
feed("sasha",1234,"dfvgbhnjmk","@")
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    feed("sasha",1234,"dfvgbhnjmk","@")
TypeError: feed() takes from 2 to 3 positional arguments but 4 were given





####

def add(a,b):
    print(f"{a} +{b} = {a+b}")

    
def sub(a,b):
    print(f"{a} - {b} = {a-b}")

    

def mul(a,b):
    print(f"{a} *{b} = {a*b}")

    
oper = inpet("exit + -")
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    oper = inpet("exit + -")
NameError: name 'inpet' is not defined. Did you mean: 'input'?
oper = input("exit + -")
exit + -
while oper != "exit":
    num1, num2 = int (input("n1:"), int(input("n2:")))
    if oper == "+":
        add(num1,num2)
    elif oper == "-":
        sub(num1,num2)
    elif oper == "*":
        mul(num1,num2)
    else:
        print("Ne ponel")
    oper = input("exit + -")

    
n1:1
n2:3
Traceback (most recent call last):
  File "<pyshell#186>", line 2, in <module>
    num1, num2 = int (input("n1:"), int(input("n2:")))
TypeError: cannot unpack non-iterable int object
while oper != "exit":
    num1, num2 = int (input("n1:"), int(input("n2:")))
    if oper == "+":
        add(num1,num2)
    elif oper == "-":
        sub(num1,num2)
    elif oper == "*":
        mul(num1,num2)
    else:
        print("Ne ponel")
    oper = input("exit + -")

    
n1:7
n2:8
Traceback (most recent call last):
  File "<pyshell#188>", line 2, in <module>
    num1, num2 = int (input("n1:"), int(input("n2:")))
TypeError: cannot unpack non-iterable int object
while oper != "exit":
    num1, num2 = int (input("n1:")), int(input("n2:"))
    if oper == "+":
        add(num1,num2)
    elif oper == "-":
        sub(num1,num2)
    elif oper == "*":
        mul(num1,num2)
    else:
        print("Ne ponel")
    oper = input("exit + -")

    
n1:7
n2:9
Ne ponel
exit + --
n1:7
n2:6
7 - 6 = 1
exit + -*
n1:6
n2:9
6 *9 = 54
exit + -exit

def main():
    oper = input("exit + -")
    while oper != "exit":
    num1, num2 = int (input("n1:")), int(input("n2:"))
    if oper == "+":
        add(num1,num2)
    elif oper == "-":
        sub(num1,num2)
    elif oper == "*":
        mul(num1,num2)
    else:
        print("Ne ponel")
    oper = input("exit + -")
    
SyntaxError: expected an indented block after 'while' statement on line 3

def main():
    oper = input("exit + -")
    while oper != "exit":
        num1, num2 = int (input("n1:")), int(input("n2:"))
        if oper == "+":
            add(num1,num2)
        elif oper == "-":
            sub(num1,num2)
        elif oper == "*":
            mul(num1,num2)
        else:
            print("Ne ponel")
        oper = input("exit + -")

        
def add(a,b):
    print(f"{a} +{b} = {a+b}")

    
def sub(a,b):
    print(f"{a} - {b} = {a-b}")

    

def mul(a,b):
    print(f"{a} *{b} = {a*b}")
    
SyntaxError: invalid syntax
def add(a,b):
    print(f"{a} +{b} = {a+b}")

    

name= input("sa")
sa
name
''
summa = add(3,2)
3 +2 = 5
summa
print(summa)
None
def add(a,b):
    print(f"{a} +{b} = {a+b}")
    return a+b

summa = add(3,4)
3 +4 = 7
summa
7
add
<function add at 0x000001B76A43D1C0>
add()
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    add()
TypeError: add() missing 2 required positional arguments: 'a' and 'b'
add(1,3)
1 +3 = 4
4
def hel (name):
    return "welcom" + name

hel("d")
'welcomd'
def sub(a,b):
    print(f"{a} - {b} = {a-b}")
    return a-b

def mul(a,b):
    print(f"{a} *{b} = {a*b}")
    return a*b

def main():
    oper = input("exit + -")
    while oper != "exit":
        num1, num2 = int (input("n1:")), int(input("n2:"))
        if oper == "+":
            res = add(num1,num2)
            print("result:", res)
        elif oper == "-":
            res = sub(num1,num2)
            print("result:", res)
        elif oper == "*":
            res = mul(num1,num2)
            print("result:", res)
        else:
            print("Ne ponel")
        oper = input("exit + -")

        
main()
exit + -+
n1:2
n2:3
2 +3 = 5
result: 5
exit + -
n1:
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    main()
  File "<pyshell#226>", line 4, in main
    num1, num2 = int (input("n1:")), int(input("n2:"))
ValueError: invalid literal for int() with base 10: ''

pass
def shel():
    pass

shel()
res = shel()
print(res)
None


def convert(cm):
    """DFGHJK.
fedcffcfccf
dfvvvdv."""
    cmm = cm%100
    mm = cm//100
    return f"{mm}.{cmm}"
help(convert)
SyntaxError: invalid syntax


def convert(cm):
    """DFGHJK.
fedcffcfccf
dfvvvdv."""
    cmm = cm%100
    mm = cm//100
    return f"{mm}.{cmm}"



help(convert)
Help on function convert in module __main__:

convert(cm)
    DFGHJK.
    fedcffcfccf
    dfvvvdv.




def convert(cm):
    """DFGHJK.
    fedcffcfccf
    dfvvvdv."""
    
    if cm < 100:
        return False
    
    cmm = cm%100
    mm = cm//100
    return f"{mm}.{cmm}"


convert(99)
False
convert(-23)
False
convert(100)
'1.0'
convert(2000)
'20.0'
def convert(cm):
    """DFGHJK.
    fedcffcfccf
    dfvvvdv."""
    return 1000
    
    if cm < 100:
        return False
    
    cmm = cm%100
    mm = cm//100
    return f"{mm}.{cmm}"



convert(-9)
1000

li = [1,2,3]
li2 = li
li2[0] = 99
li
[99, 2, 3]


def fun(lis):
    lis[0] = 9999

    
li
[99, 2, 3]
fun(li)
li
[9999, 2, 3]
li = [1,2,3]
fun(li[:])
li
[1, 2, 3]
fun(li.copy())
li
[1, 2, 3]



li
[1, 2, 3]
li2 = copy.li
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    li2 = copy.li
NameError: name 'copy' is not defined. Did you forget to import 'copy'?
li2 = li.copy
li2[0]=99
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    li2[0]=99
TypeError: 'builtin_function_or_method' object does not support item assignment
li2
<built-in method copy of list object at 0x000001B76A434FC0>
li
[1, 2, 3]
li2[0]
Traceback (most recent call last):
  File "<pyshell#294>", line 1, in <module>
    li2[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
li
[1, 2, 3]


isinstance
<built-in function isinstance>
isinstance(10,int)
True
isinstance(10,list)
False


total = 0
def ad_t(n):
    total = total +n

    
ad_t(5)
Traceback (most recent call last):
  File "<pyshell#307>", line 1, in <module>
    ad_t(5)
  File "<pyshell#306>", line 2, in ad_t
    total = total +n
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
print(total)
0
total
0
def ad_t(n):
    res = total +n
    print(res)

    
ad_t(9)
9
def ad(n):
    global total
    total = total +n

    
ad(8)
total
8
ad(9)
total
17


!1
SyntaxError: invalid syntax
1*2*3
6

def fact(n):
    if n < 0:
        return
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


fact(9)
362880
fact(0)
1
def main():
    oper = input("exit +")
    while oper != "exit":
        res = fact(int(input("factorial:")))
        print("factorial is:", res)
        oper = input("exit +")

        
main()
exit ++
factorial:10
factorial is: 3628800
exit ++8
factorial:3
factorial is: 6
exit +exit









def rec(n):
    if
    
SyntaxError: invalid syntax
def  rec(n):
    if n >= 20:
        return 1
    return n + rec(n+4)

rec(1)
46

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

fact(5)
120


import sys
sys.getrecursionlimit()
1000






f1 ,f2 = 1, 1
f1, f2 = f2, f1+f2
f2
2
f1, f2 = f2, f1+f2
f2
3
f1, f2 = f2, f1+f2
f3
Traceback (most recent call last):
  File "<pyshell#380>", line 1, in <module>
    f3
NameError: name 'f3' is not defined. Did you mean: 'f1'?
f2
5
f1, f2 = f2, f1+f2
f2
8
def feb(n):
    f1,f2 = 1, 1
    if n < 0:
        return
    if n == 1 or n ==2:
        return 1
    for i in range(2, n):
        f1, f2 = f2, f1+f2
        return f2
KeyboardInterrupt


n = 3
for i in range(2,n):
    pass
f1,f2=1,1
SyntaxError: invalid syntax
for i in range(2,n):
    f1,f2 = f2, f1+f2

    
def feb(n):
    f1,f2 = 1, 1
    if n < 0:
        return
    if n == 1 or n ==2:
        return 1
    for i in range(2, n):
        f1, f2 = f2, f1+f2
        return f2

    
feb(5)
2
f1,f2=1,1
def feb(n):
    f1,f2 = 1, 1
    if n < 0:
        return
    if n == 1 or n ==2:
        return 1
    for i in range(2, n):
        f1, f2 = f2, f1+f2
        return f2

    
feb(5)
2
f1,f2=1,1
f1
1
for i in range(2,n):
    f1,f2 = f2, f1+f2

    
f1
1
f2
2
def feb(n):
    f1,f2 = 1, 1
    if n < 0:
        return
    if n == 1 or n ==2:
        return 1
    for i in range(2, n):
        f1, f2 = f2, f1+f2
        return f2

    

feb(5)
2




f1,f2 = 1, 1
def feb(n):
    
    if n < 0:
        return
    if n == 1 or n ==2:
        return 1
    for i in range(2, n):
        f1, f2 = f2, f1+f2
        return f2

    
feb(5)
Traceback (most recent call last):
  File "<pyshell#423>", line 1, in <module>
    feb(5)
  File "<pyshell#422>", line 8, in feb
    f1, f2 = f2, f1+f2
UnboundLocalError: cannot access local variable 'f2' where it is not associated with a value
>>> def feb(n):
...     f1,f2 = 1, 1
...     if n < 0:
...         return
...     if n == 1 or n ==2:
...         return 1
...     for i in range(3, n):
...         f1, f2 = f2, f1+f2
...         return f2
... 
...     
>>> feb(5)
2
>>> def feb(n):
...     f1,f2 = 1, 1
...     if n < 0:
...         return
...     if n == 1 or n ==2:
...         return 1
...     for i in range(2, n):
...         f1, f2 = f2, f1+f2
...     return f2
... 
>>> feb(5)
5
>>> 
>>> 
>>> 

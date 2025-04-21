Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


for i in range(10):
    print(i)
else:
    print("цикл заввершился")

    
0
1
2
3
4
5
6
7
8
9
цикл заввершился
for i in range(10):
    if i == 7:
        break
    print(i)
else:
    print("цикл заввершился")

    
0
1
2
3
4
5
6


count = 10
while count > 0:
    print(count)
    count-=1
else:
    print("цикл заввершился")

    
10
9
8
7
6
5
4
3
2
1
цикл заввершился
while count > 0:
    if count == 7:
        break
    print(count)
    count-=1
else:
    print("цикл заввершился")

    
цикл заввершился
count = 10
while count > 0:
    if count == 7:
        break
    print(count)
    count-=1
else:
    print("цикл заввершился")

    
10
9
8





a =10
a>10
False
a>4
True
c = 5
a == 10
True
a == 5
False
a == 10 and c == 5
True
a == 10 and c > 5
False
a < 10 and c > 5
False


True and True
True
True and False
False
b = 100
w = 200
if w > 0 and w > b:
    print("pay")
else:
    print("failed")

    
pay
w = -10
if w > 0 and w > b:
    print("pay")
else:
    print("failed")

    
failed
time = "day"
if w > 0 and w > b and time == "day":
    print("pay")
else:
    print("failed")

    
failed
w=200
time = "day"
if w > 0 and w > b and time == "day":
    print("pay")
else:
    print("failed")
    
SyntaxError: multiple statements found while compiling a single statement

if w > 0 and w > b and time == "day":
    print("pay")
else:
    print("failed")

    
pay

c1 = 10
c2 = 15
while c1  > 0 or c2 >0:
    if c1 > 0:
        print('c1:', c1)
    else:
        print("pervii otval")
        
    if c2 > 0:
        print('c2:', c2)
    else:
        print("vtoroi otval")

        
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10
c2: 15
c1: 10Traceback (most recent call last):
  File "<pyshell#67>", line 3, in <module>
    print('c1:', c1)
KeyboardInterrupt
c1 = 3
c2 = 6
while c1  > 0 or c2 >0:
    if c1 > 0:
        print('c1:', c1)
    else:
        print("pervii otval")
        
    if c2 > 0:
        print('c2:', c2)
    else:
        print("vtoroi otval")
    c1 -=1
    c2-=1

    
c1: 3
c2: 6
c1: 2
c2: 5
c1: 1
c2: 4
pervii otval
c2: 3
pervii otval
c2: 2
pervii otval
c2: 1
c1=3
c2 = 6
while c1  > 0 and c2 >0:
    if c1 > 0:
        print('c1:', c1)
    else:
        print("pervii otval")
        
    if c2 > 0:
        print('c2:', c2)
    else:
        print("vtoroi otval")
    c1 -=1
    c2-=1

    
c1: 3
c2: 6
c1: 2
c2: 5
c1: 1
c2: 4



5 > 2
True
3 < 5
True
True or False
True
True or True
True
False or False
False


not
SyntaxError: invalid syntax


True
True
not True
False
2 > 3
False
not 2> 3
True
if not 3> 2:
    print(3)
else:
    print(2)

    
2

not not not not not not True
True
not 3 > 2 or not not not 4> 5
True


#Home work 2.5
#Home work 2.6
# Calculator

num1 = int(input('Введите число:'))
Введите число:12
num2 = int(input('Введите число:'))
Введите число:6
oper = input("+ - * / exit")
+ - * / exit+
oper
'+'
if oper == "+"
SyntaxError: expected ':'
if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print (num1 - num2)
elif oper == "*":
    print (num1 * num2)
elif oper =="/":
    print(num1/num2)
else:
    print("ne ponimau")

    
18

while oper != "exit:"
SyntaxError: expected ':'
while oper != "exit":
    num1 = int(input('Введите число:'))
    num2 = int(input('Введите число:'))

    
Введите число:if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print (num1 - num2)
elif oper == "*":
    print (num1 * num2)
elif oper =="/":
    print(num1/num2)
else:
    print("ne ponimau")
Traceback (most recent call last):
  File "<pyshell#129>", line 2, in <module>
    num1 = int(input('Введите число:'))
ValueError: invalid literal for int() with base 10: 'if oper == "+":'

while oper != "exit":
    num1 = int(input('Введите число:'))
    num2 = int(input('Введите число:'))
    if oper == "+":
        print(num1 + num2)
    elif oper == "-":
        print (num1 - num2)
    elif oper == "*":
        print (num1 * num2)
    elif oper =="/":
        print(num1/num2)
    else:
        print("ne ponimau")
    oper = input("+ - * / exit")

    
Введите число:Traceback (most recent call last):
  File "<pyshell#133>", line 2, in <module>
    num1 = int(input('Введите число:'))
ValueError: invalid literal for int() with base 10: '    print(num1 + num2)'
while oper != "exit":
    num1 = int(input('Введите число:'))
    num2 = int(input('Введите число:'))
    if oper == "+":
        print(num1 + num2)
    elif oper == "-":
        print (num1 - num2)
    elif oper == "*":
        print (num1 * num2)
    elif oper =="/":
        print(num1/num2)
    else:
        print("ne ponimau")
    oper = input("+ - * / exit")

    
Введите число:Traceback (most recent call last):
  File "<pyshell#135>", line 2, in <module>
    num1 = int(input('Введите число:'))
ValueError: invalid literal for int() with base 10: 'elif oper == "-":'
oper = input("+ - * / exit")
+ - * / exit
oper = input("+ - * / exit")
+ - * / exit


num1
12
while oper != "exit":
    num1 = int(input('Введите число:'))
    num2 = int(input('Введите число:'))
    
    if oper == "+":
        print(num1 + num2)
    elif oper == "-":
        print(num1 - num2)
    elif oper == "*":
        print(num1 * num2)
    elif oper == "/":
        print(num1/num2)
    else:
        print("ne ponimau")
        
    oper = input("+ - * / exit")

    
Введите число:Traceback (most recent call last):
  File "<pyshell#142>", line 2, in <module>
    num1 = int(input('Введите число:'))
ValueError: invalid literal for int() with base 10: '    print (num1 * num2)'
oper = input("+ - * / exit")
+ - * / exit

oper
'elif oper =="/":'
del oper
oper
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    oper
NameError: name 'oper' is not defined. Did you mean: 'open'?
oper = input("+-*/ exit:")
+-*/ exit:
oper
'    print(num1/num2)'



oper
'    print(num1/num2)'
del oper
oper
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    oper
NameError: name 'oper' is not defined. Did you mean: 'open'?



while oper != "exit":
    num1 = int(input('Введите число:'))
    num2 = int(input('Введите число:'))
    
    if oper == "+":
        print(num1 + num2)
    elif oper == "-":
        print(num1 - num2)
    elif oper == "*":
        print(num1 * num2)
    elif oper == "/":
        print(num1/num2)
    else:
        print("ne ponimau")
        
    oper = input("+ - * / exit")

    
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    while oper != "exit":
NameError: name 'oper' is not defined. Did you mean: 'open'?
while operation != "exit":
    num1 = int(input('Введите число:'))
    num2 = int(input('Введите число:'))
    
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1/num2)
    else:
        print("ne ponimau")
        
    operation = input("+ - * / exit")

    
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    while operation != "exit":
NameError: name 'operation' is not defined. Did you mean: 'StopIteration'?
operation
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    operation
NameError: name 'operation' is not defined. Did you mean: 'StopIteration'?
operation = input("+ - * / exit")
+ - * / exit
+
SyntaxError: invalid syntax

operation = input("+ - * / exit")
+ - * / exit



a = input('a=')
a=1
o = input("+-= exit")
+-= exit+
o
'+'
while o != "exit":
    num1 = int(input('Введите число:'))
    num2 = int(input('Введите число:'))
    
    if o == "+":
        print(num1 + num2)
    elif o == "-":
        print(num1 - num2)
    elif o == "*":
        print(num1 * num2)
    elif o == "/":
        print(num1/num2)
    else:
        print("ne ponimau")
        
    o = input("+ - * / exit")

    
Введите число:1
Введите число:5
6
+ - * / exit+
Введите число:3
Введите число:2
5
+ - * / exitexit






a =1
a = [1,2,3,4]
a
[1, 2, 3, 4]
a[0]
1
a[3]
4
a[7]
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    a[7]
IndexError: list index out of range
type(a)
<class 'list'>
a[]
SyntaxError: invalid syntax
a = []
a
[]
li = list()
li
[]
li = [2,4,5,6]
li[2]
5
li[-1]
6
li[-3]
4
li[0]
2



s = 'abc'
s
'abc'
print(s)
abc
s.upper()
'ABC'
s
'abc'
a =10
a.upper()
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    a.upper()
AttributeError: 'int' object has no attribute 'upper'
s
'abc'
li1 =[1,2,3]
li2 = ['asd',2,3]
li1+li2
[1, 2, 3, 'asd', 2, 3]
res li1 +li2
SyntaxError: invalid syntax
res = li1 +li2
res
[1, 2, 3, 'asd', 2, 3]
li1*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
li1
[1, 2, 3]
li2 += li1*2
li2
['asd', 2, 3, 1, 2, 3, 1, 2, 3]
len(li2)
9
len(res)
6
li1 [-1]
3
li
[2, 4, 5, 6]
li[1]=2222
li
[2, 2222, 5, 6]


li.copy(li1)
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    li.copy(li1)
TypeError: list.copy() takes no arguments (1 given)
li.copy ()
[2, 2222, 5, 6]
li.insert (3,9999999)
li
[2, 2222, 5, 9999999, 6]
li.pop()
6
li
[2, 2222, 5, 9999999]
li.reverse()
li
[9999999, 5, 2222, 2]
li. reverse()
li
[2, 2222, 5, 9999999]
li.pop()
9999999
res = li.pop
res
<built-in method pop of list object at 0x00000191DEC68BC0>
li
[2, 2222, 5]
res
<built-in method pop of list object at 0x00000191DEC68BC0>
li.pop(0)
2
li
[2222, 5]
val = 22
if val in li:
    li.remove(22)

    

li
[2222, 5]
li = [1,1,1,1,1]
li.index(0)
Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    li.index(0)
ValueError: 0 is not in list
li.index(1)
0
li.clear()
li
[]
del li
li
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    li
NameError: name 'li' is not defined. Did you mean: 'i'?

 


#######################
#home work 3.1

li = [1,2,3,4,5,6,7]
print("Длина li:",len(li))
Длина li: 7
 a = int(input("Введите число:"))
 
SyntaxError: unexpected indent
a = int(input("Введите число:"))
Введите число:33
li.insert(3, a)
li
[1, 2, 3, 33, 4, 5, 6, 7]
li.pop
<built-in method pop of list object at 0x00000191DECDBE00>
li.pop()
7
len(li)
7
li
[1, 2, 3, 33, 4, 5, 6]
print(li)
[1, 2, 3, 33, 4, 5, 6]


li
[1, 2, 3, 33, 4, 5, 6]
#by value
for i in li:
    print(i, end=" |")

    
1 |2 |3 |33 |4 |5 |6 |
for i in li:
    print(5 + i**2, end=" |")

    
6 |9 |14 |1094 |21 |30 |41 |
li
[1, 2, 3, 33, 4, 5, 6]





s = 'addfghyju'
for i in li:
    print(i, end=" |")

    
1 |2 |3 |33 |4 |5 |6 |
for i in s:
    print(i, end=" |")

    
a |d |d |f |g |h |y |j |u |

# by index
li = [1,2,3,4]
len(li)
4
for i in raneg(len(li))
SyntaxError: expected ':'
for i in raneg(len(li)):
    print(li[i])

    
Traceback (most recent call last):
  File "<pyshell#301>", line 1, in <module>
    for i in raneg(len(li)):
NameError: name 'raneg' is not defined. Did you mean: 'range'?
for i in range(len(li)):
    print(li[i])

    
1
2
3
4
t = 0
for i in raneg(len(li)):
    t += li[i]

    
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    for i in raneg(len(li)):
NameError: name 'raneg' is not defined. Did you mean: 'range'?
for i in range(len(li)):
    t += li[i]

    
t
10
for i in li:
    t += 1

    
t
14








#sorting
a = 8
b = 3
a = b
a = 8
tmp = a
a = b
b = tmp
a
3
b
8



a = 8
b = 3
a, b = b, a
a
3
b
8

li = [4,5,2,3,1,0]
li [1], li[2] = li[2],li[1]
li
[4, 2, 5, 3, 1, 0]
for i in range(len(li)):
    if li[i] > li[i+1]
    
SyntaxError: expected ':'
for i in range(len(li)):
    if li[i] > li[i+1]:
        li[i], li[i+1] = li[i+1], li[i]
    else:
        i+=1

        
Traceback (most recent call last):
  File "<pyshell#348>", line 2, in <module>
    if li[i] > li[i+1]:
IndexError: list index out of range
i
5
li
[2, 4, 3, 1, 0, 5]
p = range(len(li))
p
range(0, 6)
for i in li:
    if li[i] > li[i+1]:
        li[i], li[i+1] = li[i+1], li[i]
    else:
        i+=1

        
Traceback (most recent call last):
  File "<pyshell#354>", line 2, in <module>
    if li[i] > li[i+1]:
IndexError: list index out of range
i
5
len(li)
6
for i in len(li)+1:
    if li[i] > li[i+1]:
        li[i], li[i+1] = li[i+1], li[i]
    else:
        i+=1

        
Traceback (most recent call last):
  File "<pyshell#358>", line 1, in <module>
    for i in len(li)+1:
TypeError: 'int' object is not iterable
p = range(len(li))
p
range(0, 6)
for i in range(len(li)):
    if li[i] > li[i+1]:
        li[i], li[i+1] = li[i+1], li[i]
    else:
        i+=1

        
Traceback (most recent call last):
  File "<pyshell#362>", line 2, in <module>
    if li[i] > li[i+1]:
IndexError: list index out of range

for j in range(len(li))
    for i in range(len(li) - 1):
    
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
return li
SyntaxError: expected ':'
for j in range(len(li)):
    for i in range(len(li) - 1):
    
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
return li
SyntaxError: invalid syntax
for j in range(len(li))
    for i in range(len(li) - 1):
    
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]

SyntaxError: expected ':'
for j in range(len(li)):
    for i in range(len(li) - 1):
    
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]


li
[0, 1, 2, 3, 4, 5]



li = [2,3,1,5,3,1,0]
a = len(li)+1
a
8
while i <= len(li)+1
SyntaxError: expected ':'
while i <= len(li)+1:
    for j in range(len(li)):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

            
Traceback (most recent call last):
  File "<pyshell#378>", line 3, in <module>
    if li[j] > li[j+1]:
IndexError: list index out of range
while i <= len(li)+1:
    for j in range(len(li)-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

            
Traceback (most recent call last):
  File "<pyshell#380>", line 3, in <module>
    if li[j] > li[j+1]:
KeyboardInterrupt





while i <= len(li)+1:
    for j in range(len(li)):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
    i+=1

    
Traceback (most recent call last):
  File "<pyshell#383>", line 3, in <module>
    if li[j] > li[j+1]:
IndexError: list index out of range
while i <= len(li)+1:
    for j in range(len(li)-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
    i +=1

    
li
[0, 1, 1, 2, 3, 3, 5]



li2 = li.copy()
li
[0, 1, 1, 2, 3, 3, 5]
li2
[0, 1, 1, 2, 3, 3, 5]
li[0] = 11111
li
[11111, 1, 1, 2, 3, 3, 5]
li2
[0, 1, 1, 2, 3, 3, 5]
li = [1,2,3,4]
l2 = [1,2,li]
li3 = l2.copy()
li3
[1, 2, [1, 2, 3, 4]]
li[0] = 9999
li
[9999, 2, 3, 4]
li3
[1, 2, [9999, 2, 3, 4]]

from deepcopy import
SyntaxError: Expected one or more names after 'import'
from copy import deepcopy
li = [1,2,3,4]
l2 = [1,2,li]
li3 = deepcopy(li)
li[0]=999
li
[999, 2, 3, 4]
li3
[1, 2, 3, 4]

 


li
[999, 2, 3, 4]
li[:]
[999, 2, 3, 4]
li[1:]
[2, 3, 4]
li[:2]
[999, 2]
li[1:2]
[2]
li
[999, 2, 3, 4]
a =5
a in li
False
a no tin li
SyntaxError: invalid syntax
a not in li
True


li
[999, 2, 3, 4]
li[-3:-1]
[2, 3]
li[-1:-3]
[]
li
[999, 2, 3, 4]
del li[-3:-1]
li
[999, 4]


li = [1,2,2,2,2,3,4,5]
ko = {li}
Traceback (most recent call last):
  File "<pyshell#437>", line 1, in <module>
    ko = {li}
TypeError: unhashable type: 'list'
>>> 
>>> 

>>> s = set()
>>> s
set()
>>> s = {1,2,3,1,2,3}
>>> s
{1, 2, 3}
>>> len(s)
3
>>> 6 in s
False
>>> 1 in s
True
>>> for i in s:
...     print(i)
... 
...     
1
2
3
>>> s.add (22)
>>> s
{1, 2, 3, 22}
>>> s.update({3,4,5,6,7})
>>> s
{1, 2, 3, 4, 5, 6, 7, 22}
>>> s.remove(4)
>>> s
{1, 2, 3, 5, 6, 7, 22}
>>> s.discard(3)
>>> s
{1, 2, 5, 6, 7, 22}



>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> print('gh');
gh
>>> print('gh'
... )
gh
>>> 
>>> 
>>> input()
hello
'hello'
>>> 1 ==1
True
>>> 1!=2
True
>>> 1!=1
False
>>> a = 55
>>> a==55
True
>>> a!=66
True
>>> b =88
>>> a == b
False
>>> a!=b
True
>>> 6 ==6 
True
>>> 6!=7
True
>>> res = 6 == 6
>>> res
True
>>> type(res)
<class 'bool'>
>>> 2<3
True
>>> 2<=3
True
>>> 2<2
False
>>> 2<=2
True
>>> 
>>> 2 * 4**2 < 55
True
>>> 2 * 4**2 
32
>>> 
>>> 5
5
>>> 5.0
5.0
>>> 5 == 5.
True
>>> 5 == 5.00000000000000001
True
>>> #numpy
>>> 5 == 5.000001
False
>>> 5 == 5.0000001
False
>>> 5 == 5.00000001
False
>>> 5 == 5.000000001
False
>>> 5 == 5.0000000001
False
>>> 5 == 5.00000000001
False
>>> 5 == 5.000000000001
False
>>> 5 == 5.0000000000001
False
>>> 5 == 5.00000000000001
False
>>> 5 == 5.000000000000001
False
>>> 5 == 5.0000000000000001
True
>>> 
>>> 
>>> password = input('pass->')
pass->12345
>>> password == "12345"
True
>>> password == "rtyu"
False
>>> 
>>> password = input('pass->')
pass->123
>>> if password == "123":
...         print(''Welcome!
...         )
...         
  File "<python-input-51>", line 2
    print(''Welcome!
          ^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> if password == "123":
...         print('Welcome!')
...         123
... 
Welcome!
123
>>> 
>>> 
>>> 
>>> if password == "123":
...         print("welcome!")
...         
welcome!
>>> print(12)
12
>>> 
>>> 
>>> 
>>> password = input("pass->")
pass->1
>>> if password == "123":
...         print("welcome!")
...         
>>> 
>>> password = input("pass->")
pass->123
>>> if password == "123":
...         print("welcome!")
...         print("Welcome!")
...         print("Welcome!")
... else:
...         print("failed")
...         
welcome!
Welcome!
Welcome!
>>> 
>>> password = input("pass->")
pass->1
>>> if password == "123":
...         print("welcome!")
...         print("Welcome!")
...         print("Welcome!")
... else:
...         print("failed")
...         
failed
>>> 
>>> password = input("pass->")
pass->123("Welcome!")... else:...         print("failed")
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ("Welcome!")
... ... else:
... ...         print("fai
... 
  File "<python-input-76>", line 3
    ...         print("fai
                      ^
SyntaxError: unterminated string literal (detected at line 3)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> password = input("pass->")
pass->123
>>> if password == "123":
...         print("Welcome admin!")
... elif password == "321":
...         print("Welcome manager")
... else:
...         print("welcome client")
...         
Welcome admin!
>>> 
>>> password = input("pass->")
pass->43
>>> if password == "123":
...          print("Welcome admin!")
...  elif password == "43":
...          print("Welcome manager")
...  else:
...          print("welcome client")
...          
  File "<python-input-88>", line 3
    elif password == "43":
                          ^
IndentationError: unindent does not match any outer indentation level
>>> 123 if 1 == 1 else 55
123
>>> print(1123 if 1 == 1 else 55)
1123
>>> 
>>> pass = input("pas->")
  File "<python-input-92>", line 1
    pass = input("pas->")
         ^
SyntaxError: invalid syntax
>>> passw = input("pas->")
pas->123
>>> print(123 if passw == "123" else 55)
123
>>> 
>>> 
>>> passw = input("pas->")
pas->123
>>> passw
'123'
>>> match passw:
...          case "123":
...                   print("wel ad")
...          case "321":
...                   print("wel man")
...          case _:
...                   print("try again")
...                   
wel ad
>>> passw = input("pas->")
pas->321
>>> match passw:
... ...          case "123":
... ...                   print("wel ad")
... ...          case "321":
... ...                   print("wel man")
... ...          case _:
... ...                   print("try again")
... 
  File "<python-input-101>", line 2
    ...          case "123":
    ^^^
IndentationError: expected an indented block after 'match' statement on line 1
>>> match passw:
...           case "123":
...                    print("wel ad")
...           case "321":
...                    print("wel man")
...           case _:
...                    print("try again")
...                    
wel man
>>> passw = input("pas->")
pas->1
>>> match passw:
...           case "123":
...                    print("wel ad")
...           case "321":
...                    print("wel man")
...           case _:
...                    print("try again")
...                    
try again
>>> 
>>> passw = input("pas->")
pas->123
>>> while passw != 1:
...           print("bad, try..")
...           passw = input("pas->")
...           
bad, try..
pas->2
bad, try..
pas->3
bad, try..
pas->123
bad, try..
pas->1
bad, try..
pas->Traceback (most recent call last):
  File "<python-input-107>", line 3, in <module>
    passw = input("pas->")
  File "/usr/local/lib/python3.13/_pyrepl/readline.py", line 371, in input
    result = reader.readline(startup_hook=self.startup_hook)
  File "/usr/local/lib/python3.13/_pyrepl/reader.py", line 801, in readline
    self.handle1()
    ~~~~~~~~~~~~^^
  File "/usr/local/lib/python3.13/_pyrepl/reader.py", line 756, in handle1
    self.console.wait(100)
    ~~~~~~~~~~~~~~~~~^^^^^
  File "/usr/local/lib/python3.13/_pyrepl/unix_console.py", line 426, in wait
    or bool(self.pollob.poll(timeout))
            ~~~~~~~~~~~~~~~~^^^^^^^^^
KeyboardInterrupt
>>> passw = int(input("pas->"))
pas->123
>>> while passw != 1:
...           print("bad?try")
...           passw = int(input("pas->"))
...           
bad?try
pas->4
bad?try
pas->3
bad?try
pas->123
bad?try
pas->
Traceback (most recent call last):
  File "<python-input-109>", line 3, in <module>
    passw = int(input("pas->"))
ValueError: invalid literal for int() with base 10: ''
>>> 1
1
>>> while passw != 1:
...           print("bad?try")
...           passw = int(input("pas->"))
...           
bad?try
pas->1
>>> 
>>> x = 10
>>> while x!=0:
...           print(x, end=" ")
...           x-=1
...           
10 9 8 7 6 5 4 3 2 1 >>> 
>>> 
>>> 
>>> a = 10
>>> a = a-1
>>> a
9
>>> a-=1
>>> a
8
>>> a+=1
>>> a
9
>>> a*=2
>>> a
18
>>> a=+1
>>> a
1
>>> a =18
>>> a
18
>>> count = 1
>>> while count < 10:
...           print(count**2)
...           count+=1
...           
1
4
9
16
25
36
49
64
81
>>> for i in range(10)
  File "<python-input-133>", line 1
    for i in range(10)
                      ^
SyntaxError: expected ':'
>>> for i in range(10)
  File "<python-input-134>", line 1
    for i in range(10)
                      ^
SyntaxError: expected ':'
>>> 
>>> 
>>> 
>>> for i in range(10):
...           print(i**2)
...           
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
>>> for i in range(5,10):
...           print(i)
...           
5
6
7
8
9
>>> for i in range(1, 15):
...           print(i)
...           
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
11
12
13
14
>>> for i in range(1, 15, 2):
...           print(i)
...           
1
3
5
7
9
11
13
>>> for i in range(1, 15):
...         if i % 2 == 0:
...         print(i)
...         
  File "<python-input-142>", line 3
    print(i)
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 2
>>> for i in range(1, 15):
...     if i % 2 == 0:
...         print(i)
...         
2
4
6
8
10
12
14
>>> for i in range(1, 15):
...     if i % 2 ==0:
...         print(t)
...         if i == 12:
...             break
...             
Traceback (most recent call last):
  File "<python-input-144>", line 3, in <module>
    print(t)
          ^
NameError: name 't' is not defined
>>> for i in range(1, 15):
...     if i % 2 ==0:
...         print(i)
...         if i == 12:
...             break
...             
2
4
6
8
10
12
>>> for i in range(1, 15):
...     break
...     if i % 2 ==0:
...         print(i)
...         if i == 12:
...             break
...             
>>> 
>>> 
>>> 
>>> break
  File "<python-input-150>", line 1
    break
    ^^^^^
SyntaxError: 'break' outside loop
>>> 
>>> for i in range(1, 15):
...     if i % 2 ==0:
...         conrinue
...     print(i)
...     
1
Traceback (most recent call last):
  File "<python-input-152>", line 3, in <module>
    conrinue
NameError: name 'conrinue' is not defined
>>> for i in range(1, 15):
...     if i % 2 ==0:
...         continue
...     print(i)
...     
1
3
5
7
9
11
13
>>> for i in range(1, 15):
...     if i % 2 ==0:
...         pass
...     print(i)
...     
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
11
12
13
>>> 
14
>>> name = sasha
Traceback (most recent call last):
  File "<python-input-155>", line 1, in <module>
    name = sasha
           ^^^^^
NameError: name 'sasha' is not defined. Did you mean: 'hash'?
>>> name ="sasha"
>>> "a" in name
True
>>> "f" in name
False
>>> "f" not  in name
True
>>> if "a" in name:
...     print(1,2,3)
...     
1 2 3
>>> 
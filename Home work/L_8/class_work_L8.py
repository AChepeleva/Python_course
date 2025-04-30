Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

try:
    n = int(input("-->"))
    print(1/n)
except:
    print("Problem..")

    
-->er
Problem..
try:
    n = int(input("-->"))
    print(1/n)
except:
    print("Problem..")

    
-->2
0.5

for i in range(4):
    try:
        n = int(input("-->"))
        print(1/n)
    except:
        print("Problem..")

        
-->3
0.3333333333333333
-->er
Problem..
-->0
Problem..
-->-1
-1.0


for i in range(4):
    n = int(input("-->"))
    print(1/n)

-->
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    n = int(input("-->"))
ValueError: invalid literal for int() with base 10: ''


try:
    n = int(input("-->"))
    print(1/n)
except valueError:
    pritn("ValuError - sorry..")
except:
    print("Problem..")

    
-->123
0.008130081300813009
try:
    n = int(input("-->"))
    print(1/n)
except valueError:
    pritn("ValuError - sorry..")
except:
    print("Problem..")

    
-->0
Traceback (most recent call last):
  File "<pyshell#20>", line 3, in <module>
    print(1/n)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#20>", line 4, in <module>
    except valueError:
NameError: name 'valueError' is not defined. Did you mean: 'ValueError'?
try:
    n = int(input("-->"))
    print(1/n)
except valueError:
    pritn("ValuError - sorry..")
except:
    print("Problem..")

    
-->asdds
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    n = int(input("-->"))
ValueError: invalid literal for int() with base 10: 'asdds'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#22>", line 4, in <module>
    except valueError:
NameError: name 'valueError' is not defined. Did you mean: 'ValueError'?
try:
    n = int(input("-->"))
    print(1/n)
except ValueError:
    pritn("ValuError - sorry..")
except:
    print("Problem..")

    
-->sdcfv
Traceback (most recent call last):
  File "<pyshell#24>", line 2, in <module>
    n = int(input("-->"))
ValueError: invalid literal for int() with base 10: 'sdcfv'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#24>", line 5, in <module>
    pritn("ValuError - sorry..")
NameError: name 'pritn' is not defined. Did you mean: 'print'?
try:
    n = int(input("-->"))
    print(1/n)
except ValueError:
    pritn("ValuError - sorry..")
except:
    print("Problem..")

    
-->0
Problem..
try:
    n = int(input("-->"))
    print(1/n)
except ValueError:
    pritn("ValuError - sorry..")
except ZeroDivisionError:
    print("Delit na 0 nelsia..")
except:
    print("Problem..")

    
-->w
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    n = int(input("-->"))
ValueError: invalid literal for int() with base 10: 'w'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#29>", line 5, in <module>
    pritn("ValuError - sorry..")
NameError: name 'pritn' is not defined. Did you mean: 'print'?
try:
    n = int(input("-->"))
    print(1/n)
except ValueError:
    pritn("ValuError - sorry..")
except ZeroDivisionError:
    print("Delit na 0 nelsia..")
except:
    print("Problem..")

    
-->0
Delit na 0 nelsia..
try:
    n = int(input("-->"))
    print(1/n)
except ValueError:
    pritn("ValuError - sorry..")
except ZeroDivisionError:
    print("Delit na 0 nelsia..")
except:
    print("Problem..")

    
-->------
Traceback (most recent call last):
  File "<pyshell#33>", line 2, in <module>
    n = int(input("-->"))
ValueError: invalid literal for int() with base 10: '------'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#33>", line 5, in <module>
    pritn("ValuError - sorry..")
NameError: name 'pritn' is not defined. Did you mean: 'print'?
try:
    n = int(input("-->"))
    print(1/n)
except ValueError:
    pritn("ValueError - sorry..")
except ZeroDivisionError:
    print("Delit na 0 nelsia..")
except:
    print("Problem..")

    
-->sxcdsa
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    n = int(input("-->"))
ValueError: invalid literal for int() with base 10: 'sxcdsa'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#35>", line 5, in <module>
    pritn("ValueError - sorry..")
NameError: name 'pritn' is not defined. Did you mean: 'print'?
KeyboardInterrupt
try:
    n = int(input("-->"))
    print(1/n)
except ValueError:
    print("ValuError - sorry..")
except ZeroDivisionError:
    print("Delit na 0 nelsia..")
except:
    print("Problem..")

    
-->
ValuError - sorry..
try:
    n = int(input("-->"))
    print(1/n)
except ValueError:
    print("ValuError - sorry..")
except ZeroDivisionError:
    print("Delit na 0 nelsia..")
except:
    print("Problem..")

-->
ValuError - sorry..
try:
    n = int(input("-->"))
    print(1/n)
except ValueError:
    print("ValuError - sorry..")
except ZeroDivisionError:
    print("Delit na 0 nelsia..")
except:
    print("Problem..")

-->sdfghj
ValuError - sorry..



try:
    n = int(input("-->"))
    print(1/n)
except Exception as e:
    print(e)
    print(e.args)
    print(e.__traceback__)

    
-->asdf
invalid literal for int() with base 10: 'asdf'
("invalid literal for int() with base 10: 'asdf'",)
<traceback object at 0x00000244B8B47280>
try:
    n = int(input("-->"))
    print(1/n)
except Exception as e:
    print(type(e))
    print(e.args)
    print(e.__traceback__)

    
-->sadfg
<class 'ValueError'>
("invalid literal for int() with base 10: 'sadfg'",)
<traceback object at 0x00000244B8B47C00>




try:
    n = int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("ValuError - sorry..")
    print(type(ve))
    print(ve.args)
except ZeroDivisionError as z:
    print("Delit na 0 nelsia..")
    print(type(z))
    print(z.args[0])
except:
    print("Problem..")

    
-->sdf
ValuError - sorry..
<class 'ValueError'>
("invalid literal for int() with base 10: 'sdf'",)




import traceback
try:
    n = int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("ValuError - sorry..")
    print(type(ve))
    print(ve.args[0])
    traceback.print_tb(ve.__traceback__)
except ZeroDivisionError as z:
    print("Delit na 0 nelsia..")
    print(type(z))
    print(z.args[0])
    traceback.print_tb(z.__traceback__)
except:
    print("Problem..")

    
-->0
Delit na 0 nelsia..
<class 'ZeroDivisionError'>
division by zero
  File "<pyshell#60>", line 3, in <module>
try:
    n = int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("ValuError - sorry..")
    print(type(ve))
    print(ve.args[0])
    traceback.print_tb(ve.__traceback__)
except ZeroDivisionError as z:
    print("Delit na 0 nelsia..")
    print(type(z))
    print(z.args[0])
    traceback.print_exc(z)
except:
    print("Problem..")

    
-->0
Delit na 0 nelsia..
<class 'ZeroDivisionError'>
division by zero
Traceback (most recent call last):
  File "<pyshell#62>", line 3, in <module>
    print(1/n)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#62>", line 13, in <module>
    traceback.print_exc(z)
  File "C:\Users\Sasha_Ch\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 208, in print_exc
    print_exception(sys.exception(), limit=limit, file=file, chain=chain)
  File "C:\Users\Sasha_Ch\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 129, in print_exception
    te = TracebackException(type(value), value, tb, limit=limit, compact=True)
  File "C:\Users\Sasha_Ch\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 1052, in __init__
    self.stack = StackSummary._extract_from_extended_frame_gen(
  File "C:\Users\Sasha_Ch\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 469, in _extract_from_extended_frame_gen
    elif limit >= 0:
TypeError: '>=' not supported between instances of 'ZeroDivisionError' and 'int'
try:
    n = int(input("-->"))
    print(1/n)
except ValueError as ve:
    print("ValuError - sorry..")
    print(type(ve))
    print(ve.args[0])
    traceback.print_tb(ve.__traceback__)
except ZeroDivisionError as z:
    print("Delit na 0 nelsia..")
    print(type(z))
    print(z.args[0])
    traceback.print_tb(z.__traceback__)
except:
    print("Problem..")

    
-->sxdc
ValuError - sorry..
<class 'ValueError'>
invalid literal for int() with base 10: 'sxdc'
  File "<pyshell#64>", line 2, in <module>






if n == 1:
    print(1)
elif n ==2:
    sdfghj
elif n == 3:
    prin(3)
else:
    print(123)

    
123
n =1
if n == 1:
    print(1)
elif n ==2:
    sdfghj
elif n == 3:
    prin(3)
else:
    print(123)

    
1
n=1234
if n == 1:
    print(1)
elif n ==2:
    sdfghj
elif n == 3:
    prin(3)
else:
    print(123)

    
123
n=2
if n == 1:
    print(1)
elif n ==2:
    sdfghj
elif n == 3:
    prin(3)
else:
    print(123)

    
Traceback (most recent call last):
  File "<pyshell#88>", line 4, in <module>
    sdfghj
NameError: name 'sdfghj' is not defined
n=3
if n == 1:
    print(1)
elif n ==2:
    sdfghj
elif n == 3:
    prin(3)
else:
    print(123)

    
Traceback (most recent call last):
  File "<pyshell#91>", line 6, in <module>
    prin(3)
NameError: name 'prin' is not defined. Did you mean: 'print'?



try:
    1/0
except ZeroDivisionError:
    print("ZeroDivisionError")

    
ZeroDivisionError
try:
    1/0
except ArithmeticError:
    print("ArithmeticError")

    
ArithmeticError

try:
    1/0
except Exception:
    print("Exception")
... 
...     
Exception
>>> try:
...     1/0
... except Exception:
...     print("Exception")
... except ArithmeticError:
...     print("ArithmeticError")
... except ZeroDivisionError:
...     print("ZeroDivisionError")
... 
...     
Exception
>>> try:
...     1/0
... except ZeroDivisionError:
...     print("ZeroDivisionError")
... except ArithmeticError:
...     print("ArithmeticError")
... except Exception:
...     print("Exception")
... 
...     
ZeroDivisionError
>>> 
>>> 
>>> 
>>> try:
...     1/0
... except ZeroDivisionError:
...     print("ZeroDivisionError")
... except ArithmeticError:
...     print("ArithmeticError")
... except Exception:

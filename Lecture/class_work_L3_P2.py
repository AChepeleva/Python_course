Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list
[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
res_list = [for ** 2 for val in my_list]
SyntaxError: invalid syntax
res_list = [val ** 2 for val in my_list]
res_list
[1, 4, 16, 16, 1, 16, 4, 36, 4, 81]
res_list = [for ** 2 for val in my_list]
SyntaxError: invalid syntax
res_list = [val ** 2 for val in my_list]

res_list
[1, 4, 16, 16, 1, 16, 4, 36, 4, 81]

res_list = [int(input('number')) for i in range(int(input('n+')))]
n+5
number22
number33
number44
number55
number66


res_list = [for i in range(int(input('n ='))) if i % 2== 0]
SyntaxError: invalid syntax
res_list = [val i in range(int(input('n ='))) if i % 2== 0]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
res_list = [i for i in range(int(input('n ='))) if i % 2== 0]
n =5

res
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    res
NameError: name 'res' is not defined
>>> res_list
[0, 2, 4]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
>>> res_list = [i for i in my_list]
>>> res_list
[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
>>> res_list = {i for i in my_list}
>>> res_list
{1, 2, 4, 6, 9}
>>> res_list = list(set(my_list))
>>> res_list
[1, 2, 4, 6, 9]
>>> 
>>> 
>>> 
>>> li = [[1,2,3], [3,4,5],[5,6,7]]
>>> len()li
SyntaxError: invalid syntax
>>> len(li)
3
>>> li[1]
[3, 4, 5]
>>> li
[[1, 2, 3], [3, 4, 5], [5, 6, 7]]
>>> li[0][1]
2
>>> li[1][2]
5
>>> li[2][1]
6
>>> 

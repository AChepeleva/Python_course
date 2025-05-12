Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


import json as jj

import json as j

j
<module 'json' from 'C:\\Users\\Sasha_Ch\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\json\\__init__.py'>
# py-> json - dumps

li = [1,2,3,4,5.6,7.8]
li = [1,2,3,4,5.6,7.8,True, False, (12,34,55),None, "fdvd"]
li
[1, 2, 3, 4, 5.6, 7.8, True, False, (12, 34, 55), None, 'fdvd']
type(li)
<class 'list'>
res == j.dumps(li, indent=4)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    res == j.dumps(li, indent=4)
NameError: name 'res' is not defined
res = j.dumps(li, indent=4)
print(res)
[
    1,
    2,
    3,
    4,
    5.6,
    7.8,
    true,
    false,
    [
        12,
        34,
        55
    ],
    null,
    "fdvd"
]
type(res)
<class 'str'>

# json -> py - loads

res_l = j.loads(res)
res_l
[1, 2, 3, 4, 5.6, 7.8, True, False, [12, 34, 55], None, 'fdvd']
res_l[3]
4
res
'[\n    1,\n    2,\n    3,\n    4,\n    5.6,\n    7.8,\n    true,\n    false,\n    [\n        12,\n        34,\n        55\n    ],\n    null,\n    "fdvd"\n]'
print(res)
[
    1,
    2,
    3,
    4,
    5.6,
    7.8,
    true,
    false,
    [
        12,
        34,
        55
    ],
    null,
    "fdvd"
]
li = {1:2,3:4,5.6:7.8,"true": True, "false": False, "tuple":(12,34,55),"none":None, "texxt":"fdvd"}
res_j = j.dumps(li, indent = 4)
res_j
'{\n    "1": 2,\n    "3": 4,\n    "5.6": 7.8,\n    "true": true,\n    "false": false,\n    "tuple": [\n        12,\n        34,\n        55\n    ],\n    "none": null,\n    "texxt": "fdvd"\n}'
print(res_j)
{
    "1": 2,
    "3": 4,
    "5.6": 7.8,
    "true": true,
    "false": false,
    "tuple": [
        12,
        34,
        55
    ],
    "none": null,
    "texxt": "fdvd"
}
>>> 
>>> 
>>> 
>>> nex = j.loads(res_j)
>>> nex
{'1': 2, '3': 4, '5.6': 7.8, 'true': True, 'false': False, 'tuple': [12, 34, 55], 'none': None, 'texxt': 'fdvd'}
>>> nex["5.6"] = 222222222
>>> nex
{'1': 2, '3': 4, '5.6': 222222222, 'true': True, 'false': False, 'tuple': [12, 34, 55], 'none': None, 'texxt': 'fdvd'}
>>> next_s = j.dumps(nex)
>>> print(next_s)
{"1": 2, "3": 4, "5.6": 222222222, "true": true, "false": false, "tuple": [12, 34, 55], "none": null, "texxt": "fdvd"}
>>> next_s = j.dumps(nex, indent = 5)
>>> print(next_s)
{
     "1": 2,
     "3": 4,
     "5.6": 222222222,
     "true": true,
     "false": false,
     "tuple": [
          12,
          34,
          55
     ],
     "none": null,
     "texxt": "fdvd"
}

Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
li = [1,2,3,4,5]
li
[1, 2, 3, 4, 5]

new_list =li
new_list
[1, 2, 3, 4, 5]
new_list[1]
2
new_list[1]=999
new_list
[1, 999, 3, 4, 5]
li
[1, 999, 3, 4, 5]
id
<built-in function id>
help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.

    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

id(new_list)
     
2957115035136
id(li)
     
2957115035136
li = [1,2,3,4,5]
     

new_list = li.copy()
     
li
     
[1, 2, 3, 4, 5]
new_list
     
[1, 2, 3, 4, 5]
id(new_list)
     
2959218685824
id(li)
     
2957114968704
new_list[1]=999
     
new_list
     
[1, 999, 3, 4, 5]
li
     
[1, 2, 3, 4, 5]
new_list = li[:]
     
id(new_list)
     
2959232028672
id(li)
     
2957114968704
li
     
[1, 2, 3, 4, 5]
kk = [1, 2, 3, 4, [3,5,6,7,]]
     
new_list =kk[:]
     
id(new_list)
     
2957115126848
id(li)
     
2957114968704
loi[0]=1000
     
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    loi[0]=1000
NameError: name 'loi' is not defined. Did you mean: 'li'?
li[0]=1000
     
kk
     
[1, 2, 3, 4, [3, 5, 6, 7]]
id(kk)
     
2957115037312
kk
     
[1, 2, 3, 4, [3, 5, 6, 7]]
new_list[0]=100
     
new_list
     
[100, 2, 3, 4, [3, 5, 6, 7]]
from copy import deepcopy
     
hel(deeepcopy)
     
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    hel(deeepcopy)
NameError: name 'hel' is not defined. Did you mean: 'hex'?
help(deeepcopy)
     
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    help(deeepcopy)
NameError: name 'deeepcopy' is not defined. Did you mean: 'deepcopy'?
hel(deepcopy)
     
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    hel(deepcopy)
NameError: name 'hel' is not defined. Did you mean: 'hex'?
help(deepcopy)
     
Help on function deepcopy in module copy:

deepcopy(x, memo=None, _nil=[])
    Deep copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.

li =[1,2,3]
     
kk = [1,2,3,4,5,li]
     
new_list = deepcopy(kk)
     
new_list
     
[1, 2, 3, 4, 5, [1, 2, 3]]
kk
     
[1, 2, 3, 4, 5, [1, 2, 3]]
li
     
[1, 2, 3]
kk
     
[1, 2, 3, 4, 5, [1, 2, 3]]
new_list = kk.copy()
     
new_list
     
[1, 2, 3, 4, 5, [1, 2, 3]]
new_list[0] = 555
     
new_list
     
[555, 2, 3, 4, 5, [1, 2, 3]]
kk
     
[1, 2, 3, 4, 5, [1, 2, 3]]
new_list = deepcopy(kk)
     
kk
     
[1, 2, 3, 4, 5, [1, 2, 3]]
new_list[0] = 555
     
kk
     
[1, 2, 3, 4, 5, [1, 2, 3]]
new_list
     
[555, 2, 3, 4, 5, [1, 2, 3]]






st = "234wertyu"
     
s2 = "ggggggggggg"
     
s3 = "nAme Home"
     
st
     
'234wertyu'
print(s2)
     
ggggggggggg
prin(s3)
     
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    prin(s3)
NameError: name 'prin' is not defined. Did you mean: 'print'?
print(s3)
     
nAme Home
print(repr(st))
     
'234wertyu'
len(s2)
     
11
a = "Hello"
     
b = "hello"
     
c = "hello"
     
a == c
     
False
b == c
     
True
a  = 'fghj'
     
b = "fghj"
     
a == b
     
True
a
     
'fghj'
b
     
'fghj'


a += b
     
a
     
'fghjfghj'
a *= 9
     
a
     
'fghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghj'
9*= a
     
SyntaxError: 'literal' is an illegal expression for augmented assignment
9*a
     
'fghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghj'
a
     
'fghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghjfghj'
a = 'werty'
     
a
     
'werty'
ard
     
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    ard
NameError: name 'ard' is not defined. Did you mean: 'ord'?
ord
     
<built-in function ord>
chr
     
<built-in function chr>
a = "a"
     
ord(a)
     
97
ord("B")
     
66
ord("*")
     
42
ord("fd")
     
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    ord("fd")
TypeError: ord() expected a character, but string of length 2 found
chr(1000)
     
'Ϩ'
chr(1001)
     
'ϩ'
chr(1002)
     
'Ϫ'
fro i in range(2500,2600):
     
SyntaxError: invalid syntax
for i in range(2500,2600):
     print(chr(i), end="")

     
ৄ৅
৆েৈ৉৊োৌ্ৎ৏৐৑৒৓৔৕৖ৗ৘৙৚৛ড়ঢ়৞য়ৠৡৢৣ৤৥০১২৩৪৫৬৭৮৯ৰৱ৲৳৴৵৶৷৸৹৺৻ৼ৽৾৿਀ਁਂਃ਄ਅਆਇਈਉਊ਋਌਍਎ਏਐ਑਒ਓਔਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧ
for i in range(15000,20000):
     print(chr(i), end="")

     
㪘㪙㪚㪛㪜㪝㪞㪟㪠㪡㪢㪣㪤㪥㪦㪧㪨㪩㪪㪫㪬㪭㪮㪯㪰㪱㪲㪳㪴㪵㪶㪷㪸㪹㪺㪻㪼㪽㪾㪿㫀㫁㫂㫃㫄㫅㫆㫇㫈㫉㫊㫋㫌㫍㫎㫏㫐㫑㫒㫓㫔㫕㫖㫗㫘㫙㫚㫛㫜㫝㫞㫟㫠㫡㫢㫣㫤㫥㫦㫧㫨㫩㫪㫫㫬㫭㫮㫯㫰㫱㫲㫳㫴㫵㫶㫷㫸㫹㫺㫻㫼㫽㫾㫿㬀㬁㬂㬃㬄㬅㬆㬇㬈㬉㬊㬋㬌㬍㬎㬏㬐㬑㬒㬓㬔㬕㬖㬗㬘㬙㬚㬛㬜㬝㬞㬟㬠㬡㬢㬣㬤㬥㬦㬧㬨㬩㬪㬫㬬㬭㬮㬯㬰㬱㬲㬳㬴㬵㬶㬷㬸㬹㬺㬻㬼㬽㬾㬿㭀㭁㭂㭃㭄㭅㭆㭇㭈㭉㭊㭋㭌㭍㭎㭏㭐㭑㭒㭓㭔㭕㭖㭗㭘㭙㭚㭛㭜㭝㭞㭟㭠㭡㭢㭣㭤㭥㭦㭧㭨㭩㭪㭫㭬㭭㭮㭯㭰㭱㭲㭳㭴㭵㭶㭷㭸㭹㭺㭻㭼㭽㭾㭿㮀㮁㮂㮃㮄㮅㮆㮇㮈㮉㮊㮋㮌㮍㮎㮏㮐㮑㮒㮓㮔㮕㮖㮗㮘㮙㮚㮛㮜㮝㮞㮟㮠㮡㮢㮣㮤㮥㮦㮧㮨㮩㮪㮫㮬㮭㮮㮯㮰㮱㮲㮳㮴㮵㮶㮷㮸㮹㮺㮻㮼㮽㮾㮿㯀㯁㯂㯃㯄㯅㯆㯇㯈㯉㯊㯋㯌㯍㯎㯏㯐㯑㯒㯓㯔㯕㯖㯗㯘㯙㯚㯛㯜㯝㯞㯟㯠㯡㯢㯣㯤㯥㯦㯧㯨㯩㯪㯫㯬㯭㯮㯯㯰㯱㯲㯳㯴㯵㯶㯷㯸㯹㯺㯻㯼㯽㯾㯿㰀㰁㰂㰃㰄㰅㰆㰇㰈㰉㰊㰋㰌㰍㰎㰏㰐㰑㰒㰓㰔㰕㰖㰗㰘㰙㰚㰛㰜㰝㰞㰟㰠㰡㰢㰣㰤㰥㰦㰧㰨㰩㰪㰫㰬㰭㰮㰯㰰㰱㰲㰳㰴㰵㰶㰷㰸㰹㰺㰻㰼㰽㰾㰿㱀㱁㱂㱃㱄㱅㱆㱇㱈㱉㱊㱋㱌㱍㱎㱏㱐㱑㱒㱓㱔㱕㱖㱗㱘㱙㱚㱛㱜㱝㱞㱟㱠㱡㱢㱣㱤㱥㱦㱧㱨㱩㱪㱫㱬Traceback (most recent call last):
  File "<pyshell#110>", line 2, in <module>
    print(chr(i), end="")
KeyboardInterrupt
s = "㪙㪚㪛㪜㪝㪞㪟㪠㪡㪢㪣㪤㪥㪦㪧㪨㪩㪪㪫㪬㪭㪮㪯㪰㪱㪲㪳㪴㪵"
     
for i in s:
     print(ord(i), end="")

     
1500115002150031500415005150061500715008150091501015011150121501315014150151501615017150181501915020150211502215023150241502515026150271502815029
s = "hello"
     
len(s)
     
5
s[0]
     
'h'
s[2]
     
'l'
s[5]
     
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    s[5]
IndexError: string index out of range
s[0]="d"
     
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    s[0]="d"
TypeError: 'str' object does not support item assignment
s
     
'hello'
for let in s:
     print(let)

     
h
e
l
l
o
for let in s:
     print(let)

     
h
e
l
l
o
len(s)
     
5
for i in range(len(s)):
     print(i,s[i])

     
0 h
1 e
2 l
3 l
4 o

li = [1,2,3,4,5]
     
len(li)
     
5
for i in range(len(li)):
     print(i,li[i])

     
0 1
1 2
2 3
3 4
4 5





key = 5
     

text = "ancdefg"
     
ord("a")
     
97
chr(102)
     
'f'
mes = "hello! how are you? have a good day"
     
sec_m =""
     
sec_k = 5
     
for i in mes:
     sec_m+= chr(ord(i) + sec_k)

     
sec_m
     
'mjqqt&%mt|%fwj%~tzD%mf{j%f%ltti%if~'

#rasshifrovat nado
     
res_m = ""
     
for i in sec_m:
     res_m+= chr(ord(i) - sec_k)

     
res_m
     
'hello! how are you? have a good day'





s = "hello"
     
s
     
'hello'
s[0]
     
'h'
s[:3]
     
'hel'
s[2:]
     
'llo'
s[1:]
     
'ello'
s[1:3]
     
'el'
s[::-1]
     
'olleh'

li = [1,2,3,4,5]
     
li[1:4]
     
[2, 3, 4]
li[::1]
     
[1, 2, 3, 4, 5]
li[::2]
     
[1, 3, 5]
s
     
'hello'
s[::1]
     
'hello'
s[::2]
     
'hlo'
s[::-3]
     
'oe'
s[-1]
     
'o'
s[-3]
     
'l'
s[1]
     
'e'
s
     
'hello'





s = "a b c d e"
     
len(s)
     
9
s[4]
     
'c'
s[4]="C"
     
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    s[4]="C"
TypeError: 'str' object does not support item assignment

res_s = s[:4]+ "C" + [5:]
     
SyntaxError: invalid syntax
res_s = s[:4]+ "C" + s[5:]
     

res_s
     
'a b C d e'
s
     
'a b c d e'


#in not in
     

"a" in res_s
     
True
" " in res_s
     
True
"c" in res_s
     
False
"b" in res_s
     
True
"C" in res_s
     
True

"C" not in res_s
     
False
"a" not in res_s
     
False

s
     
'a b c d e'
del s
     
s
     
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    s
NameError: name 's' is not defined. Did you mean: 'st'?
s = "a b c d e f"
     

min
     
<built-in function min>
max
     
<built-in function max>
li = [1,2,3,4,666]
     
max(li)
     
666
min(li)
     
1
s
     
'a b c d e f'
min(s)
     
' '
min(s)
     
' '
max(s)
     
'f'
li =[]
     
max(li)
     
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    max(li)
ValueError: max() iterable argument is empty





s
     
'a b c d e f'
upper(s)
     
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    upper(s)
NameError: name 'upper' is not defined. Did you mean: 'super'?
s.upper()
     
'A B C D E F'
s.lower()
     
'a b c d e f'
s ="hello"
     
s.upper()
     
'HELLO'
s.lower()
     
'hello'
s.upper()
     
'HELLO'
s
     
'hello'
s.titte()
     
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    s.titte()
AttributeError: 'str' object has no attribute 'titte'. Did you mean: 'title'?
s = "hello hello hello"
     
s.title()
     
'Hello Hello Hello'
s.capitaize()
     
Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    s.capitaize()
AttributeError: 'str' object has no attribute 'capitaize'. Did you mean: 'capitalize'?
s.capitalize()
     
'Hello hello hello'
s.swapcase()
     
'HELLO HELLO HELLO'
s
     
'hello hello hello'
s.casefold()
     
'hello hello hello'
s
     
'hello hello hello'
s.isalpha()
     
False
s = "ghjk"
     
s.isalpha()

     
True
s
     
'ghjk'
 s ="3ee"
     
SyntaxError: unexpected indent
s="ew43"
     
s
     
'ew43'
s.isalpha()

     
False
c = " "
     
c.isspace()
     
True
c="N"
     
c.isspace()
     
False
c.istitle()
     
True

namme = input("name =")
     
name =sasha
name = name.captilize()
     
Traceback (most recent call last):
  File "<pyshell#268>", line 1, in <module>
    name = name.captilize()
NameError: name 'name' is not defined. Did you mean: 'namme'?
namme = namme.capitalize()
     

namme
     
'Sasha'
namme - inpur("->").capitalize()
     
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    namme - inpur("->").capitalize()
NameError: name 'inpur' is not defined. Did you mean: 'input'?
namme = inpur("->").capitalize()
     
Traceback (most recent call last):
  File "<pyshell#273>", line 1, in <module>
    namme = inpur("->").capitalize()
NameError: name 'inpur' is not defined. Did you mean: 'input'?
namme = input("->").capitalize()
     
->sasha
namme
     
'Sasha'
s = " peter "
     
s.capitalize()
     
' peter '
s
     
' peter '
s.strip()
     
'peter'
namme = input("->").capitalize()
     
->      fghjk           
namme
     
'      fghjk           '
namme = input("->")strip().capitalize()
     
SyntaxError: invalid syntax
namme = input("->").strip().capitalize()

->    ffffffffff        
name
     
Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    name
NameError: name 'name' is not defined. Did you mean: 'namme'?
namme
     
'Ffffffffff'
namme.replace("f","OLD")
     
'FOLDOLDOLDOLDOLDOLDOLDOLDOLD'
name = "sasha"
     
name = name.replace("a","OLD")
     
name
     
'sOLDshOLD'


n = input("->")
     
->1 2 3 4 5 6  7 8

n
...      
'1 2 3 4 5 6  7 8'
>>> n.split()
...      
['1', '2', '3', '4', '5', '6', '7', '8']
>>> 
>>> n
...      
'1 2 3 4 5 6  7 8'
>>> n = n.split()
...      
>>> n
...      
['1', '2', '3', '4', '5', '6', '7', '8']
>>> res = []
...      
>>> fro i in n:
...      
SyntaxError: invalid syntax
>>> for i in n:
...      res.append(int(i))
... 
...      
>>> res
...      
[1, 2, 3, 4, 5, 6, 7, 8]
>>> sum(res)
...      
36
>>> 
>>> 
>>> 
>>> n = [int(sn )for sn in input("->").split()]
...      
->1 2 3 4 5 
>>> n
...      
[1, 2, 3, 4, 5]
>>> sum(n)
...      
15
min(n)
     
1

Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

import requests
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
import requests
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
import requests






help(requests)
Help on package requests:

NAME
    requests

DESCRIPTION
    Requests HTTP Library
    ~~~~~~~~~~~~~~~~~~~~~

    Requests is an HTTP library, written in Python, for human beings.
    Basic GET usage:

       >>> import requests
       >>> r = requests.get('https://www.python.org')
       >>> r.status_code
       200
       >>> b'Python is a programming language' in r.content
       True

    ... or POST:

       >>> payload = dict(key1='value1', key2='value2')
       >>> r = requests.post('https://httpbin.org/post', data=payload)
       >>> print(r.text)
       {
         ...
         "form": {
           "key1": "value1",
           "key2": "value2"
         },
         ...
       }

    The other HTTP methods are supported - see `requests.api`. Full documentation
    is at <https://requests.readthedocs.io>.

    :copyright: (c) 2017 by Kenneth Reitz.
    :license: Apache 2.0, see LICENSE for more details.

PACKAGE CONTENTS
    __version__
    _internal_utils
    adapters
    api
    auth
    certs
    compat
    cookies
    exceptions
    help
    hooks
    models
    packages
    sessions
    status_codes
    structures
    utils

FUNCTIONS
    check_compatibility(
        urllib3_version,
        chardet_version,
        charset_normalizer_version
    )

DATA
    __author_email__ = 'me@kennethreitz.org'
    __build__ = 143875
    __cake__ = '✨ 🍰 ✨'
    __copyright__ = 'Copyright Kenneth Reitz'
    __description__ = 'Python HTTP for Humans.'
    __license__ = 'Apache-2.0'
    __title__ = 'requests'
    __url__ = 'https://requests.readthedocs.io'
    chardet_version = None
    charset_normalizer_version = '3.4.2'
    codes = <lookup 'status_codes'>

VERSION
    2.32.3

AUTHOR
    Kenneth Reitz

FILE
    c:\users\sasha_ch\appdata\local\programs\python\python313\lib\site-packages\requests\__init__.py


r = requests.get('https://api.github.com/events')
r.text()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    r.text()
TypeError: 'str' object is not callable
r
<Response [200]>



api_url = "https://jsonplaceholder.typicode.com/todos/1"
import requests as req


resp = req.get(api_url)
resp.status_code
200
resp.text
'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'
print(resp.te[t)
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
print(resp.text)
      
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
d_resp = resp.json()
      
d_resp
      
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
d_resp["title"]
      
'delectus aut autem'
type(resp.text)
      
<class 'str'>


users_url = "https://jsonplaceholder.typicode.com/todos/users"
      
u_resp = req.get(users_url)
      
u_resp.json()
      
{}
users_url = "https://jsonplaceholder.typicode.com/todos/users/2"
      
u_resp = req.get(users_url)
      
u_resp.json()
      
{}
Стефан Жаврид
19:56
users_url = "https://jsonplaceholder.typicode.com/users/2"
      
SyntaxError: invalid syntax


users_url = "https://jsonplaceholder.typicode.com/users/2"
      
usr_resp = req.get(users_url)
      
usr_resp.json()
      
{'id': 2, 'name': 'Ervin Howell', 'username': 'Antonette', 'email': 'Shanna@melissa.tv', 'address': {'street': 'Victor Plains', 'suite': 'Suite 879', 'city': 'Wisokyburgh', 'zipcode': '90566-7771', 'geo': {'lat': '-43.9509', 'lng': '-34.4618'}}, 'phone': '010-692-6593 x09125', 'website': 'anastasia.net', 'company': {'name': 'Deckow-Crist', 'catchPhrase': 'Proactive didactic contingency', 'bs': 'synergize scalable supply-chains'}}
usr_resp.json()[0]
      
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    usr_resp.json()[0]
KeyError: 0



todo_url =  "https://jsonplaceholder.typicode.com/todos/"
      
resp = req.get(todo_url+"1")
      
resp.json()
      
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

new_t = {'userId': 1, 'id': 1, 'title': 'buy cat', 'completed': False}

resp = req.put(todo_url+"1", json=new_t)
      
resp.status_code
      
200
resp = req.get(todo_url+"1")
      
resp.json()
      
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

new_t = {'userId': 1, 'title': 'buy cat', 'completed': False}

resp = req.put(todo_url+"1", json=new_t)

resp.status_code

200
resp.json()

{'userId': 1, 'title': 'buy cat', 'completed': False, 'id': 1}
>>> resp = req.get(todo_url+"1")
... 
>>> resp.json()
...       
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
>>> 
>>> 
>>> pos_url =  "https://jsonplaceholder.typicode.com/posts/"
...       
>>> resp = req.get(todo_url+"1")
...       
>>> resp.json()
...       
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
>>> resp = req.get(pos_url+"1")
...       
>>> resp.json()
...       
{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
>>> title = "dddddddddddddddd"
...       
>>> title = {"title":"ddddddddd"}
...       
>>> resp = req.patch(pos_url+"1", json=title)
...       
>>> resp.json()
...       
{'userId': 1, 'id': 1, 'title': 'ddddddddd', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
>>> resp1 = req.get(pos_url+"1")
...       
>>> resp1.json()
...       
{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}

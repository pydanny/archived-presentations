=============
Code samples
=============

Executed and displayed here so I can cut-and-paste into Keynote.

Whitespace
==========

.. sourcecode:: python

    """ whitespace.py """
    from random import randrange
    
    def numberizer():
        # Generate a random number from 1 to 10.
        return randrange(1, 11)
        
    number = numberizer()
    if number > 5:
        print("This number is big!")
        
    class RandomNumberHolder(object):
        # Create and hold 20 random numbers using numberizer
        
        def __init__(self):
            self.numbers = [numberizer(x) for x in range(20)]
            
    random_numbers = RandomNumberHolder()
    
Zen of Python
=============

.. sourcecode:: python

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


Strings
========

.. sourcecode:: python

    >>> foo = 'bar' # TODO: strike-out in slides
    >>> spam = 'eggs'
    
String methods
==============

.. sourcecode:: python
    
    >>> fun = 'spam and EGGS   '
    >>> dir(fun)
    ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',   
     '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
     '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__',
     '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
     '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
     '__subclasshook__', '_formatter_field_name_split', '_formatter_parser',
     'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs',
     'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
     'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace',
     'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
     'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
     'zfill']
    >>> fun.strip()
    'spam and EGGS'
    >>> spam.title()
    'Spam And Eggs   '
    >>> fun.capitalize()
    'Spam and eggs   '
    >>> fun.index('3')
    3
    >>> len(fun)
    16
    >>> fun.__len__() # same as the len function
    16
    >>> help(fun)
    no Python documentation found for 'spam and EGGS   '
    >>> help(str)

Help Slide Part I
==================

code::

    Help on class str in module __builtin__:

    class str(basestring)
     |  str(object) -> string
     |  
     |  Return a nice string representation of the object.
     |  If the argument is a string, the return value is the same object.
     |  
     |  Method resolution order:
     |      str
     |      basestring
     |      object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __contains__(...)
     |      x.__contains__(y) <==> y in x

Help Slide Part II
==================

code::

     |  capitalize(...)
     |      S.capitalize() -> string
     |      
     |      Return a copy of the string S with only its first character
     |      capitalized.
     |  
     |  center(...)
     |      S.center(width[, fillchar]) -> string
     |      
     |      Return S centered in a string of length width. Padding is
     |      done using the specified fill character (default is a space)
     |  
     |  count(...)
     |      S.count(sub[, start[, end]]) -> int
     |      
     |      Return the number of non-overlapping occurrences of substring sub in
     |      string S[start:end].  Optional arguments start and end are interpreted
     |      as in slice notation.
     
Play with strings
=================

sourcecode:: python

    >>> a = "I"
    >>> b = "like"
    >>> c = "Python"
    >>> a + b + c
    'IlikePython'
    >>> "{0} {1} {2}".format(a, b, c)
    'I like Python'
    >>> "{a} {b} {c}".format(a=a, b=b, c=c)
    'I like Python'
    >>> lst = [a,b,c]
    >>> lst
    ['I', 'like', 'Python']
    >>> " ".join(lst)
    'I like Python'
    >>> my_set, tpl = set(lst), tuple(lst)
    >>> tpl
    ('I', 'like', 'Python')
    >>> my_set
    set(['I', 'Python', 'like'])
    >>> ">".join(tpl)
    'I>like>Python'
    >>> "!".join(my_set)
    'I!Python!like'

List Comprehension
====================

.. sourcecode:: python

    >>> items = [x for x in range(20)]
    >>> items
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    >>> [x for x in range(20) if x % 2]
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    >>> # Fizzbuzz solved using Python's List Comprehension
    >>> lst = [(x, 'Fizz', 'Buzz', 'FizzBuzz') \ 
    ...     [(not x % 3) | (not x % 5) << 1] for x in range(20)]
    >>> for x in lst: print(x)
    FizzBuzz
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    16
    17
    Fizz
    19
    
    
    
Generator Expressions
=====================

.. sourcecode:: python

    >>> items = (x for x in range(20))
    >>> items
    <generator object <genexpr> at 0x100721460>
    
A generator expression evaluates only when the pointer is looking at that object.
This is really powerful, especially when working with resource/time intensive items
within an iterable.

.. sourcecode:: python

    >>> from time import sleep
    >>> items = ((x, sleep(x)) for x in range(20))
    >>> items.next()
    (0, None)
    >>> items.next()
    (1, None)
    >>> items.next()
    (2, None)
    >>> items.next()            
    (3, None)

Pygments
=========

First get the pygments code::

    pip install pygments

Then run this simple 'recursive' program:

.. sourcecode:: python

    from pygments import highlight
    from pygments.lexers import get_lexer_by_name
    from pygments.formatters import HtmlFormatter

    if __name__ == '__main__':
        code = open("pygments_demo.py", "rw").read()
        lexer = get_lexer_by_name("python", stripall=True)
        formatter = HtmlFormatter(linenos=False, cssclass="source")
        css = HtmlFormatter().get_style_defs('.source')
        highlighted_code = highlight(code, lexer, formatter)        
        page = """
            <html>
                <head><style>{css}</style></head>
                <body>{highlighted_code}</body>
            </html>
            """.format(css=css, highlighted_code=highlighted_code)
        print(page)

Now run the program and check the results::

    python pygments_demo.py > text.html
    open text.html
    
Isolate Environments
=====================

code::

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
    $ pip install virtualenv
    $ virtualenv my_env
    $ source my_env/bin/activate
    (my_env) $ 
    
More code::

    (my_env) $ pip install django==1.3.1
    (my_env) $ pip install requests==0.9.1
    (my_env) $ pip install mongoengine==0.5.2
    (my_env) $ pip install celery==2.4.6
    (my_env) $ pip install coverage==3.4
    (my_env) $ pip freeze
    celery==2.4.6
    coverage==3.4
    django==1.3.1
    mongoengine==0.5.2
    requests==0.9.1
    (my_env) $ pip freeze > requirements.txt
    ...
    (another_env) $ pip install -r requirements.txt
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

Strings are immutable

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
    
Diving into lists
=================

.. sourcecode:: python 

    lst = [1,2,3,4,5,"Python", [1,2,3,4]]
    
Sets dominate
===============

.. sourcecode:: python 

    >>> lst = [1,1,1,1,1,2,2,2,3,3,3,3,3,3]
    >>> s = set(lst)
    >>> s
    set([1,2,3])

How is this useful? What about counting unique words in a paragraph?

    >>> address = """Four score and seven years ago our fathers brought forth on this continent a new nation..."""
    >>> address = address.replace(',','').replace('.','').replace('-','')
    >>> words = address.split(' ')
    >>> len(words)
    278
    >>> unique_words = set(words)
    >>> len(unique_words)
    143

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

Persist SQL 
====================

.. sourcecode:: python

    from datetime import datetime

    from django.contrib.auth.models import User
    from django.db import models
    from django.utils.translation import ugettext_lazy as _
    
    class Post(models.Model):
    
        author = models.ForeignKey(User)
        title = models.CharField(_('Title'), max_length=100)
        content = models.TextField(_("Content"))
        pub_date = models.DateTimeField(_("Publication date"))
        
    class Comment(models.Model):
        post = models.ForeignKey(Post)
        name = models.CharField(_('Title'), max_length=100)
        content = models.TextField(_("Content"))
        
Persist NoSQL
=============

.. sourcecode:: python

    from django.utils.translation import ugettext_lazy as _

    import mongoengine as me
    
    class User(me.Document):
        email = me.StringField(_('email'), required=True)
        first_name = me.StringField(_('first name'), max_length=30)
        last_name = me.StringField(_('last name'), max_length=30)    
        
    class Post(me.Document):
        title = me.StringField(_('title'), max_length=100, required=True)
        author = me.ReferenceField(User)
        content = me.StringField(_('content'))
        pub_date = me.DateTimeField(_("Publication date"))

    class Comment(me.EmbeddedDocument):
        name = me.StringField(_('name'), max_length=100)    
        content = me.StringField(_('content'))
                
Message Queues
===============

dependencies::

    celery
    requests

tasks.py:

.. sourcecode:: python

    import logging
    import requests
    from celery import task
    
    from products.models import Product
    
    logger = logging.getLogger('products.tasks')
    
    @task
    def confirm_all_images():
    
        for product in Product.objects.all():
            response = request.get(product.medium_image.url)
            if response.status_code != 200:
                msg = "Product {0} missing image".format(product.id)
                logging.warning(msg)

Shell:

.. sourcecode:: python

    >>> from products.tasks import confirm_all_images
    >>> result = confirm_all_images.delay()
    >>> result.ready()
    False
    >>> result.ready()
    True
    
Exception Handling
===================

.. sourcecode:: python

    >>> import logging
    >>> logger = logging.getlogger()
    >>>
    >>> class CustomTypeError(Exception):
    ...     pass
        
    >>> try:
    ...     a = 1 + "Error"
    >>> except TypeError as e:
    ...     raise CustomTypeError(e)
    >>> except Exception as e:
    ...     logger.error(e)
        
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    __main__.CustomTypeError: unsupported operand type(s) for +: 'int' and 'str'
        
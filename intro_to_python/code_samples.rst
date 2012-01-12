=============
Code samples
=============

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

List Comprehension
====================

.. sourcecode:: python

    >>> [x for x in range(20)]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

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
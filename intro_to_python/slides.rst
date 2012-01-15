==========
Slides TOC
==========

* Opener

    * Subtitle: 20 cool things you can do with Python
    
* Who am I

    * History
    * Credentials
    
* Who uses Python?

    * Everyone!
    * Who doesn't use Python?
    * NASA, Canonical in Ubuntu, Google, et al
    * Startups, Scientists, Animation Studios, et al

* What is Python?

    * 20 years old and mature
    * A programming language named after Monty Python
    * Dynamically typed scripting language

* Python is similar to:

    * Ruby
    * Lisp
    * et al
    
* Python is different than:

    * Ruby
    * Java
    * Lisp
    
* Core concepts

    * Philosophy of Core devs
    
        * Conservative growth
        * *We read Knuth so you don’t have to*
        * Aim for simple implementation

    * Zen of Python
    
        * A few of my favorite lines
        
    * PEP-8

* Which Python to use?

* 20 Cool things you can do with Python
    
#. Learn it fast

    * Experienced developers take a week to get competent in Python
    * Java takes 6 months
    * C takes 2 years
    
#. Introspect

    * String basic type
    * dir
    * help  
    
#. Play with Strings

    * Concatenation
    * String formatting
    * Join iterables

#. Express yourself to laymen

    * Don't know Python? Bet you can read this!
    
#. Play with the REPL

    * Standard python shell
    * ipython
    * bpython

#. List Comprehension

    * [x for x in range(15)]
    * List Generators for ultimate power
    
#. Generate Exceptions
    
#. Create small, isolated environments for installing packages

    * Good for testing different versions of the same library::
    
    easy_install pip
    pip install virtualenv    
    virtualenv my_env
    source my_env/bin/activate
    
#. Generate the code coloration used in these slides.

    * http://pygments.org/
    * Show demo
    * Mention that both bitbucket and github use Pygments to colorize code.
    
#. Go faster than C and Javascript

    * Everyone knows C is fast, right?
    * And JavaScript on V8 is really fast too.
    * PyPy, an implementation of Python written in Python, runs faster.   
    * Faster than JavaScript, in some cases faster than C. 
    * Benchmarks, et al
    * http://en.wikipedia.org/wiki/PyPy
    * http://speed.pypy.org/
    * http://morepypy.blogspot.com/2012/01/numpypy-progress-report-running.html
    * http://blog.bossylobster.com/2011/08/lesson-v8-can-teach-python-and-other.html
    * Quora is the best known prominent user at this time
    * Integration with numpy and other scientific libraries in progress
    
#. Persist

    * LRU caching
    * Connect to SQL databases
    * Connect to NoSQL
    
#. Build websites

#. Internationalize

    * unicode
    * gettext implementation
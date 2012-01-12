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

    * Experienced developers take a week to get competent
    * Java takes 6 months
    * C takes 2 years
    
#. Introspect

    * String basic type
    * dir
    * help    

#. Express yourself to laymen

    * Don't know Python? Bet you can read this!
    
#. Play with the REPL

    * Standard python shell
    * ipython
    * bpython

#. List Comprehension

    * [x for x in range(60)]
    * List Generators for ultimate power
    
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
    
#. Go faster than Javascript

    * Everyone knows Javascript is fast, right?
    * PyPy, an implementation of Python written in Python, runs faster.   
    * Faster than JavaScript, in some cases faster than C. 
    * Benchmarks, et al
    * http://en.wikipedia.org/wiki/PyPy
    * http://speed.pypy.org/
    * Quora is the best known prominent user at this time
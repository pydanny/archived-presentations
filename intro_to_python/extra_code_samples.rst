You're going to enjoy lists.

Basic list operations
=====================

sourcecode:: python

    >>> my_list = [1, 2, 3]
    >>> my_list.append(4)
    >>> my_list
    [1, 2, 3, 4]
    >>> my_list.insert(2, 'dog')
    >>> my_list
    [1, 2, 'dog', 3, 4]
    >>> my_list.extend([5, 6])
    >>> my_list
    [1, 2, 'dog', 3, 4, 5, 6]
    >>> my_list.append([7, 8])
    >>> my_list
    [1, 2, 'dog', 3, 4, 5, 6, [7, 8]]
    >>> my_list.pop(2)
    'dog'
    >>> my_list
    [1, 2, 3, 4, 5, 6, [7, 8]]
    >>> my_list.reverse()
    >>> my_list
    [[7, 8], 6, 5, 4, 3, 2, 1]

Lists + functional programming
==============================

sourcecode:: python

    def divisible_by_2(x):
        return x % 2 == 0

    def cube(x):
        return x * x * x

    >>> numbers = [1, 2, 3, 4, 6, 31]

    >>> filter(divisible_by_2, numbers)
    >>> [2, 4, 6]
    
    >>> map(cube, numbers)
    >>> [1, 8, 27, 64, 216, 29791]

Generators
==========

def print_5_lines(filename):
    """ Prints the first 5 lines of the given file. """
    my_file = open(filename)    # my_file is a generator expression
    for i in range(5):
        line = my_file.next()
        print line

This is useful for gigantic files, such as 100MB system logs.


.. Pydanny Presentations documentation master file, created by
   sphinx-quickstart on Tue Jan 10 19:08:54 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pydanny PresentationS
=================================================

Contents:

.. toctree::
   :maxdepth: 2
   
   intro_to_python/index
   heroku-case-study/index


List of Dictionaries
=====================
            
.. code-block:: python

    collection = []
    document = {
            '_objectId': ObjectId('4f844e916c97c1000c000003'),
            'username': 'pydanny',
            'fiancee': 'audreyr'
        }
    collection = [document, ]
    collection = [document]  # JavaScript version. :-)
    
    
MongoKit Model Example
======================

.. code-block:: python

    from mongokit import Document, Connection
    import datetime

    connection = Connection()

    @connection.register
    class Review(Document):
        structure = {
                'title':unicode,
                'body':unicode,
                'author':unicode,
                'created':datetime.datetime,
                'rating':int
        }
        required_fields = ['title', 'author', 'created']
        default_values = {'rating':0, 'created':datetime.datetime.utcnow}
                       
MongoKit Query Example
======================

.. code-block:: python
    
    >>> from mongokit import Connection
    >>> connection = Connection()
    >>> for post in connection.Review.find():
    ...     print post['title']    
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
        default_values = {'rating': 0, 'created': datetime.utcnow}
                       
MongoKit Query Example
======================

.. code-block:: python
    
    >>> from mongokit import Connection
    >>> connection = Connection()
    >>> for review in connection.Review.find({'rating': 3}):
    ...     review['title']    
    
MongoEngine Model Example
===========================

.. code-block:: python

    import mongoengine as me

    class Review(me.Document):

        title = me.StringField()
        body = me.StringField()
        author = me.StringField()
        created = me.DateTimeField(default=datetime.utcnow)
        rating = me.IntField()

MongoEngine Query Example
=========================

.. code-block:: python

    >>> from reviews.models import Review
    >>> for review in Review.objects.all():
    ...     review.title
    
PyMongo Model Example    
======================

.. code-block:: python

    >>> from pymongo import Connection
    >>> connection = Connection()
    >>> my_data = {'rating': 3, 'title': 'I like ice cream'}
    >>> connection.reviews.insert(my_data)
    >>> your_data = {'rating': 3, 'name': 'You like ice cream'}
    >>> connection.reviews.insert(your_data)

PyMongo Query Example
=======================

.. parsed-literal::

    >>> connection = pymongo.Connection()
    >>> db = connection.db
    >>> for review in db.reviews.find({'rating': 3}):
    ...     review['title']
    >>> for review in db.reviews.find(
    ...        {"title": {"$regex": "ice cream"} }
    ...        ):
    ...     review['title']
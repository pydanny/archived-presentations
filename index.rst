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
   
.. code-block:: python

    class BaseMongoModel(dict):
        """ Smells like a dict but is instantiated like a class.
             Used as the superclass on pymongo Model types
             Default fields:

                 _id: object_id
                 created: datetime()
                 modified: datetime()
         """    

        def __init__(self, **kwargs):
            """ Checks to make sure all necessary fields are there. Also assigns some critical defaults """

            if 'modified' not in self and 'modified' not in kwargs:
                self['modified'] = datetime.now()

            # make that created field now
            if 'created' not in self and 'created' not in kwargs:
                self['created'] = datetime.now()

            if '_id' in kwargs and not isinstance(kwargs['_id'], ObjectId):
                raise InvalidObjectId

            if '_id' in kwargs:
                self['pk'] = str(kwargs['_id'])
                self['id'] = str(kwargs['_id'])
            self.update(kwargs)
            
.. code-block:: python

    collection = []
    document = {
            '_objectId': ObjectId('4f844e916c97c1000c000003'),
            'username': 'pydanny',
            'fiancee': 'audreyr'
        }
    collection = [document, ]
    collection = [document]  # JavaScript version. :-)
    
KeyableModel
=============

The concept of a keyable model was "inspired" by the Ruby on Rails cache_key system where you cache partials 
based on the updated timestamp of the instance. This leverages memcached `LRU`_ algorithm where unused
cache items are not a problem and are discarded after a while of not being used.

.. _LRU: http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used

Installation
-------------

To make a model a Keyable Model you need to inherit that class in your model:

.. code-block :: python

  from cache_tools.models import KeyableModel
  # ...
  class Profile(KeyableModel):
    # Your model stuff

Then sync your db or create your south migration:

.. code-block :: bash
  
  python manage.py schemamigration front add_keyable_model --auto


Usage
-------------

To use it in your templates you must pass the cache key as a parameter to the cache block:

.. code-block :: html

    {% load cache %}
    {% cache 86400 cache_tools profile.cache_key %}
        <p>
            Lots of very time consuming code.
        </p>
    {% endcache %}



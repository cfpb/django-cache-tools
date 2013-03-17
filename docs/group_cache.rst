Group Cache
============

The idea behind group caching is to have a set of pages that you group under a certain name
allowing you to expire the whole set instead of having to look for the individual cache entries.

Usage
-------------

To cache a page in a group you just use the cache_page_in_group decorator:

.. code-block :: python

  #views.py
  from cache_tools.tools import cache_page_in_group

  @cache_page_in_group('profiles')
  def show(req, slug):
    # ...


When you need to expire that group you use the expire_cache_group method:

.. code-block :: python

  from cache_tools.tools import expire_cache_group
  # ...
  expire_cache_group('profiles')

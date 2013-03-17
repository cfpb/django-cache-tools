Django Cache Tools
========================

Django Cache tools is a basic set of tools to built on top of the django cache framework
to make it easier to use and add caching related features.

Tools included
------------------------------------
- KeyableModel: Model that has a cache_key to cache with.
- expire_page: Expire a page with a given path.
- @cache_page_in_group: Cache pages with a given group name so they can be expired all at one.


Running the Tests
------------------------------------

You can run the tests with via::

    python runtests.py

Django Cache Tools
========================

[![Build Status](https://travis-ci.org/cfpb/django-cache-tools.png?branch=master)](https://travis-ci.org/cfpb/django-cache-tools)

Django Cache tools is a basic set of tools to built on top of the django cache framework
to make it easier to use and add caching related features.

Tools included
------------------------------------
- KeyableModel: Model that has a cache_key to cache with.
- expire_page: Expire a page with a given path.
- @cache_page_in_group: Cache pages with a given group name so they can be expired all at one.

Documentation
------------------------------------
You can find the docs at http://django-cache-tools.readthedocs.org/.

Running the Tests
------------------------------------

You can run the tests with via::

    python runtests.py

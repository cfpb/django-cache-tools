expire_page method
=============

Django has a great cache framework but doesn't provide an easy way to expire 
a view that has been cached.

This method does just that.

Example
-------------

If you have a view like:

.. code-block :: python
  
  #views.py
  @cache_page(60 * 10)
  def show(req, slug):
    # ...

  #urls.py
  # ...
  url(r'^profile/(?P<stub>.*)/$', 'show', name='show_profile'),
  # ...

Then you can use expire_page like:

.. code-block :: python

  from cache_tools.tools import expire_page
  # ...
  expire_page(reverse('show_profile', args=(stub,)))
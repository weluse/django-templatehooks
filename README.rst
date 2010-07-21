=====================
Django Template Hooks
=====================

`django-templatehooks` is a Django app that offers template hooks to provide an easy interface for pluggable apps to extend your templates.

Installation
------------

From PyPi::

   pip install django-templatehooks

From Git::

   pip install -e git://github.com/weluse/django-templatehooks#egg=templatehooks

Usage
-----

Add ``django-templatehooks`` to ``INSTALLED_APPS``.
Afterwards, create a hook inside any template.

``base.html``::

   ...
   <div id="header">
      <h1>Welcome!</h1>
      {% hook header_end %}
   </div>
   ...

Every hook must be registered once. This is done via the ``registry.register``
method::

   from templatehooks.registry import registry

   registry.register('header_end')

Connect to the hook inside a pluggable app. The ``models.py`` is usually a good
place for this, because it's dynamically imported if the app is enabled. It's
also the preferred place for signal bindings and `django-templatehooks` utilizes
django's signal infrastructure.

::

   from templatehooks.registry import registry


   def _connect_level2_heading(sender, **kwargs):
      """Adds a second heading at the end of the header box."""
      kwargs['content'].append("<h2>I'm dynamically added</h2>")


   registry.connect('header_end', _connect_level2_heading)

That's it. The sender parameter is an instance of the template's context, so you
can look up the request there, if a ``RequestContext`` was used.

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

Add ``templatehooks`` to ``INSTALLED_APPS``.
Afterwards you can create hooks inside any template you would like to extend
from other apps.

``base.html``::

   {% load templatehooks %}
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
       kwargs['content'].append(u"<h2>I'm dynamically added</h2>")


   registry.connect('header_end', _connect_level2_heading)

That's it. The sender parameter is an the hook registry. To access
context variables or the request object, a ``context`` instance is provided with
the ``kwargs``.

::

   from templatehooks.registry import registry


   def _connect_level2_heading(sender, **kwargs):
       """Adds a second heading at the end of the header box."""
       request = kwargs['context']['request']
       kwargs['content'].append(u"<h2>Hello, {0}!</h2>".format(
         request.user.format(request.user.username)))


   registry.connect('header_end', _connect_level2_heading)

In order to access the request object, a ``RequestContext`` must be used to
render the template containing the hook.

Decorators
~~~~~~~~~~

.. versionadded:: 0.3

An easier approach is to use the decorator syntax which combines the
above code into this snippet::

   from templatehooks.decorators import hook

   @hook('header_end')
   def render_level2_heading(context):
       return u"<h2>I'm dynamically added</h2>"

As you can see, the context is provided as first parameter.

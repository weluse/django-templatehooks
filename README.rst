=====================
Django Template Hooks
=====================

`django-templatehooks` is a Django app that offers template hooks to provide an
easy interface for pluggable apps to extend your templates.

Branch
------

This is an experimental branch which does no longer require you to explicitly
register your hooks. Instead they're automatically registered on first usage.

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

Connect to the hook inside a pluggable app. The ``models.py`` is usually a good
place for this, because it's dynamically imported if the app is enabled. It's
also the preferred place for signal bindings and `django-templatehooks` utilizes
django's signal infrastructure internally.

::

   from templatehooks.decorators import hook

   @hook('header_end')
   def render_level2_heading(context):
       return u"<h2>I'm dynamically added</h2>"

That's it. As you can see, you get the current template context object as first
parameter to your hook function. In order to access the request object, a
``RequestContext`` must be used to render the template containing the hook.

If you have multiple endpoints you want to attach your hook to, you can pass
multiple names to the ``@hook`` decorator::

   from templatehooks.decorators import hook

   @hook('header_end', 'footer_start')
   def render_level2_heading(context):
       return render_to_string("_hook.html", context['user'])


Low level connect
~~~~~~~~~~~~~~~~~

Instead of using decorators, you can also utilize the low level interface to
connect to a hook.

::

   from templatehooks.registry import registry


   def _connect_level2_heading(sender, **kwargs):
       """Adds a second heading at the end of the header box."""
       request = kwargs['context']['request']
       kwargs['content'].append(u"<h2>Hello, {0}!</h2>".format(
         request.user.username))


   registry.connect('header_end', _connect_level2_heading)


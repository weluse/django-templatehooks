# -*- coding: utf-8 -*-
"""
templatehooks.decorators
~~~~~~~~~~~~~~~~~~~~~~~~

Decorators for easy creation of templatehooks.

:copyright: 2010, weluse (http://weluse.de)
:author: Pascal Hartig <phartig@weluse.de>
:license: BSD
"""

from functools import wraps
from templatehooks.registry import registry


def hook(*names):
    """
    Decorator for creating a templatehooks.

    Example::

        @hook('header_end')
        def my_hook(context):
            return u"Hello, World!"

    Example for multiple hooks::

        @hook('header_end', 'footer_start')
        def my_hook2(context):
            return u"<h2>My dynamic level-2-heading</h2>
    """

    def _outer(func):

        @wraps(func)
        def _inner(sender, **kwargs):
            context = kwargs.get('context', None)
            kwargs['content'].append(func(context))
            return func

        for name in names:
            registry.connect(name, _inner)

        return _inner

    return _outer

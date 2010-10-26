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


def hook(name):
    """
    Decorator for creating a templatehooks.

    Example::

        @hook('header_end')
        def my_hook(context):
            return u"Hello, World!"
    """

    def _outer(func):

        @wraps(func)
        def _inner(sender, **kwargs):
            context = kwargs.get('context', None)
            kwargs['content'].append(func(context))
            return func

        registry.connect(name, _inner)
        return _inner

    return _outer

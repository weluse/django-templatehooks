# -*- coding: utf-8 -*-
"""
templatehooks.registry
~~~~~~~~~~~~~~~~~~~~~~

Registry for template hook signals.

:copyright: 2010, weluse (http://weluse.de)
:author: Pascal Hartig <phartig@weluse.de>
:license: 2010
"""

from django.dispatch.dispatcher import Signal


class HookRegistry(object):
    """Storage for template hooks."""

    def __init__(self):
        self._registry = {}

    def register(self, name, signal=None):
        """
        Register a new template hook or override an existing.

        :param name: Name of the template hook.
        :param signal: The signal to use for the hook. If not provided, it
        is created.
        """

        if signal:
            if not isinstance(signal, Signal):
                raise TypeError("Signal {0} is not of type "
                    "django.dispatch.dispatcher.Signal!".format(name))
            if 'content' not in signal.providing_args:
                raise TypeError("Signal {0} does not provide a 'content' "
                    "parameter!".format(name))
        else:
            signal = Signal(providing_args=['content'])

        self._registry[name] = signal

    def connect(self, name, fn):
        """
        Connect a function ``fn`` to the template hook ``name``.

        An example hook could look like this::
            function my_hook(sender, **kwargs):
                # Get the request from context
                request = sender['request']
                kwargs['content'].append("Hello, {0}!".format(request.user))
        """

        signal = self._registry[name]
        signal.connect(fn)

    def get_content(self, name, context):
        """
        Get the content of a template hook. Used internally by the hook
        templatetag.
        """

        signal = self._registry[name]
        content = []
        signal.send(sender=context, content=content)

        return '\n'.join(content)


registry = HookRegistry()
__all__ = ('registry',)

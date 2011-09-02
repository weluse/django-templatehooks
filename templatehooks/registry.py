# -*- coding: utf-8 -*-
"""
templatehooks.registry
~~~~~~~~~~~~~~~~~~~~~~

Registry for template hook signals.

:copyright: 2010, weluse (http://weluse.de)
:author: Pascal Hartig <phartig@weluse.de>
:license: BSD
"""

import warnings
import threading
from django.dispatch.dispatcher import Signal


# Lock used to control dynamic signal creation.
_registry_lock = threading.Lock()


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
            signal = Signal(providing_args=['content', 'context'])

        self._registry[name] = signal
        return signal

    def connect(self, name, fn):
        """
        Connect a function ``fn`` to the template hook ``name``.

        An example hook could look like this::

            function my_hook(sender, **kwargs):
                # Get the request from context
                request = kwargs['context']['request']
                kwargs['content'].append("Hello, {0}!".format(request.user))

            registry.connect('hookname', name)

        If the given hook name does not exist at runtime, it is created
        dynamically.
        """

        with _registry_lock:
            try:
                signal = self._registry[name]
            except KeyError:
                signal = self.register(name)

        signal.connect(fn)

    def get_content(self, name, context):
        """
        Get the content of a template hook. Used internally by the hook
        templatetag.

        If the referenced hook name has not been manually registered and there
        are no hooks attached to it, a warning is issued.
        """

        try:
            signal = self._registry[name]
        except KeyError:
            message = ("There are no connected functions for the hook '%s'." %
                       name)
            warnings.warn(message, RuntimeWarning)
            return u''

        content = []
        signal.send(sender=self, context=context, content=content)

        return u'\n'.join(content)


registry = HookRegistry()
__all__ = ('registry',)

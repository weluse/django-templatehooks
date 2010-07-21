# -*- coding: utf-8 -*-
"""
templatehooks.templatetags.templatehooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides easy access to templatehooks via a templatetag.

:copyright: 2010, Pascal Hartig <phartig@rdrei.net>
:license: commercial
"""
# pylint: disable-msg=C0103,R0903

from django.dispatch.dispatcher import Signal
from ..registry import registry
from django import template

register = template.Library()


class TemplateHookNode(template.Node):
    """
    Renders the {% hook %} template tag.
    """

    def __init__(self, name, as_var=None):
        self.name = name
        self.as_var = as_var

    def render(self, context):
        """
        Fires the given signal and renders the list values in return.
        """

        content = registry.get_content(self.name, context)

        if self.as_var:
            context[self.as_var] = content
            return ''

        return content


# pylint: disable-msg=W0613
@register.tag(name="hook")
def do_template_hook(parser, token):
    """
    Example use::
        {% hook {signal_name} %}
        or
        {% hook {signal_name} as {context_var} %}

    The signal must be registered with the templatehooks registry::

        >>> from templatehooks.registry import registry
        >>> registry.register('signal_name')
    """

    bits = token.split_contents()

    as_var = None
    if len(bits) == 2:
        name = bits[1]
    elif len(bits) == 4:
        name = bits[1]
        as_var = bits[3]
    else:
        raise template.TemplateSyntaxErrors("%s takes either two or four "
            "arguments: {% hook {signal_name} [as {context_var}] %}" % bits[0])

    return TemplateHookNode(name, as_var)

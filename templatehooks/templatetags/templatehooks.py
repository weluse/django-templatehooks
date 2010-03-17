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
        Fires the given signal and renders the list values in response.
        """

        content = registry.get_content(self.name, context)

        if self.as_var:
            context[self.as_var] = rendered_content
            return ''

        return rendered_content


# pylint: disable-msg=W0613
@register.tag(name="hook")
def do_template_hook(parser, token):
    """
    Extends your templates easily with pluggable apps.

    Example use::
        {% hook {signal_name} %}
        or
        {% hook {signal_name} as {context_var} %}

    The signal must be defined, currently inside this module's models.

    To use a template hook you connect to the signal and modify the signal's
    content variable::

        from templatetags.models import my_hook_name

        def extend_hook(signal, **kwargs):
            kwargs['content'].append("Hello World!")

        my_hook_name.connect(extend_hook)
    """

    bits = token.split_contents()

    as_var = None
    if len(bits) == 2:
        name = bits[1]
    elif len(bits) == 4:
        name = bits[1]
        as_var = bits[3]
    else:
        raise template.TemplateSyntaxErrors("{0} takes either two or four "
            "arguments: {% hook {signal_name} [as {context_var}] %}")

    return TemplateHookNode(name, as_var)

from django.template.loader import render_to_string
from django.template import RequestContext
from templatehooks.decorators import hook


def _render_sidebar_entry(request):
    context = RequestContext(request, {
        'value': u"Dynamic Sidebar Entry"
    })
    return render_to_string("example/_sidebar_entry.html", context)


def _render_heading():
    return u"Hello templatehooks!"

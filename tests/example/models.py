from .views import _render_sidebar_entry, _render_heading
from templatehooks.registry import registry
from templatehooks.decorators import hook


def _connect_level_heading(sender, **kwargs):
    kwargs['content'].append(_render_heading())


def _connect_sidebar_entry(sender, **kwargs):
    kwargs['content'].append(_render_sidebar_entry(sender['request']))

@hook('header_end')
def _render_second_heading(request):
    return u"<p>Hello from decorator!</p>"


registry.connect('header_end', _connect_level_heading)
registry.connect('sidebar_start', _connect_sidebar_entry)

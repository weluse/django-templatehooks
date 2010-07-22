from .views import _render_sidebar_entry, _render_heading
from templatehooks.registry import registry


def _connect_level_heading(sender, **kwargs):
    kwargs['content'].append(_render_heading())


def _connect_sidebar_entry(sender, **kwargs):
    kwargs['content'].append(_render_sidebar_entry(sender['request']))


registry.connect('header_end', _connect_level_heading)
registry.connect('sidebar_start', _connect_sidebar_entry)

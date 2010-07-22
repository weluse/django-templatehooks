from django.test import TestCase
from django.conf import settings
from templatehooks.registry import registry


class TemplateHooksDisabledTestCase(TestCase):
    """
    Test that without the example app enabled no hooks are triggered.
    """

    def test_index(self):
        """Request the index page and check the hooks are not used."""
        assert 'example' not in settings.INSTALLED_APPS

        response = self.client.get('/')
        self.assertTemplateNotUsed(response, "example/_sidebar_entry.html")
        self.assertNotContains(response, u"Hello templatehooks!")

    def test_signals(self):
        """Make sure the signals are fired."""

        _signals_fired = []

        def _connect_sidebar(sender, **kwargs):
            _signals_fired.append('sidebar')

        def _connect_header(sender, **kwargs):
            _signals_fired.append('header')

        registry.connect('sidebar_start', _connect_sidebar)
        registry.connect('header_end', _connect_header)

        self.client.get('/')
        self.assertEquals(len(_signals_fired), 2)
        self.assertTrue('sidebar' in _signals_fired)
        self.assertTrue('header' in _signals_fired)

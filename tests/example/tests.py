import warnings
from django.test import TestCase
from templatehooks.registry import registry


class TemplateHooksEnabledTestCase(TestCase):
    """
    TestCase with enabled example app.
    """

    def test_index(self):
        """Request the index page and check for hook contents."""

        response = self.client.get('/')
        self.assertTemplateUsed(response, "example/_sidebar_entry.html")
        self.assertContains(response, u"Hello templatehooks!")
        self.assertContains(response, u"Hello from decorator!")

    def test_get_content_warning(self):
        """Test requesting content from a non-existent hook."""

        with warnings.catch_warnings(record=True) as warn:
            registry.get_content('doesnotexist', {})
            assert len(warn) == 1
            assert issubclass(warn[-1].category, RuntimeWarning)

    def test_get_no_content_warning(self):
        """Test requesting content from an existent hook."""

        registry.register('doesexist')

        with warnings.catch_warnings(record=True) as warn:
            registry.get_content('doesexist', {})
            assert len(warn) == 0

    def test_implicit_registration(self):
        """Register a hook implicitly."""

        mycontext = {}
        result = u"I am Dave! Yognaught."

        def _myhook(sender, **kwargs):
            context = kwargs.get('context')
            assert id(mycontext) == id(context)
            kwargs['content'].append(result)

        registry.connect('myhook', _myhook)
        self.assertEquals(result, registry.get_content('myhook', mycontext))

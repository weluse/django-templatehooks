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

    def test_silent_failing(self):
        """Test 'silent' failing."""

        hookfn = lambda x, y: ''

        with warnings.catch_warnings(record=True) as warn:
            registry.connect('doesnotexist', hookfn, fail_silently=True)
            assert len(warn) == 1
            assert issubclass(warn[-1].category, RuntimeWarning)

    def test_loud_failing(self):
        """Expect an Exception when fail_silently == False"""

        hookfn = lambda x, y: ''

        self.assertRaises(RuntimeError,
                          lambda: registry.connect('doesnotexist', hookfn,
                                                   fail_silently=False))

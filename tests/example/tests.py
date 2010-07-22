from django.test import TestCase


class TemplateHooksEnabledTestCase(TestCase):
    """
    TestCase with enabled example app.
    """

    def test_index(self):
        """Request the index page and check for hook contents."""

        response = self.client.get('/')
        self.assertTemplateUsed(response, "example/_sidebar_entry.html")
        self.assertContains(response, u"Hello templatehooks!")

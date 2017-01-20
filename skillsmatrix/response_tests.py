from django.test import TestCase


class ResponseTestCase(TestCase):
    """Some additional assertions for Django responses."""
    def assertHttp200(self, response):
        status_code = response.status_code
        self.assertEqual(
            status_code, 200,
            "Expected a HTTP 200 response, but got HTTP %d" % status_code)

    def assertPermissionDenied(self, response):
        status_code = response.status_code
        self.assertEqual(
            status_code, 403,
            "Expected a HTTP 403 (denied), but got HTTP %d" % status_code)
        self.assertTemplateUsed(
            response, 'denied.html',
            "Expected denied.html to be rendered for the response.")

    def assertFormInvalid(self, response):
        """Assert that the response contains a form in the context, and that
        the form failed validation.
        """
        form = None
        try:
            if response.context:
                form = response.context['form']
        except KeyError:
            pass

        if not form:
            self.fail("Could not find a form in the response.")
        
        self.assertFalse(form.is_valid(), "Expected form to be invalid, but it was valid.")

        status_code = response.status_code
        self.assertEqual(
            status_code, 200,
            "Expected HTTP 200, but got HTTP %d. "
            "Looks like the form validated when it shouldn't." % status_code)

    def assertRedirects(self, response, expected_url):
        """Django's assertRedirects doesn't support external URLs, so we roll
        our own here. Note that the test client can't fetch external
        URLs, so we mustn't use fetch=True.
        """
        if response.status_code != 302:
            self.fail("Did not redirect (got HTTP %s instead)." % response.status_code)

        if hasattr(response, "redirect_chain"):
            self.fail("You can't use assertRedirects with follow=True.")
        
        final_url = response._headers['location'][1]

        if not expected_url.startswith('http://'):
            # we were given a relative URL, so convert it
            expected_url = "http://testserver%s" % expected_url

        self.assertEqual(
            final_url, expected_url,
            "Expected to be redirected to %s, but got %s instead." % (expected_url, final_url)
        )

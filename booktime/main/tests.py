from django.test import TestCase

# We are writing a test focusing on testing the behaviour at the HTTP level

class TestPage(TestCase):
    # Home page test cases:
    # Http status code = 200
    # the template home.html has been used
    # response contains the name of our shop
    def test_home_page_works(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'BookTime')
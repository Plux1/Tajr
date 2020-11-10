from django.test import TestCase
from django.urls import reverse

#The reverse() method imported here allow to call url path via their names
# We are writing a test focusing on testing the behaviour at the HTTP level

class TestPage(TestCase):
    # Home page test cases:
    # Http status code = 200
    # the template home.html has been used
    # response contains the name of our shop
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'BookTime')
    
    # About us page test case
    # Http status code = 200
    # The template about_us.html has been used
    # Response contains the name of our shop (BookTime)
    def test_about_us_page(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
        self.assertContains(response, 'BookTime')
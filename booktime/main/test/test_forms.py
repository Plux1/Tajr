from django.test import TestCase
from django.core import mail
from main import forms

class TestForm(TestCase):
    #Here we are testing both valid and invalid form data
    def test_valid_contact_us_form_sends_email(self):
        form = forms.ContactForm({
            'name': 'Issa Rajabu Juma',
            'message': 'H there!'
        })

        self.assertTrue(form.is_valid())
        form.send_mail()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Site message')
    
    def test_invalid_contact_us_form(self):
        form = forms.ContactForm({
            'message': 'Hi there'
        })

        self.assertFalse(form.is_valid())
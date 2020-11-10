from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.CharField(max_length=600, widget=forms.Textarea )

    # Method to send emails
    def send_mail(self):
        message = "From: {0}\n{0}".format(self.cleaned_data['name'], self.cleaned_data['message'])
        send_mail("Site message", message, "site@booktime.domain", ["customerservice@booktime.domain"], fail_silently=False)
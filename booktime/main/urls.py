from django.urls import path
from django.views.generic import TemplateView

# Make sure to name your urls so that they can be easly referenced
# Naming url path provide a single point of modification if we ever want to change the urls
# Named url path allow the use of reverse() method that map the path name to the actual url path 

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('about/', TemplateView.as_view(template_name='about_us.html'), name='about')
]


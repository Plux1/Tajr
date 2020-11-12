from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    # initialize signals.py file when the django application is launched 
    # by the internal django application registry
    def read(self):
        from . import signals

from django.apps import AppConfig # contains configuration meta data for the app


class FirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'firstapp'

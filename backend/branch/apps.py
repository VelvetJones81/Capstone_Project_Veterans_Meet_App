from django.apps import AppConfig


class BranchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'branch'

def __str__(self):
    return self.name


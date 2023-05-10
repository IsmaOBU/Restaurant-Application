from django.apps import AppConfig


class StaffregistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StaffRegistration'


    def ready(self):
        import StaffRegistration.signals

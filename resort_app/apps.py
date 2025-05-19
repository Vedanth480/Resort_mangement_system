from django.apps import AppConfig

class ResortAppConfig(AppConfig):  # Use PascalCase for class names
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resort_app'

    def ready(self):
        import resort_app.signals  # This ensures signals are registered

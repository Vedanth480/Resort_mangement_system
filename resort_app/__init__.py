from django.apps import AppConfig

class ResortAppConfig(AppConfig):  # ✅ Class name starts with capital letters
    name = 'resort_app'

    def ready(self):
        import resort_app.signals  # ✅ This ensures your signals are loaded

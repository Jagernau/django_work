from django.apps import AppConfig


class BirixConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "birix"
    verbose_name = "Для Битрикс"

    # def ready(self):
    #     import birix.signals

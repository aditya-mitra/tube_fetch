from os import environ
from django.apps import AppConfig


class ResultsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "results"

    def ready(self):
        from results.utils.fetch_youtube_results import start_scheduler
        start_scheduler()

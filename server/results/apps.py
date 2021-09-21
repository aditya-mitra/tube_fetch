from django.apps import AppConfig


class ResultsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "results"

    run_complete = False

    def ready(self):
        from results.utils.fetch_youtube_results import start_scheduler

        if not self.run_complete:
            start_scheduler()
            self.run_complete = True
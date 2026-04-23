from django.apps import AppConfig

class IbascoLeagueAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ibasco_league_app'

    def ready(self):
        import ibasco_league_app.models
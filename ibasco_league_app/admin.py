from django.contrib import admin
from .models import Team, Fixture

admin.site.register(Team)
admin.site.register(Fixture)
from .models import TopScorer
admin.site.register(TopScorer)
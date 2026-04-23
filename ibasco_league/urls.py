from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ibasco_league_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('teams/', views.teams),
    path('fixtures/', views.fixtures),
    path('table/', views.table),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
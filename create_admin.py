import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ibasco_league.settings')
django.setup()

from django.contrib.auth.models import User

username = "admin"
password = "admin12345"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password)
    print("Admin created")
else:
    print("Admin already exists")
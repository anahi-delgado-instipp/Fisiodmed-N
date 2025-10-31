# create_superuser.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fisiodmed_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "ANAHID")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "notmxly@gmail.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "7070")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"✅ Superusuario '{username}' creado correctamente.")
else:
    print(f"⚠️ El superusuario '{username}' ya existe.")

print("Usuarios existentes:", list(User.objects.values_list("username", flat=True)))

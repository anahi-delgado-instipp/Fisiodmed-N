# create_superuser.py
from django.contrib.auth import get_user_model
import os

User = get_user_model()

# Obtener credenciales desde variables de entorno (Render → Environment)
username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "ANAHID")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "notmxly@gmail.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "7070")

# Crear el superusuario solo si no existe
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"✅ Superusuario '{username}' creado correctamente.")
else:
    print(f"⚠️ El superusuario '{username}' ya existe, no se creó uno nuevo.")

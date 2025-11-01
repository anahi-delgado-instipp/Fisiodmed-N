import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables del archivo .env (opcional pero recomendable)
load_dotenv()

# BASE_DIR (directorio raíz del proyecto)
BASE_DIR = Path(__file__).resolve().parent.parent

# ===========================
# 🔐 SEGURIDAD
# ===========================

SECRET_KEY = os.getenv('SECRET_KEY', 'clave-secreta-para-render')  # cambia esto en producción

DEBUG = False  # Render ya maneja su propio modo de despliegue

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']

# ===========================
# 🧩 APLICACIONES INSTALADAS
# ===========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Tus apps
    'fisiodmed_project',  # ejemplo, cambia por tus apps
]

# ===========================
# ⚙️ MIDDLEWARE
# ===========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <- para servir archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fisiodmed_project.urls'

# ===========================
# 🎨 TEMPLATES
# ===========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # si usas carpeta templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fisiodmed_project.wsgi.application'

# ===========================
# 💾 BASE DE DATOS (SQLite)
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ===========================
# 🔑 AUTENTICACIÓN
# ===========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ===========================
# 🌎 LOCALIZACIÓN
# ===========================
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_TZ = True

# ===========================
# 🧾 ARCHIVOS ESTÁTICOS
# ===========================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# ===========================
# 📤 ARCHIVOS MEDIA (si los usas)
# ===========================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ===========================
# 🚀 CONFIGURACIÓN FINAL
# ===========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

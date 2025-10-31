from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-h&gf+p-tm5ziy$emk2h9z@r)=@pnmo5h^fpq!ziww$r8=a8e*$'
#SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-h&gf+p-tm5ziy$emk2h9z@r)=@pnmo5h^fpq!ziww$r8=a8e*$')
SECRET_KEY = os.environ.get('SECRET_KEY', default='fhgfjjjhvjhggfvjyt6789y54t6y54t6y54t6y54t6y54t6y54t6y54t6y54t6')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

#DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS =  ['fisiodmed-n.onrender.com', 'localhost', '127.0.0.1']
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.pacientes',
    'apps.pagos',
    'apps.servicios',
    'apps.usuarios',
    'apps.citas',
    'apps.inicio',
    'apps.dashboard',
    'apps.reportes',
    'apps.autenticacion',
    'apps.especialidades',
    'apps.medicos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fisiodmed_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



WSGI_APPLICATION = 'fisiodmed_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.postgresql_psycopg2',
   #     'NAME': 'BD-Fisiodmed',
    #    'USER': 'postgres',
     #   'PASSWORD': '1234',
      #  'HOST': 'localhost',
       # 'PORT': '5432',
        #'ATOMIC_REQUESTS': True,
    #}
#}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://fisiodmed_y8ci_user:fMug1ZCx9HiPHqXswJf9QJ2jKFxpYVC8@dpg-d424qjjipnbc73c1qp60-a/fisiodmed_y8ci')
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
}



# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/


# Archivos estáticos (CSS, JS, imágenes)
STATIC_URL = '/static/'
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Archivos multimedia (si usas imágenes subidas por usuarios)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = 'index'

#AUTHENTICATION_BACKENDS = [
 #   'apps.autenticacion.backends.MultiFieldAuthBackend',
  #  'django.contrib.auth.backends.ModelBackend',
#]

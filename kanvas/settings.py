from pathlib import Path
from  corsheaders.defaults  import  default_methods 
from  corsheaders.defaults  import  default_headers 
import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-i(siw_d_v*!0c8oe8v%mbu63-#j-av7ysm6jmvh@zo@58r7sjt'
DEBUG = True

ALLOWED_HOSTS = ['dgeneretord.herokuapp.com', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'materias',
    'turmas',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

# CORS_ALLOWED_ORIGINS  =  [ 
#     "https://dgeneretord.herokuapp.com/", 
#     "http://localhost:3000/" 
# ]

# CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOW_METHODS  =  [ 
#     "DELETE", 
#     "GET", 
#     "OPÇÕES", 
#     "PATCH", 
#     "POST", 
#     "PUT" 
# ]

# CORS_ALLOW_HEADERS = [
#     "accept",
#     "accept-encoding",
#     "authorization",
#     "content-type",
#     "dnt",
#     "origin",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",
# ]

# CORS_ALLOW_METHODS  =  list ( default_methods )  +  [ 
#     "POKE" , 
# ]

# CORS_ALLOWED_ORIGINS  =  [ 
#     "https://dgeneretord.herokuapp.com/", 
#     "http://localhost:8000/", 
#     "http://localhost:3000/"  
# ] 

# CSRF_TRUSTED_ORIGINS  =  [ 
#     "https://dgeneretord.herokuapp.com", 
#     "http://localhost:8000", 
#     "http://localhost:3000"  
# ]

# MIDDLEWARE_CLASSES = [
#     ...,
#     "corsheaders.middleware.CorsMiddleware",
#     ...,
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "corsheaders.middleware.CorsPostCsrfMiddleware",
#     ...,
# ]

# CORS_ALLOW_HEADERS  =  list ( default_headers )  +  [ 
#     "my-custom-header" , 
# ]

# CORS_REPLACE_HTTPS_REFERER: True

ROOT_URLCONF = 'kanvas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'kanvas.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    db_from_env = dj_database_url.config(
        default=DATABASE_URL, conn_max_age=500, ssl_require=True)
    DATABASES['default'].update(db_from_env)
    DEBUG = False

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
from config.env import BASE_DIR
from config.settings.common import *

if env.DATABASE_URI:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            **env.env.db_url_config(env.DATABASE_URI),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env.DB_NAME,
            "USER": env.DB_USER,
            "PASSWORD": env.DB_PASSWORD,
            "HOST": env.DB_HOST,
            "PORT": env.DB_PORT,
        }
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(env.BASE_DIR, "static")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(env.BASE_DIR, "media")

COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

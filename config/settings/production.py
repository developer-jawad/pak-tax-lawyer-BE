from corsheaders.defaults import default_headers

from config.settings.common import *

# Database — tuned for Supabase Nano (0.5 GB RAM, shared CPU, ~25 connection limit).
# Vercel is serverless: CONN_MAX_AGE=0 so each invocation releases its connection
# immediately after the response, preventing connection exhaustion on Nano.
_DB_CONN_OPTIONS = {
    "CONN_MAX_AGE": 0,
    "OPTIONS": {
        "connect_timeout": 5,
        "options": "-c statement_timeout=10000",  # 10 s hard limit — protect shared CPU
    },
}

if env.DATABASE_URI:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            **env.env.db_url_config(env.DATABASE_URI),
            **_DB_CONN_OPTIONS,
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
            **_DB_CONN_OPTIONS,
        }
    }

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(env.BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(env.BASE_DIR, "media")

COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT

# CORS configuration
CORS_ALLOWED_ORIGINS = (
    env.CORS_ALLOWED_ORIGINS if hasattr(env, "CORS_ALLOWED_ORIGINS") else []
)
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = list(default_headers) + [
    "authorization",
    "content-type",
    "x-csrftoken",
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CSRF_TRUSTED_ORIGINS = (
    env.CSRF_TRUSTED_ORIGINS if hasattr(env, "CSRF_TRUSTED_ORIGINS") else []
)

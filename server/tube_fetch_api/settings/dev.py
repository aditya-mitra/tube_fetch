from .base import BASE_DIR

DEBUG = True

SECRET_KEY = "django-insecure-z)kvwnsv*ucvbxfagorz_!y2%22s7^^46oovu-fg3$r97ma)om"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

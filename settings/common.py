import os.path, sys, os

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # project root : 파일로 부터 두번 dirname.

APPEND_SLASH = False
ALLOWED_HOSTS = ["*"]

ADMIN = ("Admin", "example@example.com")

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "taiga",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake"
    }
}

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]

# Default configuration for reverse proxy
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

# Errors report configuration
SEND_BROKEN_LINK_EMAILS = True
IGNORABLE_404_ENDS = (".php", ".cgi")
IGNORABLE_404_STARTS = ("/phpmyadmin/",)

ATOMIC_REQUESTS = True
TIME_ZONE = "UTC"

if __name__ == "__main__":
    print('__file__ : ' + __file__)
    print('BASE_DIR : ' + BASE_DIR)

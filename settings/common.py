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

if __name__ == "__main__":
    print('__file__ : ' + __file__)
    print('BASE_DIR : ' + BASE_DIR)

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

try:
    from settings import celery_local as celery_settings
except ImportError:
    from settings import celery as celery_settings

app = Celery('tiger')
app.config_from_object(celery_settings)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

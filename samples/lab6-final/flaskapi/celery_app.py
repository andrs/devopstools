import os
from celery import Celery

def make_celery(flask_app):
    broker_url = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@rabbit:5672//")
    backend_url = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
    celery = Celery(flask_app.import_name, broker=broker_url, backend=backend_url)
    celery.conf.update(flask_app.config)
    return celery
import os
from celery import Celery

def make_celery(flask_app):
    broker_url = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@rabbit:5672//")
    backend_url = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
    celery = Celery(flask_app.import_name, broker=broker_url, backend=backend_url)
    celery.conf.update(flask_app.config)
    return celery
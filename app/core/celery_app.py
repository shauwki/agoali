import os
from celery import Celery

broker_url = os.environ.get("CELERY_BROKER_URL")
result_backend = os.environ.get("CELERY_RESULT_BACKEND")

app = Celery(
    'mod_assistant_tasks',
    broker=broker_url,
    backend=result_backend,
    include=['tasks']  
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Amsterdam',
    enable_utc=True,
)

if __name__ == '__main__':
    app.start()
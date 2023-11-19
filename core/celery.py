from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Create a Celery instance and configure it using the settings from Django.
app = Celery('core')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc = False
app.conf.update(timezone = 'Aisa/Kolkata')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()
# app.conf.broker_url = 'redis://localhost:6379/0'

# # Use the Django database as the result backend.
# app.conf.result_backend = 'db+django://'  # or 'db+django://'

# # Other Celery settings...
# app.conf.accept_content = ['application/json']
# app.conf.task_serializer = 'json'
# app.conf.result_serializer = 'json'
# app.conf.timezone = 'Asia/Kolkata'

# # Auto-discover tasks in all installed apps.
# app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'request: f{self.request!r}')
from datetime import timedelta
from celery import Celery


app = Celery('tasks')
app.conf.update(
    BROKER_URL='redis://localhost',
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERYBEAT_SCHEDULE={
        'say_hello': {
            'task': 'tasks.say_hello',
            'schedule': timedelta(seconds=5)
        }
    }
)


@app.task(name='tasks.say_hello')
def say_hello():
    print("Hello, World!")

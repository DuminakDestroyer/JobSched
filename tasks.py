import requests
import textwrap

from datetime import timedelta
from celery import Celery


app = Celery('trial_task')
app.conf.update(
    BROKER_URL='redis://localhost',
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERYBEAT_SCHEDULE={
        'say_hello': {
            'task': 'trial_task.say_hello',
            'schedule': timedelta(seconds=5)
        }
    }
)


@app.task(name='trial_task.say_hello')
def say_hello():
    print("Hello, World!")
    api_call()


# Sample API Call function and response
def api_call():
    url = 'http://ES_search_demo.com/document/record/_search?pretty=true'
    data = textwrap.dedent("""\
                {"query":{"bool":{"must":[{"text":{"record.document":
                "SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"
                }}],"must_not":[],"should":[]}},"from":0,"size":50,
                "sort":[],"facets":{}}'
           """)
    response = requests.get(url, data=data)
    return response.json()

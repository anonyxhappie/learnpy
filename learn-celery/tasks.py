from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://akshay:123456@localhost/myvhost')

@app.task
def add(x, y):
    return x + y

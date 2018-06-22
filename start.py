from celery import Celery
app = Celery("mytasks",broker="redis://redis:6379")
@app.task
def add(x, y): return x + y
if __name__ == '__main__':
    app.worker_main()
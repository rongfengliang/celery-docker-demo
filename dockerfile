FROM celery
WORKDIR /app
RUN pip install redis
COPY start.py /app/
ENTRYPOINT [ "celery","-A","start","worker","--loglevel=info"]
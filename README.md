# celery docker && docker-compose running

> Note rabbitmq is not required

## How to Run

* build image

```code
docker-compose  build
```

* run

```code
docker-compose up -d
```

* call result

> because this is async call it will return the task id

```code
docker-compose logs -f worker
docker-compose logs client
``
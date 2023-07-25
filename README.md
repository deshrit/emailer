## emailer

django, celery, redis and celery-flower for asynchronous task queue - sending emails.

![image](https://github.com/deshrit/emailer/assets/59757711/2ad4615b-8ba0-44b9-bf66-cd61800b60e5)


## To run locally

**1. Create `src/.env` file**

```bash
EMAIL_HOST_USER='your_user'
EMAIL_HOST_PASSWORD='your_password'
```

**2. Must have docker and docker compose**

Clone this repository and run

```
docker compose up
```

**3. Application access**

1. emailer

```
http://localhost:8008
```

2. celery flower

```
http://localhost:7007
```

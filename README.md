# emailer
django and celery and redis and flower asynchronous task queue - sending emails.

![image](https://github.com/deshrit/emailer/assets/59757711/2ad4615b-8ba0-44b9-bf66-cd61800b60e5)


# To run locally
### 1. Create `src/.env` file
```bash
EMAIL_HOST_USER='your_user'
EMAIL_HOST_PASSWORD='your_password'
```
### 2. Must have docker and docker compose
```
docker compose up
```

### 3. Application access
#### i. emailer
```
http://localhost:8008
```
#### ii. celery flower
```
http://localhost:7007
```

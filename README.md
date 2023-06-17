# emailer
django and celery and redis and flower asynchronous task queue - sending emails.

![image](https://github.com/deshrit/emailer/assets/59757711/6b001f31-7b1c-47bc-b87a-730af58fc3d8)

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

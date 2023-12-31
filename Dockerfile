FROM python:3.10-alpine

LABEL maintainer="deshritbaral.com.np"

ENV PYTHONUNBUFFERED 1

WORKDIR /emailer

RUN pip install --no-cache-dir --upgrade \ 
    pip \
    pipenv \
    "celery[redis]" \
    flower

RUN addgroup -S emailer && \
    adduser --disabled-password -H  -S emailer -G emailer

COPY ./Pipfile* ./

RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

USER emailer

WORKDIR /emailer/src

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8008" ]
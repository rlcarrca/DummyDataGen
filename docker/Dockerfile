FROM python:3.8.1-alpine

RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt \
&& rm -rf /etc/apk/cache \
&& rm -rf /var/cache/yum \
&& rm -rf /var/cache/apt \
&& rm -rf /requirements.txt /requirements-test.txt 

WORKDIR /app

#COPY datagen /app 

CMD ["/bin/ash"]

FROM alpine:3.7
MAINTAINER Cleon Mullings "smithcleon@gmail.com"
RUN apk add python3 build-base python3-dev py-virtualenv mariadb-dev --no-cache
RUN pip3 install --no-cache-dir --upgrade pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "run.py"]
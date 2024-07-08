# pull the official docker image
FROM python:3.10

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set display port to avoid crash
ENV DISPLAY=:99

RUN apt-get -y update; \
    apt-get -y upgrade; \
    apt-get -y install apt-utils \
    nano  \
    htop;

# copy project
COPY . .

# install dependencies
RUN pip install -U pip

RUN pip install -r requirements.txt 


CMD [ "python", "main.py" ]
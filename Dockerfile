FROM python:3.9

USER root
RUN apt-get update -y && apt-get upgrade -y


ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt /app/
ADD ./runserver.sh /app/
RUN pip3 install -r /app/requirements.txt
ADD . /app/

ENV DJANGO_DB_NAME=default
ENV DJANGO_SU_NAME=admin
ENV DJANGO_SU_PASSWORD=admin

CMD ["/app/runserver.sh"]


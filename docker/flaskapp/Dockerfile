FROM alpine:3.7
LABEL maintainer="Gerold Penz - <gerold@halvar.at>"

# Spracheinstellung
ENV LANG de_AT.UTF-8

# Programme installieren
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN apk add --no-cache py3-flask
RUN apk add --no-cache py3-redis
RUN apk add --no-cache uwsgi
RUN apk add --no-cache uwsgi-python3

## Python3 Abhängigkeiten installieren
#COPY /docker/flaskapp/requirements.txt /requirements.txt
#RUN pip3 install --upgrade pip
#RUN pip3 install --requirement /requirements.txt

# Programmdateien kopieren
ADD /application /application
ADD /docker/flaskapp/startup.sh /startup.sh

CMD ["/bin/sh", "/startup.sh"]

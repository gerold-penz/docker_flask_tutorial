FROM nginx:1.13-alpine

LABEL maintainer="Gerold Penz - <gerold@halvar.at>"

ADD /docker/nginx/nginx.conf /etc/nginx/nginx.template
ADD /docker/nginx/startup.sh /startup.sh

ADD /application /usr/share/nginx/html

CMD ["/bin/sh", "/startup.sh"]

#!/bin/sh

cp /etc/nginx/nginx.template /etc/nginx/nginx.conf

if [ "${PRODUCTION}" == "true" ]; then
    echo "Nginx in PRODUCTION-Mode"
    sed -i "s/__production__/1/g" /etc/nginx/nginx.conf
else
    echo "Nginx in DEVELOPMENT-Mode"
    sed -i "s/__production__/0/g" /etc/nginx/nginx.conf
fi
nginx -g 'daemon off;'

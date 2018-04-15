#!/bin/sh

# Um die Performance der Flask-Anwendung zu erhöhen, können mehrere
# Prozesse und Threads gestartet werden.
# --processes 4 --threads 2
#
# Mit `--py-autoreload 2` wird alle 2 sec. auf Änderungen im Quellcode geprüft.

if [ "${PRODUCTION}" == "true" ]; then
    echo "Flask-Application in PRODUCTION-Mode"
    /usr/sbin/uwsgi \
        --socket :3031 \
        --plugin /usr/lib/uwsgi/python3_plugin.so \
        --uid uwsgi \
        --gid uwsgi \
        --master \
        --enable-threads \
        --callable app \
        --wsgi-file /application/my_flask_app.py
else
    echo "Flask-Application in DEVELOPMENT-Mode"
    /usr/bin/python3 /application/my_flask_app.py
fi

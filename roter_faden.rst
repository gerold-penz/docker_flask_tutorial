########################################################
Entwicklung und produktiver Einsatz von Flask und Docker
########################################################

Gerold Penz 2018 <gerold@halvar.at>


- Begriffe klären

    - Host
    - Docker-Container
    - Docker-Image
    - Docker-Volume
    - Dockerfile
    - Docker-Compose
    - Docker-Hub

- Mit `docker pull` ein aktuelles "alpine:3.7" Image holen

- Den Docker-Hub erklären

- Mit `docker run -it --rm ...` das Alpine-Linux starten und zeigen wie man
  etwas installiert.

- Docker-Container wurde gelöscht --> zeige dass das installierte
  Programm wieder weg ist.

- Einfaches Flask-Beispiel erstellen und ausprobieren

- Einfaches Dockerfile für Flaskapp erstellen

    - Mit RUN Python 3 und Flask installieren

    - Mit `docker build --tag gerold/tutorial_demo .` ein Docker-Image erstellen

    - Mit `docker run -it --rm gerold/tutorial_demo` den Container starten
      und zeigen dass Python installiert ist.

- Einfaches Docker-Compose-File erstellen

- Mit `docker-compose build --no-cache` den Container erstellen

- Mit `docker-compose up` den Container starten

- Mit `docker-compose exec flaskapp /bin/sh` in den Container einsteigen und
  untersuchen

- Docker-Compose-Datei um den *redis:4-alpine*-Part erweitern
  Kein eigenes Image. `volumes` setzen, damit die Daten erhalten bleiben.

- Redis in die Flaskapp einbauen.

- Dockerfile für Redis erstellen.

- Docker-Compose-Datei so anpassen, dass diese ein eigenes Redis-Image erstellt.
  Ausprobieren: `build --no-cache`




























    ├── application
    │   └── my_flask_app.py
    ├── deploy
    │   └── hetzner_testserver
    │       ├── docker_flask_tutorial_dev
    │       │   ├── docker-compose.yaml
    │       │   └── _docker_save_images.py
    │       └── docker_flask_tutorial_prod
    │           ├── docker-compose.yaml
    │           └── docker_tag_images.py
    ├── docker
    │   ├── flaskapp
    │   │   ├── Dockerfile
    │   │   ├── requirements.txt
    │   │   └── startup.sh
    │   ├── nginx
    │   │   ├── Dockerfile
    │   │   ├── nginx.conf
    │   │   └── startup.sh
    │   └── redis
    │       └── Dockerfile
    ├── docker-compose
    │   ├── dev
    │   │   └── docker-compose.yaml
    │   └── prod
    │       └── docker-compose.yaml
    ├── README.rst
    └── roter_faden.rst


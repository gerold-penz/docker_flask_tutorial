########################################################
Entwicklung und produktiver Einsatz von Flask und Docker
########################################################

Gerold Penz 2018 <gerold@halvar.at>


=========
Quellcode
=========

https://github.com/gerold-penz/docker_flask_tutorial


===================
Begriffserklärungen
===================


----
Host
----

Computer auf dem der Docker-Deamon (Dienst) läuft. Dieser Computer startet die einzelnen
Docker-Container.


----------------
Docker-Container
----------------

In einem Docker-Container läuft unser Programm. Dieser Container enthält alle
Abhängigkeiten die das Programm zum Laufen benötigt.

Das Dateisystem eines Docker-Containers wird von einem Docker-Image geladen.


------------
Docker-Image
------------

Dateisystem-Abbild eines Docker-Containers zu einem bestimmten Zeitpunkt (sehr einfach gesagt).

In einer einfachen Textdatei (Dockerimage-Datei) kann beschrieben werden wie ein
Docker-Image aufgebaut werden soll.

In einer Dockerimage-Datei wird festgelegt auf welchem anderen Image unser Docker-Image
aufbaut, welche Dateien (z.B. Quellcode) hineinkopiert werden solle und welche Befehle
(z.B. `apt get install python3`) beim Erstellen des Images ausgeführt werden sollen.


-------------
Docker-Volume
-------------

Im einfachsten Fall wird ein Ordner des Host-Dateisystems in den Container gemappt.
Änderungen in diesem Ordner bleiben erhalten, auch wenn man den Docker-Container löscht.


----------
Dockerfile
----------

Eine Textdatei in der beschrieben wird, wie ein Docker-Image aufgebaut ist.

- Gibt an, auf welches vorhandene Docker-Image unser neues Docker-Image aufbaut (FROM).
- Gibt an, welche Dateien in das neue Docker-Image kopiert werden sollen (ADD).
- Gibt an, welche Programme das Docker-Image ändern sollen (RUN):
    - Programminstallationen
    - Ändern von Konfigurationdateien
- Gibt an, welches Programm beim Start des Containers ausgeführt werden soll (CMD).


--------------
Docker-Compose
--------------

Damit werden mehrere Docker-Container zu einem Programmpaket geschnürt.

- Webserver in einem eigenen Container
- Datenbank in einem eigenen Container
- Python-Programm in einem eigenen Container

- Mehrere Container bilden ein Programmpaket
- Container werden in der richtigen Reihenfolge gestartet
- Container sind in einem eigenen IP-Adressbereich miteinander verbunden

Compose file version 3 reference: https://docs.docker.com/compose/compose-file/


----------
Docker-Hub
----------

Öffentliches Repositry mit frei verfügbaren Docker-Images

https://hub.docker.com/

- Alpine-Linux
- Debian
- Ubuntu
- Redis
- PostgreSql
- Nginx
- ...


====================================================
Änderungen im Dateisystem eines laufenden Containers
====================================================

Ein Docker-Image baut auf anderen Docker-Images auf (Schichten).
Die Images auf denen ein Docker-Image aufbaut sind schreibgeschützt.
Nur die letzte oberste Schicht kann sich ändern.

Ändert der laufende Docker-Container Dateien im Dateisystem, ändert sich
die oberste Schicht des Docker-Images die mit dem Docker-Container verbunden ist.

Löscht man den Container, werden auch diese Änderungen gelöscht.


=============================
Das Bauen eines Docker-Images
=============================







==========
Referenzen
==========

---------------------------------------------
About images, containers, and storage drivers
---------------------------------------------

https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/


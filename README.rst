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

------------
Docker-Image
------------

Dateisystem-Abbild eines Docker-Containers zu einem bestimmten Zeitpunkt (sehr einfach gesagt).

Ein Docker-Image baut auf anderen Docker-Images auf (Schichten).
Diese Images auf denen ein Docker-Image aufbaut sind schreibgeschützt.
Nur die letzte oberste Schicht kann sich ändern.

Ein Ubuntu-Image kann so eine Schicht sein, auf der unser eigenes Image aufbaut.

Docker-Images können gebaut werden. In einer einfachen Textdatei (Dockerimage-Datei)
kann beschrieben werden wie ein Docker-Image aufgebaut werden soll.


----------------
Docker-Container
----------------

Container-Laufzeitumgebung die mit einem Docker-Image gestartet wird.

Änderungen im Dateisystem ändern die oberste Schicht des Docker-Images auf dem der
Container aufbaut. Löscht man den Container, wird auch diese Änderung im Docker-Image
gelöscht.


-------------
Docker-Volume
-------------

Im einfachsten Fall wird ein Ordner des Host-Dateisystems in den Container gemappt.
Änderungen in diesem Ordner bleiben erhalten, auch wenn man den Docker-Container löscht.


----------
Dockerfile
----------



--------------
Docker-Compose
--------------


-----
Flask
-----


----
WSGI
----


-----
uWsgi
-----


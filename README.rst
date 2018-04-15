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

Ein Docker-Container ist ein Container in dem unser Programm läuft. Dieser Container
enthält alle Abhängigkeiten die das Programm zum Laufen benötigt.

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



--------------
Docker-Compose
--------------


====================================================
Änderungen im Dateisystem eines laufenden Containers
====================================================

Änderungen im Dateisystem ändern eine neue oberste Schicht des Docker-Images (die mit dem
Docker-Container verbunden ist) auf dem der Container aufbaut.

Löscht man den Container, werden auch diese Änderungen gelöscht.


=============================
Das Bauen eines Docker-Images
=============================


Ein Docker-Image baut auf anderen Docker-Images auf (Schichten).
Diese Images auf denen ein Docker-Image aufbaut sind schreibgeschützt.
Nur die letzte oberste Schicht kann sich ändern.

Ein Ubuntu-Image kann so eine Schicht sein, auf der unser eigenes Image aufbaut.


==========
Referenzen
==========

---------------------------------------------
About images, containers, and storage drivers
---------------------------------------------

https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/


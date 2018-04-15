#!/usr/bin/env python3
# coding: utf-8
"""
Speichert alle benötigten Produktiv-Images in ein komprimiertes *tar.bz2*-Archiv.
"""


from __future__ import print_function
from six.moves import input

import os
import subprocess

THISDIR = os.path.dirname(os.path.abspath(__file__))
IMAGESDIR = os.path.abspath(os.path.join(THISDIR, "..", "..", "..", "_local_images"))


def main():
    
    # Zielpfad erstellen
    if not os.path.isdir(IMAGESDIR):
        os.makedirs(IMAGESDIR)
    
    # DEV-Versionen speichern
    print("Docker-Images DEV speichern...")
    try:
        returncode = subprocess.call(
            [
                "docker",
                "save",
                "--output", os.path.join(IMAGESDIR, "docker_flask_tutorial_dev.tar"),
                "gerold/tutorial_redis:dev",
                "gerold/tutorial_flaskapp:dev",
                "gerold/tutorial_nginx:dev",
            ],
            cwd = THISDIR
        )
        if returncode != 0:
            input("Press ENTER to continue...")
    except KeyboardInterrupt:
        pass

    # DEV-Version Komprimieren
    print("Docker-Images DEV komprimieren...")
    try:
        returncode = subprocess.call(
            [
                "bzip2",
                "--force",
                os.path.join(IMAGESDIR, "docker_flask_tutorial_dev.tar")
            ],
            cwd = IMAGESDIR
        )
        if returncode != 0:
            input("Press ENTER to continue...")
    except KeyboardInterrupt:
        pass
    
    # Fertig
    print("Fertig!")
    print()


if __name__ == "__main__":
    main()


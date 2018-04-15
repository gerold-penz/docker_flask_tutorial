#!/usr/bin/env python3
# coding: utf-8
"""
Erstellt aus den aktuellen DEV-Images die PROD-Images
"""


from __future__ import print_function
from six.moves import input

import os
import subprocess

THISDIR = os.path.dirname(os.path.abspath(__file__))


def main():
    
    # PROD-Versionen taggen
    print("Docker-Images PROD taggen...")
    try:
        for image in [
            "gerold/tutorial_redis",
            "gerold/tutorial_flaskapp",
            "gerold/tutorial_nginx",
        ]:
            returncode = subprocess.call(
                [
                    "docker",
                    "image",
                    "tag",
                    "{}:dev".format(image),
                    "{}:prod".format(image)
                ],
                cwd = THISDIR
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


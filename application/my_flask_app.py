#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import flask
import redis

THISDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, THISDIR)  # für uWSGI

app = flask.Flask(__name__)
rdb = redis.StrictRedis(host = 'redis')


@app.route("/")
def index():
    my_counter = rdb.incr("my_counter")
    
    if os.environ.get("PRODUCTION") == "true":
        retval = "Production: {}".format(my_counter)
    else:
        retval = "Development: {}".format(my_counter)

    return retval


def main():
    app.run(host = "0.0.0.0", port = 8080, debug = True)


if __name__ == "__main__":
    main()

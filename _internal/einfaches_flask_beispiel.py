#!/usr/bin/env python3
# coding: utf-8

import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "OK"


def main():
    app.run(host = "0.0.0.0", port = 8080, debug = True)


if __name__ == "__main__":
    main()

#!/bin/env python3

import flask
import pyjokes

app = flask.Flask(__name__)


@app.route("/")
def home():
    return flask.render_template("home.html", joke=pyjokes.get_joke(category="chuck"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

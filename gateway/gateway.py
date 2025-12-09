"""
Docstring for sample-flask-app.app
"""

from random import randint
import sys
from time import sleep
from logging.config import dictConfig
from flask import Flask

app = Flask(__name__)


dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            },
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["wsgi"],
        },
    }
)


@app.route("/")
def hello_world():
    app.logger.info("Hello, World! endpoint was reached")
    return "Successful response\n", 200


@app.route("/server_error")
def server_error():
    app.logger.info("Server Error endpoint was reached")
    return "Server error\n", 500


@app.route("/client_error")
def client_error():
    app.logger.info("Client Error endpoint was reached")
    return "Client error\n", 400


@app.route("/latency")
def latency():
    rn = randint(1, 100)
    # 90 percententile latency of 2 seconds
    if rn > 90 and rn <= 99:
        sleep(2)
    # 99 percententile latency of 5 seconds
    elif rn > 99:
        sleep(5)
    return f"Latency endpoint {rn}\n", 200


@app.route("/blowup")
def blowup():
    rn = randint(1, 10)
    app.logger.info("blowup endpoint was reached")
    # 30% chance to crash
    if rn > 7:
        app.logger.info("crashing...")
        sys.exit(1)
    return "Survived blowup\n", 200


if __name__ == "__main__":
    app.run(debug=True)

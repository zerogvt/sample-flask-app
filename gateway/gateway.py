"""
A sample flask web app that simulates various response codes and latencies.
"""

from random import randint
import sys
from time import sleep
from logging.config import dictConfig
from flask import Flask

wapp = Flask(__name__)


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


@wapp.route("/")
def hello_world():
    wapp.logger.info("Hello, World! endpoint was reached")
    return "Successful response\n", 200


@wapp.route("/server_error")
def server_error():
    wapp.logger.info("Server Error endpoint was reached")
    return "Server error\n", 500


@wapp.route("/client_error")
def client_error():
    wapp.logger.info("Client Error endpoint was reached")
    return "Client error\n", 400


@wapp.route("/latency")
def latency():
    rn = randint(1, 100)
    # 90 percententile latency of 2 seconds
    if rn > 90 and rn <= 99:
        sleep(2)
    # 99 percententile latency of 5 seconds
    elif rn > 99:
        sleep(5)
    return f"Latency endpoint {rn}\n", 200


@wapp.route("/blowup")
def blowup():
    rn = randint(1, 10)
    wapp.logger.info("blowup endpoint was reached")
    # 30% chance to crash
    if rn > 7:
        wapp.logger.info("crashing...")
        sys.exit(1)
    return "Survived blowup\n", 200


if __name__ == "__main__":
    wapp.run(debug=True)

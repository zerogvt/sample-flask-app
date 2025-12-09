"""
Sample backend Flask application
"""
from logging.config import dictConfig
from flask import Flask, jsonify, request

bapp = Flask(__name__)


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


@bapp.route("/", methods=["POST"])
def home():
    '''
    Docstring for home
    '''
    if request.method != "POST":
        return jsonify({"error": "Invalid request method"}), 405
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    data = request.get_json()
    return jsonify({"you_sent": data}), 201


if __name__ == "__main__":
    bapp.run(debug=True)

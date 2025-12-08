from flask import Flask
from random import randrange
from time import sleep
app = Flask(__name__)

from logging.config import dictConfig

dictConfig({
'version': 1,
'formatters': {
'default': {
'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
},
},
'handlers': {
'wsgi': {
'class': 'logging.StreamHandler',
'stream': 'ext://flask.logging.wsgi_errors_stream',
'formatter': 'default',
},
},
'root': {
'level': 'INFO',
'handlers': ['wsgi'],
},
})


@app.route("/")
def hello_world():
   #print("Hello, World! endpoint was reached")
   app.logger.info("Hello, World! endpoint was reached")
   return "Hello, World!"


@app.route("/server_error")
def server_error():
   app.logger.info("Server Error endpoint was reached")
   return "server error", 500 


@app.route("/client_error")
def client_error():
   app.logger.info("Client Error endpoint was reached")
   return "client error", 400 

@app.route("/latency")
def latency():
   sleep_time = randrange(1,10)
   app.logger.info("latency endpoint was reached")
   sleep(sleep_time)
   return "client error", 400 

if __name__ == "__main__":
   app.run(debug=True)


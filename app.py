from flask import Flask
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
   return "<h1>Hello, World!</h1>"
if __name__ == "__main__":
   app.run(debug=True)


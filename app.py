import os
from flask import Flask 



app = Flask(__name__)


from routes import *
#lancement du microservice flask

if __name__ == '__main__':
    app.run()

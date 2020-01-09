from config import Config
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
mongo = PyMongo(app)
bootstrap = Bootstrap(app)


from analysis import controller
from analysis import nsepy_fix

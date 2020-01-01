from config import Config
from flask import Flask
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)
bootstrap = Bootstrap(app)


from analysis import controller

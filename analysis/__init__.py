from config import Config
from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)


from analysis import controller

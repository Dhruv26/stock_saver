import json
from flask import render_template, request
from . import app
from .forms import AddEntryForm
from .model import MongoDb


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('add_entry.html', form=AddEntryForm())


@app.route('/addEntry', methods=['POST'])
def add_entry():
    indicators = dict()
    ob = AddEntryForm()
    return 'Preparing to save...'

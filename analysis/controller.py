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
    ob = AddEntryForm()
    data = {
        "stock_name": ob.data["stock_name"],
        "indicators": [{k: v for k, v in d.items() if k != 'csrf_token'} for d in ob.data['indicators']]
    }
    MongoDb().insert(data)
    return 'Preparing to save...'


@app.route('/update', methods=['POST'])
def update():
    ob = AddEntryForm()
    data = {
        "stock_name": ob.data["stock_name"],
        "indicators": [{k: v for k, v in d.items() if k != 'csrf_token'} for d in ob.data['indicators']]
    }
    MongoDb().update(data)
    return 'Preparing to save...'


@app.route('/delete', methods=['DELETE'])
def delete(ob_id):
    MongoDb().delete(ob_id)
    return 'Preparing to save...'

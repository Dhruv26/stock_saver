from flask import render_template, request
from app import app
from app.forms import AddEntryForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('add_entry.html', form=AddEntryForm())


@app.route('/addEntry', methods=['POST'])
def add_entry():
    import json
    print(json.dumps(request.form, indent=2))
    import pdb; pdb.set_trace()
    return 'Preparing to save...'

from flask import render_template, flash, redirect, url_for
from collections import defaultdict
from . import app
from .forms import AddEntryForm
from .model import MongoDb
from .table import HomePageTable, MoreInfoTable
from .indicators import INDICATORS


@app.route('/')
@app.route('/index')
def index():
    raw_items = MongoDb().get_all()
    table_items = []
    for entry in raw_items:
        res = defaultdict(str)
        for indicator in entry['indicators']:
            res[indicator['name']] += "|" + indicator['value'] + "|"
        res['stock_name'] = entry['stock_name']
        res['_id'] = str(entry['_id'])
        res.update({n: '' for n in INDICATORS if n not in res})
        table_items.append(res)

    table = HomePageTable(items=table_items,
                          no_items='No entries created yet.',
                          classes=['hometable'],
                          border=True)
    return render_template('index.html', table=table)


@app.route('/more_info/<id>', methods=['GET', 'POST'])
def get_more_info(id):
    data = MongoDb().get_by_id(id)
    import pdb;pdb.set_trace()
    table_items = []
    for n in data['indicators']:
        res = {'indicator': n['name'].upper(), 'type': n['type'], 'value': n['value']}
        table_items.append(res)
    table = MoreInfoTable(items=table_items,
                          classes=['hometable'],
                          border=True)
    return render_template('index.html', table=table)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddEntryForm()
    if form.validate_on_submit():
        flash('Creating...')
        data = {
            "stock_name": form.data["stock_name"],
            "indicators": [{k: v for k, v in d.items() if k != 'csrf_token'} for d in form.data['indicators']]
        }
        MongoDb().insert(data)
        return redirect(url_for('index'))

    return render_template('add_entry.html', title='Add new entry', form=form)


@app.route('/update', methods=['POST'])
def update():
    ob = AddEntryForm()

    data = {
        "stock_name": ob.data["stock_name"],
        "indicators": [{k: v for k, v in d.items() if k != 'csrf_token'} for d in ob.data['indicators']]
    }
    MongoDb().update(data)

    return redirect(url_for('index'))


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    MongoDb().delete(id)
    return redirect(url_for('index'))

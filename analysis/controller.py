from flask import render_template, flash, redirect, url_for
from collections import defaultdict
from . import app
from .forms import AddEntryForm
from .model import MongoDb
from .table import HomePageTable
from .indicators import INDICATORS


@app.route('/')
@app.route('/index')
def index():
    raw_items = MongoDb().get_all()

    table_items = []
    for entry in raw_items:
        res = defaultdict(list)
        for indicator in entry['indicators']:
            res[INDICATORS[indicator['name']]].append(indicator['value'])
        res['stock_name'] = entry['stock_name']
        res.update({n: [] for n in INDICATORS.values() if n not in res})
        table_items.append(res)

    import pdb; pdb.set_trace()
    table = HomePageTable(items=table_items,
                          no_items='No entries created yet.',
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
        return redirect('/index')

    return render_template('add_entry.html', form=form)


@app.route('/update', methods=['POST'])
def update():
    ob = AddEntryForm()
    data = {
        "stock_name": ob.data["stock_name"],
        "indicators": [{k: v for k, v in d.items() if k != 'csrf_token'} for d in ob.data['indicators']]
    }
    MongoDb().update(data)
    return redirect('index')


@app.route('/delete', methods=['DELETE'])
def delete(ob_id):
    MongoDb().delete(ob_id)
    return redirect('index')

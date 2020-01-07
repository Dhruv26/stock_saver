from flask import request
from collections import defaultdict
from . import app
from .model import MongoDb
from .const import INDICATORS, INDICATORS_TYPES, PERIOD


@app.route('/get_table')
def get_table():
    data = []
    for entry in MongoDb().get_all():
        res = defaultdict(str)
        for group in entry['indicatorGroups']:
            for indicator in group['indicators']:
                #res[indicator['name']] += "|" + indicator['value'] + ' ({}) |\t'.format(indicator['period'][:1])
                if 'indicator' in indicator and indicator.get('value'):
                    res[indicator['indicator']] += indicator['value'] + '({}), '.format(indicator.get('period', '')[:1])
        res['StockName'] = entry['stockName']
        res['_id'] = str(entry['_id'])
        res.update({n: '' for n in INDICATORS if n not in res})
        data.append(res)
    return {
        "Status": 200,
        "Data": data,
    }


@app.route('/get_stock_info/<id>', methods=['GET', 'POST'])
def get_stock_info(id):
    stock_info = MongoDb().get_by_id(id)
    stock_info['_id'] = str(stock_info['_id'])
    return {
        "Status": 200,
        "Data": stock_info
    }


@app.route('/get_entry_meta_data', methods=['GET'])
def get_entry_meta_data():
    return {
        "Status": 200,
        "Data": {
            'indicators': INDICATORS,
            'indicatorTypes': INDICATORS_TYPES,
            'timePeriods': PERIOD
        }
    }


@app.route('/add', methods=['GET', 'POST'])
def add():
    MongoDb().insert(request.json)
    return {
        "Status": 201
    }


@app.route('/update', methods=['POST'])
def update():
    data = request.json
    ob_id = data['id']
    MongoDb().update(ob_id, data)
    return {
        "Status": 201
    }


@app.route('/delete/<id>', methods=['GET', 'POST', 'DELETE'])
def delete(id):
    MongoDb().delete(id)
    return {
        "Status": 201
    }

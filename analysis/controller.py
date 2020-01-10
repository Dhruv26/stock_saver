from flask import request
from datetime import date
from collections import defaultdict
from . import app
from .model import MongoDb
from .const import INDICATORS, INDICATORS_TYPES, PERIOD
from .processor import TechAnalysis


@app.route('/get_table')
def get_table():
    data = []
    for entry in MongoDb().get_all():
        res = defaultdict(str)
        for group in entry['indicatorGroups']:
            res['_id'] = str(entry['_id'])
            res['StockName'] = entry['stockName'] + ' ({})'.format(entry.get('Date'))
            res['Alert'] = False
            try:
                tech_analysis = TechAnalysis(entry['stockName'])
                res['LivePrice'] = round(tech_analysis.get_live_price(), 3)
            except:
                res['LivePrice'] = ''
            for indicator in group['indicators']:
                if 'indicator' in indicator and indicator.get('value'):
                    if indicator['indicator'] != 'PRICE':
                        res[indicator['indicator']] += indicator['value'] + '({}), '.format(
                            indicator.get('period', '')[:1])
                    else:
                        res[indicator['indicator']] += indicator['value'] + ', '
                        try:
                            price = float(indicator['value'])
                            if res['LivePrice']:
                                perc_val = price * 0.05
                                if price - perc_val <= res['LivePrice'] <= price + perc_val:
                                    res['Alert'] = True
                        except:
                            pass
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
    data = request.json
    data['Date'] = str(date.today())
    MongoDb().insert(data)
    return {
        "Status": 201
    }


@app.route('/update', methods=['POST'])
def update():
    data = request.json
    ob_id = data['_id']
    data.pop('_id', None)
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

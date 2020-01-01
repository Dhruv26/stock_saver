from flask_table import Table, Col, ButtonCol


class HomePageTable(Table):
    _id = Col('ID', show=False)
    stock_name = Col('Name')
    rsi = Col('RSI')
    ema = Col('EMA')
    sma = Col('SMA')
    delete = ButtonCol('Delete', 'delete', url_kwargs=dict(id='_id'))
    more_info = ButtonCol('More Info', 'get_more_info', url_kwargs=dict(id='_id'))


class MoreInfoTable(Table):
    #stock_name = Col('Name')
    indicator = Col('INDICATOR')
    type = Col('TYPE')
    value = Col('VALUE')

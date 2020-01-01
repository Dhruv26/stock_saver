from flask_table import Table, Col, ButtonCol


class HomePageTable(Table):
    _id = Col('ID', show=False)
    stock_name = Col('Name')
    RSI = Col('RSI')
    EMA = Col('EMA')
    SMA = Col('SMA')
    DELETE = ButtonCol('Delete', 'delete', url_kwargs=dict(id='_id'))

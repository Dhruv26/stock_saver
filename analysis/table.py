from flask_table import Table, Col


class HomePageTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover']
    _id = Col('ID', show=False)
    stock_name = Col('Name')
    RSI = Col('RSI')
    EMA = Col('EMA')
    SMA = Col('SMA')

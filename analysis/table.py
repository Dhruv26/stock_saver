from flask_table import Table, Col, ButtonCol


class HomePageTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover']
    _id = Col('ID', show=False)
    stock_name = Col('Name')
    RSI = Col('RSI')
    EMA = Col('EMA')
    SMA = Col('SMA')
    delete = ButtonCol('Delete', 'delete', url_kwargs=dict(id='_id'))
    more_info = ButtonCol('More Info', 'get_more_info', url_kwargs=dict(id='_id'))


class MoreInfoTable(Table):
    group_name = Col('Group')
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover']
    indicator = Col('INDICATOR')
    type = Col('TYPE')
    period = Col('PERIOD')
    value = Col('VALUE')
    comment = Col('Comment')
    date_ref = Col('Historical Date Ref')


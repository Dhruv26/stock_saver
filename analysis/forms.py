from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms import FieldList, FormField


class ParameterForm(FlaskForm):
    type = SelectField(label='Parameter Type', choices=[('cross', 'CROSS'), ('val', 'VALUE')])
    name = SelectField(label='Indicator', choices=[('rsi', 'RSI'), ('sma', 'SMA'), ('ema', 'EMA')])
    value = StringField(label='Value')


class AddEntryForm(FlaskForm):
    stock_name = StringField('Stock Name')
    flist = FieldList(FormField(ParameterForm), min_entries=1)
    add_parameter = SubmitField('Add Parameter')
    submit = SubmitField('Submit')

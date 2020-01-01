from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FieldList, FormField
from wtforms import validators


class ParameterForm(FlaskForm):
    type = SelectField(label='Parameter Type',
                       choices=[('cross', 'CROSS'), ('val', 'VALUE')],
                       validators=[validators.DataRequired()])
    name = SelectField(label='Indicator',
                       choices=[('rsi', 'RSI'), ('sma', 'SMA'), ('ema', 'EMA')],
                       validators=[validators.DataRequired()])
    value = StringField(label='Value', validators=[validators.DataRequired()])


class AddEntryForm(FlaskForm):
    stock_name = StringField('Stock Name', [validators.DataRequired()])
    indicators = FieldList(FormField(ParameterForm), min_entries=1)
    submit = SubmitField('Submit')

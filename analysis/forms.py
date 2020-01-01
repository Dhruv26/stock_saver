from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired
from .indicators import INDICATORS


class ParameterForm(FlaskForm):
    type = SelectField(label='Parameter Type',
                       validators=[DataRequired()],
                       choices=[('cross', 'CROSS'), ('val', 'VALUE')])
    name = SelectField(label='Indicator',
                       validators=[DataRequired()],
                       choices=[(k, v) for k, v in INDICATORS.items()])
    value = StringField(label='Value', validators=[DataRequired()])


class AddEntryForm(FlaskForm):
    stock_name = StringField(label='Stock Name', validators=[DataRequired()])
    indicators = FieldList(FormField(ParameterForm), min_entries=1)
    submit = SubmitField('Submit')

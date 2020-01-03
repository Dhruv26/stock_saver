from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired
from .const import INDICATORS, PERIOD, INDICATORS_TYPES


class ParameterForm(FlaskForm):
    type = SelectField(label='Parameter Type',
                       validators=[DataRequired()],
                       choices=[(k, v) for k, v in INDICATORS_TYPES.items()])
    period = SelectField(
        label='Period', validators=[DataRequired()], choices=[(n, n) for n in PERIOD])
    name = SelectField(label='Indicator',
                       validators=[DataRequired()],
                       choices=[(n, n) for n in INDICATORS])
    other_name = StringField(label='Other Indicator(optional)')
    value = StringField(label='Value')

    class Meta:
        csrf = False


class AddEntryForm(FlaskForm):
    stock_name = StringField(label='Stock Name', validators=[DataRequired()])
    indicators = FieldList(FormField(ParameterForm), min_entries=1)
    submit = SubmitField('Submit')

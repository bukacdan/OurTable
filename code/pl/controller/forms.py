from typing import Any

from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, TimeField
from wtforms.fields import BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired


class ReservationForm(FlaskForm):
    """
    A class for obtaining inputs from reservation form

    asks for number of guests, date and time of reservation
    all fields are required
    """

    guests_cnt = SelectField(
        'počet hostů',
        validators=[DataRequired()],
        choices=[i for i in range(1, 60)])

    date = DateField(
        'datum',
        validators=[DataRequired()])

    time = TimeField(
        'čas',
        validators=[DataRequired()],
        format='%H:%M'
    )

    submit = SubmitField('Rezervovat')


class TableSelectForm(FlaskForm):
    """
    A class for obtaining input from table select form

    only asks for table identificator
    """
    table_id = SelectField(
        'vyberte číslo stolu',
        validators=[DataRequired()],
        choices=[])

    submit = SubmitField('Vybrat')


    def __init__(self, tables:list, *args:Any, **kwargs:Any) -> None:
        """
        class construtor

        inits super class with args and kwargs
        sets choices to list 
        """
        super().__init__(*args, **kwargs)
        self.table_id.choices = list(map(lambda x: x.StulID, tables))

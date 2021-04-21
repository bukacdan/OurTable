from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, TimeField
from wtforms.fields import BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired


class ReservationForm(FlaskForm):
    """
    Reservation form

    asks for number of guests and datetime for reservation
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
    Simple form for user to select table id
    """
    table_id = SelectField(
        'vyberte číslo stolu',
        validators=[DataRequired()],
        choices=[])

    submit = SubmitField('Vybrat')


    def __init__(self, tables, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table_id.choices = list(map(lambda x: x.StulID, tables))

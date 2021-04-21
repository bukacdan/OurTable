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
        validators=[DataRequired()]
    )

    submit = SubmitField('Register')

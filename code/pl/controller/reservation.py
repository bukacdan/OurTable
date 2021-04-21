from flask import Blueprint, render_template
from .forms import ReservationForm

reservation_bp = Blueprint('reservation_bp', __name__)

@reservation_bp.route('/reserve', methods=['GET', 'POST'])
def reserve():
    form = ReservationForm()
    sent_data = []
    if form.validate_on_submit():
        pass
    return render_template('reservation.html', form=form, sent_data=sent_data)
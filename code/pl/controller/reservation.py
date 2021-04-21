from flask import Blueprint, render_template, redirect, url_for, request
from .forms import ReservationForm, TableSelectForm
from dl.mapper.table import TableMapper
from datetime import datetime

reservation_bp = Blueprint('reservation_bp', __name__, url_prefix='/reserve')


@reservation_bp.route('', methods=['GET'])
def reserve():
    form = ReservationForm()
    sent_data = []
    if form.validate_on_submit():
        console.log('here')
        return redirect(
            url_for('reservation_bp.select-table', date=form.date.data, time=form.time.data, people=form.guests_cnt.data))

    return render_template('reservation.html', form=form, sent_data=sent_data)


@reservation_bp.route('select-table', methods=['GET', 'POST'])
def select_table():
    dtime_str = str(request.form['date']) + ' ' + str(request.form['time'])
    dtime = datetime.fromisoformat(dtime_str)
    free_tables = TableMapper.get_all_free(dtime, request.form['guests_cnt'])
    form = TableSelectForm(tables=free_tables)
    return render_template('table_select.html', tables=free_tables, form=form)


@reservation_bp.route('finish', methods=['GET', 'POST'])
def finish():
    pass
from flask import Blueprint, render_template, redirect, url_for, request, flash
from .forms import ReservationForm, TableSelectForm
from dl.mapper.table import TableMapper
from datetime import datetime
from werkzeug import exceptions

reservation_bp = Blueprint('reservation_bp', __name__, url_prefix='/reserve')


@reservation_bp.route('', methods=['GET', 'POST'])
def reserve():
    form = ReservationForm()
    if form.validate_on_submit():
        return redirect(url_for('reservation_bp.select_table', date=form.date.data, time=form.time.data, guests_cnt=form.guests_cnt.data))
    return render_template('reservation.html', form=form)


@reservation_bp.route('select-table', methods=['GET', 'POST'])
def select_table():
    dtime_str = str(request.args['date']) + ' ' + str(request.args['time'])
    dtime = datetime.fromisoformat(dtime_str)
    free_tables = TableMapper.get_all_free(
        dtime, request.args['guests_cnt'])
    form = TableSelectForm(tables=free_tables)
    if form.validate_on_submit():
        return redirect(url_for('reservation_bp.finish', table_id=request.form['table_id'], dtime=dtime))
    return render_template('table_select.html', tables=free_tables, form=form)
    

@reservation_bp.route('finish', methods=['GET', 'POST'])
def finish():
    dtime = datetime.fromisoformat(request.args['dtime'])
    table_id = request.args['table_id']
    success = False
    return render_template('reserve_final.html', dtime=dtime, table_id=table_id, success=success)

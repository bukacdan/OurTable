from typing import Union

from flask import Blueprint, render_template, redirect, url_for, request
from .forms import ReservationForm, TableSelectForm
from bl.services.table import TableService

from dl.mapper.table import ITableMapper
from bl.services.reservation import ReservationService

from datetime import datetime
from werkzeug import exceptions, Response


class ReservationController:
    """
    a class for controlling reservation blueprint

    handles routing, using forms, checking free tables and creating reservation
    """
    # create modulable blueprint
    reservation_bp = Blueprint(
        'reservation_bp', __name__, url_prefix='/reserve')  # all bp routes prefixed with '/reserve'

    @staticmethod
    @reservation_bp.route('', methods=['GET', 'POST'])
    def reserve() -> Union[str, Response]:
        """
        routes to /reserve/

        renders reservation form and obtains its data
        if form validation successful, redirects to select_table
        """
        form = ReservationForm()
        if form.validate_on_submit():
            return redirect(url_for('reservation_bp.select_table', date=form.date.data, time=form.time.data, guests_cnt=form.guests_cnt.data))
        return render_template('reservation.html', form=form)

    @staticmethod
    @reservation_bp.route('select-table', methods=['GET', 'POST'])
    def select_table(table_mapper: ITableMapper) -> Union[str, Response]:
        """
        routes to /reserve/select-table

        renders select table form and obtains its data
        if form validation successful, redirects to finish
        """
        dtime_str = str(request.args['date']) + ' ' + str(request.args['time'])
        dtime = datetime.fromisoformat(dtime_str)
        free_tables = TableService.get_free_tables(
            dtime, request.args['guests_cnt'], table_mapper)
        form = TableSelectForm(tables=free_tables)
        if form.validate_on_submit():
            return redirect(url_for('reservation_bp.finish', table_id=request.form['table_id'], dtime=dtime))
        return render_template('table_select.html', tables=free_tables, form=form)

    @staticmethod
    @reservation_bp.route('finish', methods=['GET', 'POST'])
    def finish(reservation_service_mapper:ReservationService, table_mapper:ITableMapper) -> str:
        """
        routes to /reserve/finish

        renders validation confirmation depending on reservation success
        """
        dtime = datetime.fromisoformat(request.args['dtime'])
        table_id = request.args['table_id']
        success = reservation_service_mapper.add_reservation(dtime, table_id, table_mapper)
        return render_template('reserve_final.html', dtime=dtime, table_id=table_id, success=success)

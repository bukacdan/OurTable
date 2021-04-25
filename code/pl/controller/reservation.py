from typing import Union

from flask import Blueprint, render_template, redirect, url_for, request
from .forms import ReservationForm, TableSelectForm

from bl.services.tableservice import TableService
from bl.services.reservationservice import ReservationService

from dl.mapper.table import ITableMapper
from dl.mapper.schedule import IScheduleMapper
from dl.mapper.reservation import IReservationMapper

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
    def select_table(table_service_mapper: TableService, table_mapper: ITableMapper,  schedule_mapper: IScheduleMapper) -> Union[str, Response]:
        """
        routes to /reserve/select-table

        renders select table form and obtains its data
        if form validation successful, redirects to finish
        """
        dtime_str = str(request.args['date']) + ' ' + str(request.args['time'])
        dtime = datetime.fromisoformat(dtime_str)
        free_tables = table_service_mapper.get_free_tables(
            dtime, request.args['guests_cnt'], table_mapper, schedule_mapper)
        form = TableSelectForm(tables=free_tables)
        if form.validate_on_submit():
            return redirect(url_for('reservation_bp.finish', table_id=request.form['table_id'], dtime=dtime))
        return render_template('table_select.html', tables=free_tables, form=form)

    @staticmethod
    @reservation_bp.route('finish', methods=['GET', 'POST'])
    def finish(reservation_service_mapper: ReservationService, reservation_mapper: IReservationMapper) -> str:
        """
        routes to /reserve/finish

        renders validation confirmation depending on reservation success
        """
        dtime = datetime.fromisoformat(request.args['dtime'])
        table_id = request.args['table_id']
        success = reservation_service_mapper.add_reservation(dtime, table_id, reservation_mapper)
        return render_template('reserve_final.html', dtime=dtime, table_id=table_id, success=success)

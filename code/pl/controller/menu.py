from flask import render_template, Blueprint
from dl.mapper.imeal import IMealMapper

menu_bp = Blueprint('menu_bp', __name__)

@menu_bp.route('/menu')
def menu(mapper: IMealMapper):
    menu_items = mapper.get_all()
    return render_template('menu.html', items=menu_items)
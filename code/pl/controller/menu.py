from flask import render_template, Blueprint
from .menuItems import get_items
from dl.mapper.meal import MealMapper

menu_bp = Blueprint('menu_bp', __name__)

@menu_bp.route('/menu')
def menu():
    menu_items = MealMapper.get_all()
    return render_template('menu.html', items=menu_items)
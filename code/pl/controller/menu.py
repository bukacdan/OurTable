from flask import render_template, Blueprint
from dl.mapper.meal import MealMapper


class MenuController:
    """
    a class for controlling menu blueprint

    handles routing and obtaining menu from database
    """
    # create modulable blueprint
    menu_bp = Blueprint('menu_bp', __name__)

    @staticmethod
    @menu_bp.route('/menu')
    def menu() -> str:
        """
        routes to menu

        renders list of restaurant's meals
        """
        menu_items = MealMapper.get_all()
        return render_template('menu.html', items=menu_items)

from flask import Blueprint, render_template


class HomeController:
    """
    a class for controlling home blueprint

    handles routing 
    """
    # create modulable blueprint
    home_bp = Blueprint('home_bp', __name__)

    @staticmethod
    @home_bp.route('/')
    def home() -> str:
        """
        routes homepage of app
        """
        return render_template('index.html')

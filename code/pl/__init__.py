from typing import Any

import os
from flask import Flask
from sassutils.wsgi import SassMiddleware


class AppFactory:
    """
    a class responsible for creation of app
    """
    @staticmethod
    def register_context(app:Any) -> None:
        """
        register app's dependencies
        """
        from .controller import home, menu, reservation
        app.register_blueprint(home.HomeController.home_bp)
        app.register_blueprint(menu.MenuController.menu_bp)
        app.register_blueprint(
            reservation.ReservationController.reservation_bp)

    @staticmethod
    def create_app(test_config:dict=None) -> Any:
        """
        creates flask app
        """
        app:Any = Flask(__name__, instance_relative_config=True)
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        )

        app.wsgi_app = SassMiddleware(app.wsgi_app, {
            __name__: ('static/sass', 'static/css', '/static/css')
        })

        if test_config is None:
            # Load the instance config, if it exists, when not testing
            app.config.from_pyfile('config.py', silent=True)
        else:
            # Load the test config if passed in
            app.config.from_mapping(test_config)

        # ensure the instance folder exists
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        with app.app_context():
            AppFactory.register_context(app)

        return app


app = AppFactory.create_app()

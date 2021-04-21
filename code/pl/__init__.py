import os, sys, inspect

from flask import Flask
from flask_injector import FlaskInjector

from sassutils.wsgi import SassMiddleware

from config import configure


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
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

    #from dl import db
    #db.init_app(app)

    from .controller import home, menu, reservation
    app.register_blueprint(home.home_bp)
    app.register_blueprint(menu.menu_bp)
    app.register_blueprint(reservation.reservation_bp)

    FlaskInjector(app=app, modules=[configure])

    return app

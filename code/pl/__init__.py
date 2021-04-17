import os

from flask import Flask
from flask_assets import Environment, Bundle

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    assets = Environment(app)
    assets.url = app.static_url_path
    scss_files = [f for f in os.listdir('./app/' + str(app.static_url_path)) if f.endswith(".scss")]
    scss_bundle = Bundle(*scss_files, filters='pyscss', output='all.css')
    assets.register('scss_all', scss_bundle)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    with app.app_context():
        from . import db
        db.init_app(app)

        from .controlers import home
        
    return app
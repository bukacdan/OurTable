from flask import current_app as app
from flask_assets import Environment, Bundle

bundles = {
    'styles_global': Bundle(
        'scss/style.scss',
        'scss/home.scss',
        filters='pyscss',
        output='css/all.css'
    ),
}

assets = Environment(app)
assets.append_path(app.static_folder)
assets.append_path(str(app.root_path) + '/home/static/')
assets.register(bundles)
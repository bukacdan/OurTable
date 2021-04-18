from flask import Flask, url_for, render_template, request, jsonify
from markupsafe import escape
from dl.db import add_address as add_address_db
from dl.db import add_alergen as add_allergen_db
#from . import auth

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tables/all', methods=['GET'])
def get_tables():
    return ""


@app.route('/meals/all', methods=['GET'])
def get_meals():
    return ""


@app.route('/meals', methods=['POST'])
def add_meal():
    return ""


@app.route('/menus/all', methods=['GET'])
def get_menus():
    return ""


@app.route('/menus/', methods=['POST'])
def add_menu():
    return ""


@app.route('/menus/', methods=['DELETE'])
def delete_menu():
    return ""


@app.route('/orders', methods=['POST'])
def add_order():
    return ""


@app.route('/reservations/all', methods=['GET'])
def get_reservations():
    return ""


@app.route('/reservations', methods=['POST'])
def add_reservation():
    return ""


@app.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation():
    return ""


@app.route('/addresses', methods=['POST'])
def add_address():
    # TODO read values from form
    city: str
    psc: str
    state: str
    street: str

    add_address_db(city, psc, state, street)


@app.route('allergen/all', methods=['GET'])
def get_allergens():
    return ""


@app.route('/allergens', method=['POST'])
def add_allergen():
    # TODO read value from form
    name: str

    add_allergen_db(name)


@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    return ""


@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    return ""

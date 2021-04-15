from flask import Flask, url_for, render_template, request
from markupsafe import escape
from . import auth

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


@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    return ""


@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    return ""

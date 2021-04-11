from flask import Flask, url_for, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    return f'Post {post_id}'


@app.route('/image')
def image():
    return f"<img src=\"{url_for('static', filename='test.jpg')}\">"


@app.route('/hello/')
@app.route('/hello/<name>')
def render(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'Post: {username} - {password}'
    else:
        # Get
        return f"Get {request.args.get('key', '')}"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('image'))
    print(url_for('static', filename='test.jpg'))

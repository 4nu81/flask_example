import click
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.cli.command('hello')
@click.argument('name')
def hello(name):
    res = f"Hello {name}"
    print(res)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app')
def to_app():
    zeuch = ['dies','kommt','aus','einer','liste']
    return render_template('app.html', zeuch=zeuch)

def get_num(num):
    if num not in range(10):
        abort(404)
    return num

@app.route('/<int:num>')
def num(num):
    num = get_num(num)
    return render_template('num.html', num=num)

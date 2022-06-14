import json
import os

import click
from flask import Flask, render_template, request
from werkzeug.exceptions import abort

from middleware import middleware

app = Flask(__name__)

### Basic Middleware Method ##
app.wsgi_app = middleware(app.wsgi_app)

### injected Middleware functions ###
def before_req_func():
    print(f"sparked before request procession")

def after_req_func(res):
    print(f"sparked after request procession")
    print(res.content_type, res.response)
    return res

app.before_request_funcs = {
    None: [before_req_func]
}
app.after_request_funcs = {
    None: [after_req_func]
}

### Routes To HTML Views ###

@app.cli.command('hello')
@click.argument('name')
def hello(name):
    res = f"Hello {name}"
    print(res)

@app.route('/', methods=['GET'])
def index():
    return render_template('index_form.html')

@app.route('/', methods=['POST'])
def index_post():
    values = request.form
    return render_template('index.html', form_data=values)

@app.route('/app')
def to_app():
    zeuch = ['dies','kommt','aus','einer','liste']
    return render_template('app.html', zeuch=zeuch)

@app.route('/<int:num>')
def num(num):
    if num not in range(10):
        ### simple 404 example
        abort(404)
    return render_template('num.html', num=num)

### Routes To Json Views ###

@app.route('/hello/<string:name>')
def hello_name(name):
    return json.dumps({"hello": name})

### Import Debugger if needed ###

if os.getenv("PYTHONDEBUGGER") == "True":
    import multiprocessing
    if multiprocessing.current_process().pid > 1:
        import debugpy
        debugpy.listen(("0.0.0.0", 3000))
        print("⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳")

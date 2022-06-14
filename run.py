import os

import click
from flask import Flask, render_template, request
from werkzeug.exceptions import abort

app = Flask(__name__)

def before_req_middleware():
    print(f"sparked before request procession")

def after_req_middleware(res):
    print(f"sparked after request procession")
    print(res.content_type, res.response)
    return res

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

def get_num(num):
    if num not in range(10):
        abort(404)
    return num

@app.route('/<int:num>')
def num(num):
    num = get_num(num)
    return render_template('num.html', num=num)

app.before_request_funcs = {
    None: [before_req_middleware]
}
app.after_request_funcs = {
    None: [after_req_middleware]
}

if os.getenv("PYTHONDEBUGGER") == "True":
    import multiprocessing
    if multiprocessing.current_process().pid > 1:
        import debugpy
        debugpy.listen(("0.0.0.0", 3000))
        print("⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳")

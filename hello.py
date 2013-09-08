import os
from flask import Flask
from flask import render_template

PROJECT_DIR = os.path.dirname(__file__) # this is not Django setting.
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
    # here you can add another templates directory if you wish.
)
app = Flask(__name__)

@app.route('/')
def hello(name='Hello World!'):
	return render_template('hello.html', name=name)

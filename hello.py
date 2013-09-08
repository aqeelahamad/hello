import os
from flask import Flask
from flask import render_template

TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, "templates")

app = Flask(__name__)

@app.route('/')
def hello(name='Hello World!'):
	return render_template('hello.html', name=name)

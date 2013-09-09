import os
from flask import Flask
from flask import render_template

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
# ...
app = Flask('myapp', template_folder=tmpl_dir)
app = Flask(__name__)

@app.route('/')
def hello():
	name='Hello World!'
	#return render_template('hello.html', name=name)
	return name
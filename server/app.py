from flask import Flask, render_template

app = Flask(__name__)
import logging
logging.basicConfig(format='%(message)s', level=logging.INFO)


@app.route('/')
def index():
    return render_template('index.html')




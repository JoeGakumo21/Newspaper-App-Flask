from flask import render_template
from app import app

#ViewDisplay
@app.route('/')
def index():
    '''
    ViewDisplay root page function that retruns the index page and its data
    '''
    return render_template('index.html')
from flask import render_template
from app import app

#ViewDisplay
@app.route('/')
def index():
    '''
    ViewDisplay root page function that retruns the index page and its data
    '''
    landing="Welcome to Newspaper Application "
    return render_template('index.html',landing=landing)

@app.route('/bussiness')  
def bussiness():
    '''
    
    '''  
    
    return render_template('bussiness.html',)

@app.route('/technology')
def technology():
    '''
    
    '''  
    title="Technology" 
    return render_template('technology.html',) 
@app.route('/sports')
def sports():
    '''
    
    '''   
    return render_template('sports.html',)
@app.route('/entertain')
def entertain():
    '''
    
    '''     
    return render_template('entertain.html')

